# Example — New Feature Slice

## Situation

A project wants to add a small approval summary card before a user publishes a change.
The work is not huge, but it touches behavior and needs proof.

## Skill combination

- `workflow`
- `feature-planning`
- `testing`

## Why this combination

- `workflow` sets the immediate boundary
- `feature-planning` turns the request into a smallest useful slice
- `testing` makes proof explicit before implementation expands

## Minimal flow

### 1. Use `workflow`

State:
- goal
- in-scope and out-of-scope
- minimum proof

Example:
- goal: add a readable approval summary before publish
- in scope: summary card, data mapping, visible state
- out of scope: notification redesign, analytics overhaul
- proof: successful smoke plus one regression check on current publish flow

### 2. Use `feature-planning`

Define:
- smallest useful slice
- dependencies
- first acceptance evidence

Example first slice:
- render the summary card with existing approval data
- show fallback state when data is incomplete
- keep publish behavior unchanged

### 3. Use `testing`

Choose proportionate proof:
- one implementation-level check for mapping/render logic
- one smoke of the publish flow
- one regression-oriented check for missing approval data

## Why it works

The task stays small, the first slice stays defensible, and the proof is visible before the feature grows into adjacent concerns.
