---
name: work-continuity-efficiency
description: Make oversized or interrupted work smaller, resumable, reviewable, and clear to hand off through selective use of continuity building blocks.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: efficiency
---

# Overview

Use this optional family entrypoint when work is too large, interrupted, context-heavy, or
crosses operators and the right continuity building block is not yet clear. It selects the
smallest sufficient path through `task-chunking`, `checkpoint-review`, `handoff-summary`, and
`communication`.

Use a building block directly when the need is already specific. This family does not manage
tasks, persist state, schedule agents, or replace project governance.

# When to Use

- A large request needs a safe first slice and explicit stop condition.
- Work may be resumed by another session, person, or agent.
- The task changed shape and needs a continue, stop, or handoff decision.
- A status, decision, failure, or handoff needs to become legible without carrying full context.

# When NOT to Use

- The task is already a small, obvious execution pass.
- The work needs product, architecture, policy, or macro-gate judgment instead.
- The requester expects task tracking, scheduling, automatic persistence, or external actions.
- A direct building block already matches the question.

# Core Moves

1. **Frame the continuity need.** Identify the work state, current round, intended outcome,
   next owner, unresolved uncertainty, and minimum proof.
2. **Classify the dominant need.** Choose chunking, checkpointing, handoff, or communication;
   do not treat all continuity concerns as the same problem.
3. **Select the smallest path.** Activate one primary building block and add another only when
   its output is necessary for safe continuation.
4. **Produce a bounded artifact.** State what changed, what is proved, what remains open, and
   the explicit stop, continue, or handoff condition.
5. **Verify resumability.** Confirm that another operator can continue without reconstructing
   the original context and without confusing assumptions with proof.

# Building Blocks

- `task-chunking` — smallest useful slice, dependencies, boundaries, and stop condition.
- `checkpoint-review` — continue, stop, or handoff decision after a meaningful round.
- `handoff-summary` — compact verified context for another round or owner.
- `communication` — clear status, decision, failure, or handoff explanation.

Use only the blocks justified by the continuity need. Family membership does not load all four
contracts by default.

# Optional Modules

- **Continuity need framing** — Bound the current round, intended outcome, next owner, and
  minimum proof before selecting a path.
- **Dominant need classification** — Distinguish slicing, checkpointing, handoff, and
  communication needs.
- **Selective composition** — Add a supporting building block only when its output is needed
  for safe continuation.
- **Resumability check** — Test whether another operator can act without reconstructing the
  original context.

# Activation Triggers

- Activate `task-chunking` when the task is oversized, fuzzy, or entangled.
- Activate `checkpoint-review` when the task changed shape or continuation is uncertain.
- Activate `handoff-summary` when another round, owner, or agent must resume the work.
- Activate `communication` when the result must be made legible as status, decision, failure,
  or handoff information.

# Expected Output

```yaml
work_continuity_review:
  work_state: <current state>
  intended_outcome: <outcome>
  dominant_need: chunk | checkpoint | handoff | communication
  primary_building_block: <skill>
  supporting_building_blocks: [<only necessary skills>]
  proved: [<validated facts or artifacts>]
  open_items: [<unresolved items>]
  decision: continue | stop | handoff
  stop_condition: <condition>
  next_step: <bounded next action>
  handoff_owner: <owner or unknown>
  risks_or_blockers: [<visible risks>]
```

# Verification

- The current state and dominant continuity need are explicit.
- One primary building block is selected and justified.
- Supporting blocks are necessary rather than merely adjacent.
- Proven work is separated from assumptions and open items.
- Stop, continue, or handoff is explicit.
- The artifact is smaller than the context it replaces and sufficient to resume safely.
- No task tracking, scheduling, persistence, or external action is claimed.

# Handoff Signals

- Product or feature scope is unresolved → `intent-clarification` or `feature-planning`.
- A macro gate, authorization, or ownership decision is required → AletheIA or consumer governance.
- The next work needs a different specialty → hand off with `handoff-summary`.
- The work is clear but only needs a direct slice → use the matching building block directly.

# Pairs Well With

- `workflow`
- `feature-planning`
- `checkpoint-review`
- `handoff-summary`
- `communication`

# Anti-patterns

- Loading all continuity skills for every task.
- Calling a large task a slice without reducing it.
- Continuing only because the round has momentum.
- Writing a handoff that hides missing proof or unresolved ownership.
- Turning continuity guidance into a project-management runtime.
