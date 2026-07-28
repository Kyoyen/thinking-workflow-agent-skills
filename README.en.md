# Thinking Workflow Agent Skills

[中文](README.md) · [Agent Skills standard](https://agentskills.io/)

Five Agent Skills that turn a personal way of thinking into an executable workflow:

1. `preflight` — look outward for precedents before building.
2. `scale` — move outward, inward, and sideways until a workable boundary appears.
3. `fusion` — absorb useful ideas and form an original, coherent solution.
4. `postflight` — verify completion, recovery, maintenance, and handoff.
5. `retro-insights` — turn repeated experience into the next testable improvement.

These skills began as tools for my own work across research, product, operations, writing, engineering, tool governance, and organizational change. They are not dedicated to one industry. Use them independently or as a cycle.

```mermaid
flowchart LR
    A["Preflight"] --> B["Scale"]
    B --> C["Fusion"]
    C --> D["Execute & verify"]
    D --> E["Postflight"]
    E --> F["Retro Insights"]
    F -. "validated change" .-> A
```

## Why this repository exists

I am sharing a transferable way of thinking, not the internal answers of any company or project.

- Make tacit personal judgment legible and repeatable for an Agent.
- Make the reasoning behind a decision easier for collaborators to inspect.
- Explore how a viewpoint becomes boundaries, steps, stop conditions, and acceptance evidence instead of a long prompt.
- Exchange practical methods with people working on internal transformation in established enterprises.

Enterprise transformation is an important sharing direction for this repository, but it does not define the scope of the five skills.

The public edition has been sanitized. It contains no company, client, project, location, internal system, account, local path, production log, or identifiable business case. All scenarios are synthetic composites.

## Personal position

The outside world comes before internal imagination. Boundaries are temporary hypotheses for a decision. Innovation is not accumulation; it is coherent recombination after understanding and subtraction. Completion requires evidence, recovery, and handoff. Experience becomes learning only when it changes the next action.

For established enterprises specifically, I do not see them as obsolete objects waiting to be “fixed” by technology. They contain hard-won experience, relationships, and constraints, as well as genuine inertia and cost. Transformation should understand before it chooses, validate locally before it scales, and avoid worshipping either the past or new technology.

## Install

With a compatible Skills CLI:

```bash
npx skills add Kyoyen/thinking-workflow-agent-skills
```

Or install manually:

```bash
git clone https://github.com/Kyoyen/thinking-workflow-agent-skills.git
mkdir -p ~/.agents/skills
cp -R thinking-workflow-agent-skills/skills/* ~/.agents/skills/
```

Restart or refresh your Agent Skills client after installation.

## Typical uses

- Start an unfamiliar research or product question without reinventing the wheel.
- Untangle a problem that keeps expanding or fragmenting.
- Turn several useful options into one original route.
- Close code, research, documents, automation, or projects with evidence.
- Review repeated human–Agent work without mistaking activity metrics for value.
- Apply the full cycle from an idea to a sustainable working method.

See the Chinese README for the full philosophy, catalog, boundaries, and sanitized scenarios.

## Contributing and contact

Sanitized experience reports, issues, discussions, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [PRIVACY.md](PRIVACY.md) first.

License: [MIT](LICENSE)

Email: [lumon.merrifort@foxmail.com](mailto:lumon.merrifort@foxmail.com)
