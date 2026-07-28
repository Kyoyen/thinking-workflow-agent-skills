# Preflight Brief Reference

Use this reference when the user wants more than a quick scan.

## Core Questions

Before action, answer:

1. Who has already tried something like this?
2. What part should we copy or adapt?
3. What part should we explicitly avoid?
4. Which heavier skill, if any, should take over?
5. What is the smallest next step that benefits from this knowledge?
6. What is the simplest viable path before custom work?
7. Is the next artifact clear enough, or should a requirements review interrogate it before execution?

## Brief Shape

```md
**Preflight Question**
<what we are checking before acting>

**Landscape**
<category, terminology, and existing precedent>

**Relevant Precedents**
| Option | Type | Borrow | Avoid | Evidence |
|---|---|---|---|---|

**Take The Essence**
- <specific behavior/API/UI/workflow/business/content/research pattern>

**Discard The Dross**
- <what not to copy>

**Routing**
- <continue here or route to a specialist skill>

**Simplest Viable Path**
- <skip / reuse / stdlib / native / installed dependency / wrap / minimum custom build>

**Recommendation**
<Build / adapt / integrate / wrap / route / defer> + next concrete step.
```

## Comparison Axes

- Capability fit: what user need it actually satisfies.
- Expected UX: what users already expect from known tools or concepts.
- Adoption signal: stars, downloads, public customers, marketplace rating, community, recency, citations, or standardization.
- Integration cost: APIs, SDKs, data model mismatch, deployment, auth, pricing, permissions, ops burden.
- Differentiation: what the user should not rebuild, and what could still be unique.
- Simplest viable path: what can be skipped, reused, configured, wrapped, or solved by stdlib/native/platform behavior before writing new code.
- Failure modes: abandoned repos, misleading demos, lock-in, legal/licensing constraints, missing edge cases.
- Evidence quality: primary source, date, source bias, and whether claims are verified by docs or code.

## Routing Boundaries

- Academic review: use a scholarly workflow with reproducible search and citations.
- Competitor dossier: use a structured competitor-research workflow.
- Chosen-technology best practice: use current official documentation and a version-aware technical workflow.
- Several known options need synthesis: use `fusion`.
- The problem boundary is unclear: use `scale`.
- Coding implementation after direction is clear: use an implementation workflow that enforces reuse, native-first choices, YAGNI, and a small correct change.
- Over-engineering review: use a simplification review that produces a concrete delete or replacement list.
- Plan, specification, ticket, or handoff ambiguity: use a requirements interrogation workflow.
- Local-only implementation: skip broad preflight and inspect the repository directly.

Use preflight to choose the next capability, not to duplicate that capability's full process.

## Plugin Feature Checklist

For plugin or extension ideas, check:

- Native capability: does the host app or OS already support this?
- Marketplace precedent: do users expect status indicators, commands, dashboard widgets, notifications, or integrations?
- Simplest viable path: can this be skipped, configured, wrapped, or handled by platform-native behavior before a new plugin exists?
- State model: idle, running, paused, completed, skipped, failed.
- User controls: start, pause, resume, skip, reset, configure.
- Notifications: sound, desktop notification, in-app badge, Do Not Disturb respect.
- Persistence: survive refresh/restart, multi-device sync, session history.
- Integrations: tasks, calendar, focus modes, analytics, team status, documents.
- Privacy and permissions: notification permission, background timers, activity tracking, external API access.
- Failure modes: drift, throttling, stale state, notification fatigue, overbuilt analytics.

## Useful Search Patterns

- `"<capability>" "open source"`
- `"<capability>" API docs`
- `"<capability>" alternatives`
- `"<host app>" plugin "<capability>"`
- `"<capability>" extension marketplace`
- `"<competitor/product>" pricing docs`
- `site:github.com "<capability>" stars`
- `"<concept>" paper` or `"<concept>" standard`
- `"<problem wording>" "best practices"`
