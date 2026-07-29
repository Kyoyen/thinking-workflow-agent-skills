---
name: postflight
description: Close non-trivial work through acceptance, operational readiness, recovery, maintenance, handoff, and the smallest next-cycle improvement. Use after implementation, research, planning, collaboration-platform work, document generation, Skill or plugin changes, cleanup, deployment, automation, design delivery, or any task preparing to declare completion. Trigger on postflight, closeout, acceptance check, delivery check, Definition of Done, operational readiness, maintenance, durability, handoff, rollback, or questions about whether a stage is truly complete.
---

# Postflight

## Purpose

`postflight` is the closing gate paired with `preflight`.

`preflight` asks what precedents, shortcuts, routes, and avoidable work should shape the start.

`postflight` asks whether the result is accepted, recoverable, maintainable, and transferable.

This Skill handles evidence-led acceptance and the operational surface after work is produced. Research, synthesis, design, and production remain outside its boundary.

## Reference Ideas

- A shared Definition of Done prevents partial work from being presented as complete.
- A launch checklist stays short, concrete, executable, and open to pruning.
- Significant incidents preserve impact, cause, actions, and learning.
- Long-running work needs observable indicators and explicit state.
- The next cycle should be a small evidence-led experiment.

## Principles

- Accept the result before expanding it.
- Mark anything untested, unopened, or unread as unverified.
- Preserve rollback or quarantine paths for files, caches, configuration, deployment, and authority changes.
- Make only reusable knowledge durable.
- Leave one smallest next action when a further cycle is justified.

## Classify the Deliverable

| Type | Main checks | Typical evidence |
|---|---|---|
| Code or automation | Acceptance, tests, regression, rollback | Diff, tests, command output, logs |
| Document or report | Structure, sources, gaps, handoff | File, outline, citations, unresolved items |
| Collaboration platform | Link, authority, owner, follow-up | Readback, task state, permission result |
| Skill or plugin | Triggers, installation, authority, usage path | `SKILL.md`, installed state, smoke test |
| Local cleanup or configuration | Read-only evidence, reversibility, impact | Dry run, scan, backup, quarantine |
| Deployment or recurring operation | Monitoring, alerts, rollback, cadence, owner | URL, health check, runbook, schedule |
| Design delivery | Source, visual acceptance, implementation fit | Design source, screenshot, comparison, review |

## Routing

| Closing concern | Pair with |
|---|---|
| Stale project state, memory, or handoff | Project-state and handoff alignment |
| Correctness or regression risk | Tests, build, and code review |
| Excessive complexity | Simplification review |
| Ambiguous acceptance criteria | Requirements interrogation |
| Visual or interaction quality | Design review |
| Collaboration-platform delivery | The platform’s readback and permission checks |
| Skill or plugin change | Skill validation and installed-state verification |
| Local cleanup | Read-only scan and dry run |
| Deployment or recurring operation | Runbook and automation capability |

## Workflow

1. **Restate the promise:** describe the original deliverable in one sentence.
2. **Set acceptance criteria:** use the user’s criteria or add the smallest fair standard.
3. **Match evidence:** list verified items, unverified items, and why evidence is unavailable.
4. **Assign status:** use only `accepted`, `accepted with caveats`, `not accepted`, or `blocked`.
5. **Check operations:** for reusable or long-running work, inspect owner, entry point, rollback, monitoring, and review cadence.
6. **Make selected knowledge durable:** update the relevant document, task, runbook, Skill source, or handoff only when it will affect later action.
7. **Leave one next step:** include cadence and trigger when work is recurring.

## Status Definitions

| Status | Condition |
|---|---|
| Accepted | Core criteria are met, evidence is present, and no required risk remains |
| Accepted with caveats | Deliverable is usable with explicit unverified items, environmental limits, or low-risk follow-up |
| Not accepted | A core criterion fails, so a completion claim would mislead |
| Blocked | Missing authority, information, external state, or user decision prevents verification |

## Durability Test

Preserve:

- rules, paths, commands, triggers, and authority boundaries that change future action;
- workflows or tool combinations proven useful;
- owners, dates, cadence, and risks that require follow-up;
- terminology, preferences, or project facts explicitly corrected by the user.

Leave out:

- one-time activity logs;
- facts already clear from code or filenames;
- unverified guesses;
- ordinary history available through version control.

## Output

```markdown
**Postflight Status**
Accepted / accepted with caveats / not accepted / blocked.

**Acceptance Evidence**
- Criterion: result / evidence.

**Unverified Items and Risks**
- Item, remaining risk, rollback, or manual confirmation.

**Durability**
- Recorded / linked / scheduled / no durable update needed.

**Next Cycle**
- One smallest action, with owner, cadence, or trigger when needed.
```

Expand only when the user asks for a full closeout report.

## Guardrails

- Claim only verification that actually occurred.
- Keep closeout within the original scope.
- Keep history logs out of long-term instruction files.
- Apply approval gates to installations, builds, migrations, deployments, runtime downloads, and large network fetches.
- Delete files, caches, or configuration only with clear authority and exact targets.
- Confirm target, identity, authority, and readback before collaboration-platform writes.
- Use absolute dates.
