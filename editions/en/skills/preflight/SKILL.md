---
name: preflight
description: Broad pre-task preflight and routing gateway to prevent self-indulgent, closed-door building. Use before planning or implementation when the task may benefit from checking predecessors, comparable products, open-source libraries, platform features, standards, concepts, business analogies, academic work, competitor examples, or prior local precedents. Triggers include preflight, prior art, existing solutions, similar tools, market landscape, what already exists, avoid reinventing the wheel, and vague feature or strategy ideas that need broad grounding before action.
---

# Preflight

## Philosophy

Preflight exists to prevent self-indulgent, closed-door building.

Do not start from the assumption that the user's idea is novel, isolated, or best solved from scratch. First look outward and backward: what have others already tried, what worked, what failed, what language already exists, and what should be borrowed or avoided.

The core method is simple:

1. Stand on predecessors' shoulders.
2. Extract what is useful.
3. Discard what is noisy, stale, misleading, or mismatched.
4. Return to the user's actual task with a sharper next step.

This is a first-pass gateway, not a final research artifact. It does broad coarse processing, then either gives a compact recommendation or routes to a heavier specialist skill.

Preflight is also the top-level router for "do not reinvent the wheel" work. It should decide whether the next useful move is research, simplification, interrogation, implementation, review, or deferral.

Irreplaceable boundary: preflight only finds precedents, judges routes, and sharpens the next move before work starts; it does not fuse several options into a new solution, produce design rules, or close out finished work.

## Use When

- A feature, product, plugin, workflow, agent capability, content idea, research direction, or business question may already have known precedents.
- The user asks for competitors, alternatives, prior art, existing solutions, open-source options, platform-native features, concepts, analogies, or benchmarks.
- A task is vague enough that terminology and precedents would change the plan.
- Implementation could take meaningful time and a short check could avoid duplicate work.
- The user explicitly wants to avoid closed-door thinking or reinventing the wheel.

## Do Not Use When

- The task is a tiny local edit where broader landscape would only slow execution.
- The user already chose the exact tool/technology and only needs official usage details. Route to a best-practice research flow.
- The user asks for a deep, audited deliverable from the start. Route to the relevant specialist.
- The answer is fully repo-local. Inspect the repo directly instead.

## Default Timebox

Default to a compact scan:

- 10-20 minutes.
- 5-8 high-signal precedents, options, or concepts.
- 2-4 primary or high-quality sources per major category when web research matters.
- One local-context pass if the current repo, workspace, or prior decisions matter.

Stop as soon as further research would not change the recommendation.

## Routing Pipeline

Preflight should actively route to a more suitable capability when the problem has a clearer domain shape. Do not assume that another named Skill is installed.

| If the task is really about... | Route or hand off to... | Why |
|---|---|---|
| Several known options must become one original solution | `fusion` | Needs lawful synthesis, tradeoffs, and a coherent new route |
| The same problem must be traced across goals, actors, systems, and actions | `scale` | Needs a workable boundary before solution design |
| Academic literature or a systematic review | A scholarly research workflow | Needs reproducible search, methods, citations, and bias handling |
| Competitor or market analysis | A competitor-research workflow | Needs structured evidence grounded in the actual options |
| Current technical best practice for a chosen stack | Official documentation and a version-aware technical workflow | Needs current primary sources |
| Product requirements or implementation | The relevant product, design, architecture, or engineering workflow | The direction is clear enough to leave preflight |
| A non-trivial plan or handoff is still ambiguous | A requirements interrogation or review workflow | Goals, acceptance, boundaries, alternatives, and assumptions need pressure-testing |

If routing is appropriate, say so explicitly and either hand off or use this preflight only to define the handoff question.

## Simplest Viable Path

When the task may lead to coding or automation, run this ladder before recommending custom work:

1. Does this need to exist at all?
2. Does the current codebase, workspace, or prior local artifact already solve it?
3. Does the standard library, platform, host app, or OS already solve it?
4. Does an already-installed dependency or configured tool solve it?
5. Can the need be wrapped, configured, or composed instead of newly built?
6. Only then recommend the minimum custom implementation.

Preflight applies this ladder at decision time, not as a substitute for implementation review. Do not let the ladder replace evidence gathering when public or local precedent could change the decision.

## Workflow

1. Restate the actual capability, decision, or question in one sentence.
2. Classify the landscape:
   - product or competitor precedent
   - open-source library or package
   - platform/native feature
   - academic or technical concept
   - business benchmark or go-to-market analogy
   - social/content/community pattern
   - workflow/process pattern
   - internal/local precedent
3. Decide whether this generic preflight is enough or a specialist skill should take over.
4. Search local context first when the current repo, docs, workspace, or prior decisions matter.
5. Search the web when public, current, or ecosystem information could change the decision.
6. Prefer primary evidence: official docs, source repos, release notes, standards, papers, product pages, marketplace listings, pricing pages, and first-party case studies.
7. Run the simplest viable path ladder for implementation-shaped work.
8. Compare options on fit, maturity, integration cost, expected UX, constraints, risk, what to borrow, and what not to build.
9. If the next artifact is a plan, specification, ticket, or handoff, pressure-test unresolved goals, acceptance, boundaries, alternatives, and assumptions before treating it as executable.
10. End with what this changes and the smallest useful next step.

## Source Quality

- Prefer primary sources over SEO summaries.
- Use third-party commentary only as supplemental signal.
- State date/version context for fast-moving products, APIs, plugins, or libraries.
- Label inference when evidence is indirect.
- Do not present stale memory or old notes as current market reality without verification.
- If live web is unavailable, say the result is local-memory-only and may be stale.

## Decision Language

- Build: no adequate option exists, or differentiation requires owning the capability.
- Adapt: a known pattern or open-source project is close but needs tailoring.
- Integrate: a mature external option solves the need better than custom work.
- Wrap: native/platform behavior exists, but the user needs better workflow, UI, automation, or integration.
- Route: a specialist skill should handle the next step.
- Defer: unclear value, weak evidence, or high risk relative to the task.
- Shrink: the idea is valid, but the smallest viable path is reuse, stdlib/native/platform behavior, configuration, or a thinner implementation.

## Output

Use this structure unless the user asks otherwise:

```markdown
**Preflight Question**
<one sentence: what are we checking before acting?>

**Landscape**
<what already exists, and what category this problem belongs to>

**Relevant Precedents**
- Name: what it is, what to borrow, what to avoid, evidence quality.

**Take The Essence**
- Patterns, APIs, UX choices, business moves, language, or constraints worth reusing.

**Discard The Dross**
- Traps, stale patterns, overbuilt parts, misleading analogies, weak evidence, or non-goals.

**Routing**
- Continue here / route to <skill> / use <skill> after this preflight.

**Simplest Viable Path**
- Keep / skip / reuse / stdlib / native / installed dependency / wrap / minimum custom build.

**Recommendation**
Build / adapt / integrate / wrap / route / defer, with the next concrete step.
```

## Guardrails

- Do not praise novelty before checking precedent.
- Do not produce a generic list of famous tools; connect every item to the user's actual decision.
- Do not let research become a substitute for execution.
- Do not keep researching after the recommendation would not change.
- Do not send ambiguous plans straight into implementation when unresolved goals, acceptance, boundaries, alternatives, or assumptions would make an agent guess.
- Do not send coding work straight into custom implementation; use the simplest viable path and an appropriate implementation review.
- If a heavy install, build, migration, or scrape is needed, apply the long-operation approval gate before executing.

For deeper comparison templates and plugin checklists, read `references/preflight-brief.md`.
