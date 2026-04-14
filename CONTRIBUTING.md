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
python3 scripts/validate_evolution.py
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


## Evolution layer changes

Use the evolution layer when a real usage signal suggests the library itself may need review.

Prefer this order before proposing a new skill:
1. `no-change`
2. trigger adjustment
3. example, checklist, or template refinement
4. new module candidate
5. only then a new-skill candidate

Do not treat every local success or failure as a library edit request. `reinforced` and `no-change` are healthy outcomes.
