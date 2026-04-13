# Worked Example — Feature Slice with AletheIA

## Scenario

A consumer project wants to add a small approval summary before a publish action.
The task is meaningful enough to need framing and proof, but still small enough for a first AletheIA test.

## Why this is a good first test

- small blast radius
- clear proof shape
- easy to separate framing from execution guidance
- easy to tell whether the macro/micro split stayed legible

## Macro layer: what AletheIA does

AletheIA should handle:
- **framing** — clarify the goal, dominant lane, and immediate boundary
- **proof expectation** — require a smoke plus one regression-oriented check
- **gate/review** — decide whether the task is still a local feature slice or needs broader review
- **handoff** — detect whether product/design review becomes necessary

Example framing:
- goal: add a readable approval summary before publish
- dominant lane: feature delivery
- immediate boundary: summary card and data mapping only
- out of scope: notification redesign, analytics expansion, approval rules redesign
- minimum proof: render logic check plus publish-flow smoke

## Micro layer: what the skills do

### `workflow`

Provides:
- one-sentence goal
- in-scope vs out-of-scope boundary
- explicit minimum proof

### `feature-planning`

Provides:
- smallest useful slice
- first acceptance evidence
- visibility on hidden scope

Example smallest slice:
- show the summary card using existing approval data
- handle incomplete data with a fallback state
- do not change publish semantics yet

### `testing`

Provides:
- proportionate proof for the slice
- at least one regression-oriented lens

Example proof:
- implementation-level check for summary rendering
- publish-flow smoke test
- fallback-state regression check

## What stayed local to the consumer project

The consumer project should still own:
- branch/review conventions
- domain vocabulary specific to its product
- release or security gates
- any approval workflow rules beyond the UI slice

## Why this split works

- AletheIA prevents the task from sprawling semantically.
- The skills prevent execution from becoming improvised.
- Proof stays visible because AletheIA asks for it and `testing` shapes it.
- The consumer project keeps its own local operating rules.

## Failure mode to watch for

This test is going wrong if:
- AletheIA starts prescribing the detailed slice logic that belongs in `feature-planning`
- the skills start defining review gates or local release rules
- the task grows past the first slice without revisiting framing
