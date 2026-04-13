# Contributing

## Principles

- Keep skills small and reusable.
- Prefer adapting with modules over bloating the core.
- Do not move project-local operating rules into generic skills.
- Domain-specific knowledge belongs in `domain-packs/`, not in generic domains.

## When to edit the core

Edit `Core Moves` only when:
- the invariant logic is wrong
- repeated use shows a structural gap
- the skill becomes simpler and more durable after the change

## When to add a module

Add an `Optional Module` when:
- a contextual need repeats often
- the logic is real but not universal
- it would otherwise bloat the core

## When to add sidecars

Add templates, checklists, examples, or references only when they:
- reduce complexity in `SKILL.md`
- are reusable
- are likely to evolve on their own

Do not create empty sidecar directories.

## Before opening a PR

Run:

```bash
python3 scripts/validate_skills.py
python3 scripts/report_projection_status.py
python3 scripts/project_to_codex.py --all --dry-run
```

If you changed projection metadata, also run:

```bash
python3 scripts/project_to_codex.py --check
```

## When to add an example

Add or update an example when:
- a new skill is hard to understand from the contract alone
- a skill combination becomes a repeated usage pattern
- a domain pack needs a clear boundary example
