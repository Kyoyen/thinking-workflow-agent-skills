# Thinking Workflow Agent Skills

<p>
  <a href="README.md">中文</a> ·
  <a href="https://agentskills.io/">Agent Skills standard</a>
</p>

<p align="center">
  <img src="docs/assets/thinking-workflow-hero.svg" width="100%" alt="Thinking Workflow Agent Skills: a five-stage route across personal experience, organizational practice, and personal action">
</p>

I come from the humanities and social sciences, previously taught history, and now work at the frontier of FDE. I am glad to share these Skills with people exploring Vibe Coding, learning how AI workflows operate, or organizing complex work through a structuralist lens.

The collection turns my personal thinking habits into five executable Agent Skills: look outward, scale the problem, absorb and reorganize useful ideas, verify completion with evidence, and let reflection change the next action.

## A wide route

The method grows from personal experience, enters organizational and enterprise settings where relationships become more complex, and returns to personal judgment, choice, and action. The five-stage analysis provides a stable backbone. Each Skill also offers an independent entry point.

| 01 · Personal origin | 02 · Organizational practice | 03 · Personal return |
|---|---|---|
| Experience, questions, values, and working habits become the source of method. | Collaboration, process, authority, systems, and shared goals test the method across a wider network. | Evidence, counterexamples, and reflection return to personal practice and change the next choice. |

The route supports research, product, operations, writing, engineering, tool governance, organizational change, and everyday decisions.

## Choose an edition

The repository provides two complete editions. Each contains all five Skills, interface metadata, references, and supporting scripts. They share the same method, stage boundaries, and invocation names.

| Edition | Entry point | Best for |
|---|---|---|
| English | [`editions/en/skills/`](editions/en/skills/) | English instructions, templates, and script output |
| Chinese | [`editions/zh-CN/skills/`](editions/zh-CN/skills/) | Chinese instructions, templates, and script output |

Install one edition. Both editions intentionally use the same Skill names, so installing both creates duplicate-name discovery or overwrite conflicts.

## Five-stage analysis

```mermaid
flowchart LR
    A["Preflight<br/>Look outward"] --> B["Scale<br/>Trace relations"]
    B --> C["Fusion<br/>Form a new whole"]
    C --> D["Execute & verify"]
    D --> E["Postflight<br/>Accept & sustain"]
    E --> F["Retro Insights<br/>Reflect across cycles"]
    F -. "validated change" .-> A
```

| Skill | English | Chinese | Core question |
|---|---|---|---|
| `preflight` | [Open](editions/en/skills/preflight/) | [Open](editions/zh-CN/skills/preflight/) | What already exists, what is useful, and what should be discarded? |
| `scale` | [Open](editions/en/skills/scale/) | [Open](editions/zh-CN/skills/scale/) | How far outward, inward, and sideways must this problem be seen before action? |
| `fusion` | [Open](editions/en/skills/fusion/) | [Open](editions/zh-CN/skills/fusion/) | How can several useful directions become one coherent solution? |
| `postflight` | [Open](editions/en/skills/postflight/) | [Open](editions/zh-CN/skills/postflight/) | Is the result complete, recoverable, maintainable, and transferable? |
| `retro-insights` | [Open](editions/en/skills/retro-insights/) | [Open](editions/zh-CN/skills/retro-insights/) | Which repeated patterns deserve a place in the next cycle? |

## Philosophical foundations

<p align="center">
  <img src="docs/assets/philosophy-route-bar.svg" width="100%" alt="Positivism, structuralism, existentialism, and the route from personal experience through organizational practice back to personal action">
</p>

### Positivism

Observable facts, reviewable material, and practical results ground judgment. `preflight` examines real precedents, `postflight` requires completion evidence, and `retro-insights` looks for repetition across tasks. Every conclusion remains open to new evidence.

### Structuralism

Meaning emerges through relations, positions, differences, constraints, and feedback. `scale` moves outward, inward, and sideways around one concern. `fusion` reorganizes several sources within one goal structure. Boundaries serve the current decision and remain revisable.

### Existentialism

People act from concrete situations and take responsibility through choice. A Skill provides structures for observation and judgment; the actor still chooses and acts. The cycle returns to the individual: understand the situation, choose, take responsibility, and let experience shape the next action.

| Philosophical line | Workflow expression | Main carriers |
|---|---|---|
| Positivism | Evidence, results, and reviewability constrain judgment | `preflight`, `postflight`, `retro-insights` |
| Structuralism | Relations, boundaries, and whole structures explain the problem | `scale`, `fusion` |
| Existentialism | Situated choice, action, responsibility, and personal return | Execution, `postflight`, `retro-insights` |

## Why open source

This repository makes a personal way of thinking readable, usable, and discussable:

- Turn tacit judgment into working contracts an Agent can execute.
- Keep reasoning, boundaries, and completion evidence visible to collaborators.
- Explore how a viewpoint becomes triggers, steps, stop conditions, and acceptance structures.
- Observe how personal methods enter collaborative systems and return through organizational learning.
- Exchange practical methods with people working on internal transformation in established enterprises.

## Install

Clone the repository, then copy one edition:

```bash
git clone https://github.com/Kyoyen/thinking-workflow-agent-skills.git
mkdir -p ~/.agents/skills
cp -R thinking-workflow-agent-skills/editions/en/skills/* ~/.agents/skills/
```

For the Chinese edition, replace the final line with:

```bash
cp -R thinking-workflow-agent-skills/editions/zh-CN/skills/* ~/.agents/skills/
```

You may also copy one Skill directory, such as `editions/en/skills/preflight/`. Restart or refresh your Agent Skills client after installation.

## Typical uses

- Start an unfamiliar research or product question with relevant precedents.
- Untangle a problem that keeps expanding or fragmenting.
- Turn several useful options into one original route.
- Close code, research, documents, automation, or projects with evidence.
- Review repeated human–Agent work through results, friction, and correction.
- Apply the full cycle from an idea to a sustainable working method.

See the Chinese README for detailed scenarios and usage boundaries.

## Contributing and contact

Sanitized experience reports, issues, discussions, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [PRIVACY.md](PRIVACY.md) first.

License: [MIT](LICENSE)

Email: [lumon.merrifort@foxmail.com](mailto:lumon.merrifort@foxmail.com)
