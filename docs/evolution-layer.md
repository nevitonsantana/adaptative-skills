# Evolution Layer

## Why this layer exists

Adaptative Skills already treats skills as reusable, structured, and portable.
The next step is to let the library improve through real usage without turning it into an unrestricted self-rewriting system.

The evolution layer exists to make that improvement:

- visible
- reviewable
- domain-aligned
- safe enough to govern by pull request

## Core thesis

Skills should improve through use, but the improvement loop must stay governed.

This repository therefore uses an explicit loop:

1. **Observe** — capture what happened in a real task or pilot.
2. **Read** — review the current skill, modules, sidecars, and fit.
3. **Execute** — assess how the skill was actually used.
4. **Reflect** — separate local friction from reusable library friction.
5. **Attribute** — decide whether the issue belongs to the skill, the trigger, the module, the surrounding operating system, or nowhere.
6. **Propose** — write an auditable proposal when change is justified.
7. **Govern** — decide whether the proposal is accepted, rejected, deferred, or downgraded to no-change.
8. **Write** — update the library only after review.

## What this is not

This is not a self-rewrite runtime.
In v1.1:

- skills do **not** edit themselves automatically
- the canon in `skills/` and `domain-packs/` is still changed by normal pull requests
- observations and proposals are repository-level artifacts, not hidden memory

The inspiration from systems such as Memento-Skills is the governed learning loop, not automatic mutation of the public library.

## Success-aware outcomes

Not every observation should change the library.
Valid outcomes include:

- `reinforced` — the skill worked and the case strengthens confidence in the current design
- `no-change` — the issue was local, macro-layer, or not a library problem
- `proposal-created` — a concrete improvement proposal is justified
- `new-module-candidate` — repeated context suggests a module may be missing
- `new-skill-candidate` — repeated evidence suggests the current skill boundary is too small
- `rejected` — a proposed change should not enter the library

## Repo-level design

The evolution layer is intentionally centralised.

It lives in:

- `evolution/registry.yaml`
- `evolution/observations/`
- `evolution/proposals/`
- `evolution/templates/`
- `evolution/reviews/`

This keeps the library coherent and avoids adding `telemetry.md` or `improvement-log.md` to every skill before the process is proven.

## Protected versus proposal-safe surfaces

The v1.1 layer protects the most conceptually sensitive surfaces:

- skill identity and thesis
- `When to Use` / `When NOT to Use`
- `Core Moves`
- category and domain boundaries
- merge or split decisions for skills

The layer is more open to proposals for:

- `Activation Triggers`
- `Optional Modules`
- `Verification`
- `Anti-patterns`
- `templates/`, `checklists/`, `examples/`, `references/`, and `changelog.md`

## Initial pilot

The first evolution pilot is intentionally small and domain-aligned.
It focuses on:

- `workflow`
- `feature-planning`
- `testing`
- `debugging`
- `ux-writing`

It also uses the Crisis Monitor + AletheIA case as seed evidence, especially where the library needs to distinguish:

- a good local fix
- a reinforced skill
- a true proposal-worthy library gap

## Relation to AletheIA

AletheIA may eventually help coordinate this layer by surfacing repeated breakdowns, handoff friction, and continuity signals.
But Adaptative Skills must remain useful without AletheIA.
The evolution layer therefore stays repository-native and review-native in v1.1.
