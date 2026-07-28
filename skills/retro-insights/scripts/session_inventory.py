#!/usr/bin/env python3
"""Build a privacy-sanitized inventory of local Codex root sessions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


WINDOW_RE = re.compile(r"^(\d+)([hdw])$")
PROBE_RE = re.compile(r"^(?:what is 2\+2\? reply with just the number\.?|\d+)$", re.I)
BLOCK_PATTERNS = [
    re.compile(r"<environment_context>.*?</environment_context>", re.S),
    re.compile(r"<codex_internal_context.*?</codex_internal_context>", re.S),
    re.compile(r"<in-app-browser-context.*?</in-app-browser-context>", re.S),
    re.compile(r"<recommended_plugins>.*?</recommended_plugins>", re.S),
    re.compile(r"<turn_aborted>.*?</turn_aborted>", re.S),
]
SECRET_PATTERNS = [
    (re.compile(r"\b(?:sk|rk|pk)-[A-Za-z0-9_-]{16,}\b"), "<redacted-token>"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"), "<redacted-github-token>"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{12,}={0,2}"), "Bearer <redacted>"),
    (re.compile(r"(?i)\b(api[_-]?key|access[_-]?token|refresh[_-]?token|password)\s*[:=]\s*[^\s,;]+"), r"\1=<redacted>"),
    (re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I), "<redacted-email>"),
    (re.compile(r"(?<!\w)/(?:Users|home)/[^\s,;:)\]}>]+"), "<redacted-local-path>"),
    (re.compile(r"(?i)\b[A-Z]:\\\\Users\\\\[^\s,;:)\]}>]+"), "<redacted-local-path>"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-root", type=Path, default=Path.home() / ".codex" / "sessions")
    parser.add_argument("--window", default="7d", help="Relative window such as 24h, 7d, 2w, or all")
    parser.add_argument("--since", help="Absolute inclusive start date/time in ISO format")
    parser.add_argument("--until", help="Absolute exclusive end date/time in ISO format")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--max-messages", type=int, default=8)
    parser.add_argument("--max-chars", type=int, default=420)
    parser.add_argument("--cwd-prefix", default="")
    parser.add_argument("--include-probes", action="store_true")
    parser.add_argument("--include-automation", action="store_true")
    parser.add_argument(
        "--include-local-details",
        action="store_true",
        help="Include raw session IDs, local paths, client metadata, and the cwd filter value",
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    return parser.parse_args()


def parse_iso(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def resolve_bounds(args: argparse.Namespace) -> tuple[datetime, datetime]:
    now = datetime.now(timezone.utc)
    until = parse_iso(args.until) if args.until else now
    if args.since:
        since = parse_iso(args.since)
    elif args.window == "all":
        since = datetime.min.replace(tzinfo=timezone.utc)
    else:
        match = WINDOW_RE.fullmatch(args.window)
        if not match:
            raise ValueError("--window must look like 24h, 7d, or 2w")
        count = int(match.group(1))
        unit = match.group(2)
        delta = timedelta(hours=count) if unit == "h" else timedelta(days=count * (7 if unit == "w" else 1))
        since = until - delta
    if since >= until:
        raise ValueError("since must be earlier than until")
    return since, until


def read_meta(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                if item.get("type") == "session_meta":
                    return item.get("payload", {})
                return None
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None
    return None


def sanitize(text: str, max_chars: int) -> str:
    cleaned = text
    for pattern in BLOCK_PATTERNS:
        cleaned = pattern.sub(" ", cleaned)
    cleaned = re.sub(
        r"# AGENTS\.md instructions(?: for [^\n<]+)?\s*<INSTRUCTIONS>.*?</INSTRUCTIONS>",
        " ",
        cleaned,
        flags=re.S,
    )
    for pattern, replacement in SECRET_PATTERNS:
        cleaned = pattern.sub(replacement, cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if len(cleaned) > max_chars:
        cleaned = cleaned[: max_chars - 1].rstrip() + "…"
    return cleaned


def user_messages(path: Path, max_chars: int) -> list[str]:
    messages: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if item.get("type") != "response_item":
                    continue
                payload = item.get("payload", {})
                if payload.get("type") != "message" or payload.get("role") != "user":
                    continue
                texts = [
                    block.get("text", "")
                    for block in payload.get("content", [])
                    if isinstance(block, dict) and block.get("type") == "input_text"
                ]
                cleaned = sanitize(" ".join(texts), max_chars)
                if cleaned:
                    messages.append(cleaned)
    except (OSError, UnicodeDecodeError):
        return []
    return messages


def is_probe(messages: list[str]) -> bool:
    if not messages:
        return True
    return all(PROBE_RE.fullmatch(message.strip()) is not None or len(message.strip()) <= 2 for message in messages)


def selected_messages(messages: list[str], limit: int) -> list[str]:
    if len(messages) <= limit:
        return messages
    head = max(1, limit // 3)
    tail = max(1, limit - head)
    return messages[:head] + messages[-tail:]


def session_record(path: Path, meta: dict[str, Any], args: argparse.Namespace) -> dict[str, Any] | None:
    try:
        timestamp = parse_iso(str(meta.get("timestamp", "")))
    except (ValueError, TypeError):
        return None
    cwd = str(meta.get("cwd", ""))
    if args.cwd_prefix and not cwd.startswith(args.cwd_prefix):
        return None
    messages = user_messages(path, args.max_chars)
    probe = is_probe(messages)
    if probe and not args.include_probes:
        return None
    chosen = selected_messages(messages, args.max_messages)
    title = chosen[0][:140] if chosen else "(no meaningful user message)"
    record = {
        "timestamp": timestamp.isoformat().replace("+00:00", "Z"),
        "title": title,
        "user_message_count": len(messages),
        "messages": chosen,
        "is_probe": probe,
    }
    if args.include_local_details:
        record.update(
            {
                "id": str(meta.get("id") or meta.get("session_id") or path.stem),
                "cwd": cwd,
                "thread_source": str(meta.get("thread_source", "")),
                "originator": str(meta.get("originator", "")),
                "cli_version": str(meta.get("cli_version", "")),
                "model_provider": str(meta.get("model_provider", "")),
                "path": str(path),
            }
        )
    return record


def collect(args: argparse.Namespace) -> dict[str, Any]:
    since, until = resolve_bounds(args)
    counters = {
        "files_scanned": 0,
        "sessions_in_window": 0,
        "root_user_sessions": 0,
        "automation_sessions": 0,
        "subagent_or_child_sessions": 0,
        "probe_sessions_excluded": 0,
    }
    records: list[dict[str, Any]] = []
    if not args.session_root.exists():
        raise FileNotFoundError(f"session root not found: {args.session_root}")

    for path in args.session_root.rglob("rollout-*.jsonl"):
        counters["files_scanned"] += 1
        meta = read_meta(path)
        if not meta:
            continue
        try:
            timestamp = parse_iso(str(meta.get("timestamp", "")))
        except (ValueError, TypeError):
            continue
        if not (since <= timestamp < until):
            continue
        counters["sessions_in_window"] += 1
        source = str(meta.get("thread_source", ""))
        parent = str(meta.get("parent_thread_id") or "")
        if parent or source == "subagent":
            counters["subagent_or_child_sessions"] += 1
            continue
        if source == "automation":
            counters["automation_sessions"] += 1
            if not args.include_automation:
                continue
        elif source != "user":
            continue
        else:
            counters["root_user_sessions"] += 1

        record = session_record(path, meta, args)
        if record is None:
            if not args.include_probes:
                messages = user_messages(path, args.max_chars)
                if is_probe(messages):
                    counters["probe_sessions_excluded"] += 1
            continue
        records.append(record)

    records.sort(key=lambda item: item["timestamp"], reverse=True)
    records = records[: args.limit]
    for index, record in enumerate(records, start=1):
        record["label"] = f"session-{index:03d}"
    return {
        "scope": {
            "since": since.isoformat().replace("+00:00", "Z"),
            "until": until.isoformat().replace("+00:00", "Z"),
            "limit": args.limit,
            "cwd_filter_applied": bool(args.cwd_prefix),
            "cwd_prefix": args.cwd_prefix if args.include_local_details else None,
            "include_probes": args.include_probes,
            "include_automation": args.include_automation,
            "include_local_details": args.include_local_details,
        },
        "counts": {**counters, "returned_sessions": len(records)},
        "sessions": records,
    }


def markdown(data: dict[str, Any]) -> str:
    counts = data["counts"]
    lines = [
        "# Codex Session Inventory",
        "",
        f"- Range: `{data['scope']['since']}` to `{data['scope']['until']}`",
        f"- Root user sessions: {counts['root_user_sessions']}",
        f"- Returned substantive sessions: {counts['returned_sessions']}",
        f"- Excluded probes: {counts['probe_sessions_excluded']}",
        f"- Child/subagent sessions: {counts['subagent_or_child_sessions']}",
        "",
        "| Time (UTC) | Session | Theme | Messages |",
        "|---|---|---|---:|",
    ]
    if data["scope"]["include_local_details"]:
        lines[-2:] = [
            "| Time (UTC) | Session | CWD | Theme | Messages |",
            "|---|---|---|---|---:|",
        ]
    for session in data["sessions"]:
        theme = str(session["title"]).replace("|", "\\|")
        if data["scope"]["include_local_details"]:
            cwd = str(session["cwd"]).replace("|", "\\|")
            lines.append(
                f"| {session['timestamp']} | `{session['id'][:8]}` | `{cwd}` | {theme} | {session['user_message_count']} |"
            )
        else:
            lines.append(
                f"| {session['timestamp']} | `{session['label']}` | {theme} | {session['user_message_count']} |"
            )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.limit <= 0 or args.max_messages <= 0 or args.max_chars < 80:
        print("limit/max-messages must be positive and max-chars must be >= 80", file=sys.stderr)
        return 2
    try:
        data = collect(args)
    except (ValueError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(markdown(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
