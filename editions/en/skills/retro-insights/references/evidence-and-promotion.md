# Evidence and Promotion Rules

## Evidence Levels

| Level | Evidence | Supported conclusion |
|---|---|---|
| A | Real files, version control, tests, logs, command results, working entry points, explicit user corrections | Facts and high-confidence actions |
| B | Consistent behavior or outcomes across independent user root sessions | Trends and repeated patterns |
| C | Memory, activity history, screenshots, interface state, summaries | Routing and hypotheses to verify |
| D | One inference, vague impression, adjacent time window | Validation questions only |

Source count does not equal evidence strength. Ten summaries of one event still describe one event.

## Pattern Card

Record:

```text
Pattern:
Factual evidence:
Distinct user root sessions:
Domains: code / product / collaboration and documents / design / environment / automation / delivery / other
Impact: time / quality / risk / trust / cost
Counterexamples:
Root-cause confidence: low / medium / high
State: observation / watch item / promotion candidate / implemented / validated / withdrawn
```

Repeated details inside one session count as one independent session. Sub-agents, guardians, automation, and technical probes do not replace user root-session evidence.

## Promotion Ladder

### Observation

- One occurrence or only level C/D evidence.
- Keep it in the report.

### Watch Item

- Appears in two distinct user root sessions.
- Seek counterexamples, impact, and causal evidence during the next cycle.

### Promotion Candidate

Any one condition:

- at least three distinct user root sessions across at least two domains;
- the same high-risk problem occurs twice with level A evidence;
- the user explicitly requests durable treatment;
- one event causes major irreversible loss and a low-cost, testable guardrail is clear.

### Implemented

- The user approves the destination and change.
- Back up first, apply the smallest patch, and read back the result.

### Validated

- The next cycle shows fewer similar errors or clear positive evidence.
- Withdraw, narrow, or move an ineffective rule to project scope.

## Choose the Destination

| Insight | Preferred destination |
|---|---|
| Stable collaboration boundary across projects | User-level Agent rules |
| Project fact, term, command, or business boundary | Project rules or project-state document |
| Repeated multi-step method | New Skill or a small update to an existing Skill |
| Machine-detectable risky action or precondition | Hook, validator, or script |
| Recurring check and report | Automation |
| Recovery, owner, monitoring, or rollback | Runbook or postflight document |
| Unstable or single occurrence | Retro-insights report only |

Keep project details out of global rules. Put executable checks in code. Create a new Skill only when a repeated method warrants one.

## Cycle Comparison

Review up to three actions from the previous cycle:

| State | Meaning |
|---|---|
| Effective | Level A/B evidence shows fewer problems or better outcomes |
| Ineffective | The action ran and outcomes did not improve |
| Not executed | The action did not occur, so its method remains unevaluated |
| Insufficient evidence | The result is unobservable or the window is too short |

Remove low-value recommendations left unexecuted for two consecutive cycles.
