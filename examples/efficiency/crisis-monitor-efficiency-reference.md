# Crisis Monitor Efficiency Reference

## Context

This is a lightweight reference example for using the first Efficiency Layer trio against a real product lane.

Reference lane:

- Crisis Monitor
- routing / approval / follow-up explainability
- one bounded round, not a broad rollout

## Problem shape

The lane is already valid, but it is vulnerable to three common efficiency problems:

- the next round tries to include too much at once
- the team keeps going past a healthy checkpoint
- restart context becomes heavier than necessary

## Trio usage

### 1. `task-chunking`

Current round:

- keep the slice to one auditable improvement in the lane
- avoid bundling adjacent follow-up ideas into the same round
- leave later improvements outside the current execution boundary

Expected effect:

- one bounded change
- one explicit next slice
- less lane creep

### 2. `checkpoint-review`

Checkpoint question:

- is the next step still part of the same smallest useful slice?

In this reference case, if the answer becomes no, the round should stop instead of expanding.

Expected effect:

- explicit continue / stop / handoff decision
- less accidental session growth

### 3. `handoff-summary`

Round closure should record only:

- what changed
- what was verified
- what remains open
- what the next round should do

Expected effect:

- easier restart
- less need to reload the whole previous session

## Boundary check

What stays with AletheIA:

- macro framing
- proof expectation
- gate or escalation logic
- cross-round continuity posture

What stays local to Crisis Monitor:

- product semantics
- domain-specific approval meaning
- ownership by thread
- rollout and audit policy

What the Efficiency Layer adds:

- bounded slice discipline
- useful pause decisions
- lighter resumable handoff notes

## Likely result mode

For an early pilot, a healthy outcome is often:

- `reinforced`
- or `no-change`

That is acceptable.
The point is to prove that the trio helps operationally, not to force immediate changes to the library.
