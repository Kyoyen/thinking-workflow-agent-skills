---
name: retro-insights
description: Reflect across sessions, projects, tools, and time windows to improve the working system. Use for periodic reviews of human-Agent collaboration, code and non-code projects, product work, collaboration platforms, documents, design, local environments, automation, and delivery. Identify repeated success patterns, recurring friction, user corrections, tool drift, and lessons that may deserve a durable rule. Trigger on retro-insights, agent insights, weekly reflection, repeated problems, cross-project retrospective, monthly review, insights report, or comparisons across 24 hours, 7 days, 30 days, recent sessions, and projects.
---

# Retro Insights

## Purpose

Turn evidence from several tasks into a testable improvement for the next cycle.

`preflight` asks what to learn before starting. `postflight` asks whether one task is truly complete. `retro-insights` asks what keeps repeating across tasks and which change deserves a place in a rule, Skill, hook, runbook, or automation.

Single-task acceptance belongs to `postflight`. Durable rule changes require separate confirmation.

## Method

This Skill combines session insight, engineering retrospectives, organizational learning, `preflight`, and `postflight` into a broad evidence loop:

- identify patterns from real tasks and reviewable evidence;
- cover code, non-code work, collaboration, environment, and delivery;
- keep lessons searchable, expirable, and reversible;
- preserve stage boundaries, evidence priority, the smallest next step, and selective durability.

Exclude vanity metrics, raw activity rankings, automatic global rules from one failure, repository-only views, long chronological logs, and dependency on an external memory service.

## Modes

| Input | Default scope | Focus |
|---|---|---|
| `retro-insights` | Last 7 days, up to 20 substantive root sessions | Periodic synthesis |
| `retro-insights 24h/7d/30d` | Requested window | Time trend |
| `retro-insights 20sessions` | Most recent 20 substantive root sessions | Session sample |
| `retro-insights compare` | Current 7 days versus previous 7 days | Whether an improvement worked |
| `retro-insights project <path>` | One project | Local project pattern |
| `retro-insights scheduled` | Last 7 days and a saved local report | Recurring review |

Use the last 7 days when the range is omitted.

## Evidence Pipeline

1. **Set the window and question:** efficiency, quality, collaboration, tool stability, cognitive bias, delivery, or durable rules.
2. **Read root sessions:** when authorized and supported, run `scripts/session_inventory.py`. Exclude sub-tasks, automation, empty inputs, and technical probes by default.
3. **Add engineering evidence:** inspect version control, tests, builds, and hotspots when relevant. Treat commit volume as activity.
4. **Add non-code evidence:** read selected project state, handoffs, postflight results, operational logs, authentication or network checks, and explicit user corrections. Activity summaries are routing clues.
5. **Build pattern cards:** record evidence count, distinct root sessions, domain spread, impact, confidence, counterexamples, and state.
6. **Separate levels:** distinguish facts, trends, inferences, recommendations, and unknowns.
7. **Propose the smallest change:** at most three actions per cycle, each testable in the next period.
8. **Decide on promotion:** use `references/evidence-and-promotion.md`.
9. **Review the previous cycle:** mark each earlier action `effective`, `ineffective`, `not executed`, or `insufficient evidence`.

## Optional Session Inventory

Locate the installed Skill:

```bash
RETRO_SKILL_DIR="$HOME/.agents/skills/retro-insights"
```

Recent seven days:

```bash
python3 "$RETRO_SKILL_DIR/scripts/session_inventory.py" --window 7d --limit 20 --format json
```

Recent twenty substantive sessions:

```bash
python3 "$RETRO_SKILL_DIR/scripts/session_inventory.py" --window all --limit 20 --format json
```

Project filter:

```bash
python3 "$RETRO_SKILL_DIR/scripts/session_inventory.py" --window 30d --cwd-prefix "/absolute/project/path" --format markdown
```

The script is an optional read-only adapter for local Codex session JSONL. It hides local paths and real session identifiers by default and redacts common credentials, email addresses, and user-directory paths. It cannot infer every company, project, or business term. Manually sanitize any result before sharing it.

## Observation Dimensions

Choose only those supported by evidence:

- work distribution across code, product, collaboration, documents, design, research, environment, automation, and delivery;
- successful routes, Skills, delivery structures, and verification methods;
- recurring friction such as timeouts, repeated retries, context contamination, path drift, file-provider issues, and dependency failures;
- user corrections to terminology, scope, sequence, aesthetics, evidence claims, communication, and authority;
- drift in clients, collaboration platforms, version control, providers, plugins, network, and authentication;
- alignment among entry points, manual trials, logs, tests, links, screenshots, files, and unverified items;
- task length, context compression, handoff quality, and when a new task would improve continuity;
- candidate changes to rules, Skills, hooks, runbooks, automation, or project documentation.

## Promotion

Keep global rules, project rules, hooks, and automation unchanged by default.

- One occurrence becomes an `observation`.
- Two distinct root sessions become a `watch item`; seek counterexamples.
- At least three root sessions across two domains, or explicit user confirmation, becomes a `promotion candidate`.
- Before writing, choose the narrowest useful destination.
- After writing, test whether the next cycle shows fewer errors or better outcomes. Revert or narrow an ineffective change.

When the user explicitly requests an immediate write, back up the target, apply the smallest patch, and read back the exact change.

## Output

```markdown
**Retro Insights Scope**
- Window, session count, domains, and evidence gaps.

**Effective Patterns**
- Pattern, evidence, why it worked, and whether to continue.

**Recurring Friction and Cost**
- Issue, occurrences, impact, root-cause confidence, and counterexamples.

**User Corrections and Boundary Changes**
- Correction, prior behavior, corrected boundary, and current durability.

**System Health and Drift**
- Tools, authentication, network, paths, Skills, and automation.

**Promotion Candidates**
| Candidate | Evidence | Destination | Confidence | State |
|---|---|---|---|---|

**Next-Cycle Experiments**
1. Up to three actions with validation signals.
```

In comparison mode, add the status of the previous cycle’s actions. Say plainly when no actionable insight exists.

## History and Scheduling

- Interactive use returns the report in chat.
- `scheduled`, `compare`, or an explicit save request writes a sanitized report to:

  ```text
  ./retro-insights-reports/
  ```

- Save topics, evidence counts, insights, actions, and validation state. Exclude full sessions, tokens, cookies, account identifiers, and sensitive business text.
- A seven-day report supports weekly reflection. A monthly review is a better place to approve promotion into durable rules.

## Routing

| Actual need | Route |
|---|---|
| One-repository engineering metrics | Engineering retrospective and version-control analysis |
| Engineering trends across tools and repositories | Cross-repository engineering analysis |
| Search, cleanup, or export of saved lessons | Long-term knowledge governance |
| Single-task acceptance and handoff | `postflight` |
| Pre-task precedent and shortest path | `preflight` |
| Synthesis of several approaches | `fusion` |
| Root cause of a failure event | Root-cause analysis, postmortem, or AAR |
| Recent activity context | Authorized activity history as a clue |

## Guardrails

- Judge output quality through outcomes and evidence. Treat sessions, tokens, lines of code, and commits as activity signals.
- Count only substantive user root sessions as user-session evidence.
- Summarize sensitive sessions through topics and evidence counts.
- Treat activity and interface state as clues; executable evidence proves completion.
- Keep one failure out of global rules.
- Keep reports and learning data local unless the user approves an external destination.
- Leave authentication, network, credential storage, and remote systems unchanged without approval.
- Limit each cycle to three improvement actions.

Read `references/evidence-and-promotion.md` when evaluating evidence strength, repeated patterns, and durable destinations.
