---
name: scale
description: Trace one problem outward, inward, and sideways through goals, relations, causes, constraints, feedback, and action. Use after preflight and before solution design to choose a workable boundary, preserve cross-cutting relations, decide how deeply to decompose, determine whether coordination is justified, and route the next specialist capability. Trigger on scale, scope, macro-to-micro reasoning, decomposition, management depth, task allocation, cross-functional work, system boundaries, or questions about how large a problem really is.
---

# Scale

`scale` is a verb for moving through relations. It keeps one concern stable while changing the viewing distance until a workable boundary appears.

Use it after `preflight` has found relevant precedents and before detailed solution design. Follow relations, causes, constraints, and feedback until the boundary preserves what matters and still supports action and acceptance.

This Skill chooses the working boundary and routes the next capability. Research, synthesis, product requirements, design, architecture, implementation, and `postflight` continue elsewhere.

## Principles

- Macro and micro describe viewing distance. Zooming changes foreground and background.
- One object can be a whole, part of another whole, and a participant in several overlapping systems.
- Real structures often form overlapping networks; lateral relations matter.
- A boundary is a temporary hypothesis serving the current decision.
- Stop after obtaining the smallest sufficient evidence.

## Input

Prefer the `preflight` result, the user’s goal, and existing material. Establish:

- the concern: what must be understood, decided, or changed;
- the desired result: what change would count;
- known relations among goals, people, systems, data, tools, authority, risk, and external effects;
- evidence status: facts, inferences, and unknowns;
- explicit user boundaries.

State low-risk assumptions and continue. Ask up to three short questions only when missing information could change the goal, authority, critical boundary, or result.

## Scaling Loop

Keep the name of the concern stable.

1. **Anchor the concern:** state the one thing being understood, decided, or changed.
2. **Zoom outward:** follow real connections to larger goals, required inputs, decision rights, shared systems, downstream effects, feedback, and time horizons.
3. **Zoom inward:** follow the causal chain through judgments, actions, materials, interfaces, handoffs, failure points, and completion evidence.
4. **Trace sideways:** find overlapping workflows, shared resources, circular dependencies, common constraints, and costs shifted elsewhere by local optimization.
5. **Compare lenses:** identify invariants, transitions, couplings, and blind spots.
6. **Return to the concern:** decide whether the new information changes the current decision. Repeat only when it does.

At each pass, compare:

- **Invariants:** goals, tensions, constraints, feedback patterns, or completion definitions that remain stable.
- **Transitions:** new authority, risk, cadence, language, or causal mechanism.
- **Couplings:** elements that must be judged together and relations that can become inputs, outputs, constraints, or feedback.
- **Blind spots:** what the current lens hides and whether that affects action.

When the same pattern repeats at different distances, reuse one task contract. When the mechanism changes, mark the transition and route to the relevant specialist.

## Stop and Choose the Boundary

Zoom outward until additional relations no longer change the goal, authority, major risk, acceptance, or present action. Zoom inward until the next step can be executed and verified independently and further decomposition would add coordination cost.

The working boundary should:

- contain the critical causal chain and tightly coupled relations;
- represent external dependencies as inputs, constraints, interfaces, approvals, or feedback;
- remain within the user’s scope, authority, and risk limits;
- support assignment, execution, and acceptance.

Explain why the analysis stops there. Keep the boundary revisable.

## Coordination and Agents

- Add coordination roles or control gates only for shared decisions, blocking dependencies, authority, or independent acceptance.
- Divide work by outcome responsibility, decision rights, and handoff commitments.
- Treat Agents as temporary observation or execution capacity.
- Isolate exploration only when branches are independent, source material is much larger than the final conclusion, and the handoff contract is clear.
- An isolated exploration returns conclusions, evidence locations, confidence, and unresolved items.
- Concurrent writes require explicit file ownership. Otherwise keep exploration read-only or sequential.

## Routing

| Finding | Route |
|---|---|
| The concern, user evidence, or business result remains weak | Business analysis, user research, or requirements interrogation |
| Several precedents must become one new solution | `fusion` or collaborative ideation |
| Scope and acceptance need definition | Product requirements or planning |
| Interface behavior is a key mechanism | Interaction design and design review |
| The mechanism changes at a system, data, or interface boundary | Architecture or API design |
| Sensitive data, external action, or authority is critical | Threat modeling and security review |
| The boundary is stable and work can begin | Implementation planning and the relevant delivery capability |
| Work is ready to close | `postflight` |

Use the smallest combination that matches the current transition.

## Output

```markdown
**Current Concern**
- The one thing being understood, decided, or changed.

**Scaling Trace**
- Outward: goals, constraints, effects, and feedback.
- Inward: judgments, actions, interfaces, and completion evidence.
- Sideways: overlapping relations and shared constraints.

**Scale Invariants**
- Structures that remained stable.

**Transitions and Tight Couplings**
- Where the mechanism changed and what must stay together.

**Working Boundary**
- Included:
- Represented as an external dependency:
- Excluded for now:
- Why stop here:

**Smallest Executable Unit**
- Owner, input, action, output, evidence, and handoff.

**Routing**
- Next capability and the question it receives.

**Unknowns and Risks**
- Facts, inferences, unknowns, and validation signals.
```

## Guardrails

- Preserve one concern throughout the scaling loop.
- Follow actual relations and evidence.
- Keep cross-cutting relations visible.
- Respect the user’s declared scope and review gates.
- Avoid creating hierarchy where a simple contract or interface is enough.
- Stop when more detail no longer changes the decision.
