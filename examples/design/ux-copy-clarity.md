# Example — UX Copy Clarity Review

## Situation

A project has a dashboard state labeled `critical dispatch` and users keep misreading it as an action instead of a system status.

## Skill combination

- `ux-writing`
- `heuristic-audit`

## Why this combination

- `ux-writing` improves wording, terminology, and explanation
- `heuristic-audit` checks whether the wording failure also exposes a deeper usability problem

## Minimal flow

### 1. Use `ux-writing`

Classify the problem:
- terminology ambiguity
- explanation gap
- action vs state confusion

Possible rewrite:
- replace `critical dispatch` with `critical alert dispatch status`
- add short supporting text clarifying whether dispatch is pending, active, or failed

### 2. Use `heuristic-audit`

Check whether users can:
- identify the current system state
- understand the consequence of that state
- decide the next action without guessing

## Expected improvement

The state becomes easier to scan, operational meaning becomes clearer, and the UI stops pretending that terminology alone can solve a structural clarity problem.
