# Thinking Workflow Agent Skills — English Edition

This directory contains the complete English edition of all five Skills. Natural-language instructions, templates, interface metadata, references, and script output are in English. Invocation names, command arguments, code keywords, and stable data fields remain consistent across editions.

## Included Skills

- [`preflight`](skills/preflight/) — check precedents and the simplest viable path before acting.
- [`scale`](skills/scale/) — trace relations and choose a workable boundary.
- [`fusion`](skills/fusion/) — digest several directions into one coherent solution.
- [`postflight`](skills/postflight/) — close work through evidence, recovery, maintenance, and handoff.
- [`retro-insights`](skills/retro-insights/) — turn cross-cycle evidence into a testable improvement.

## Install

Run from the repository root:

```bash
mkdir -p ~/.agents/skills
cp -R editions/en/skills/* ~/.agents/skills/
```

You may copy a single Skill directory instead. Do not install this edition alongside the Chinese edition because both use the same invocation names.

Return to the [English repository homepage](../../README.en.md).
