---
id: vc-work-continuity-family-selection-001
skill_id: work-continuity-efficiency
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task:
    request: "This initiative is too big for this session. Break it down and leave it ready for another agent tomorrow."
    current_state: "Several assumptions are unresolved; no validated slice exists."
expected_behavior:
  must_do:
    - Start with the work-continuity-efficiency family because the request needs both chunking and continuation.
    - Select task-chunking as the primary building block.
    - Add handoff-summary only because another agent must resume the work.
    - Define the smallest useful slice, excluded work, dependencies, proof, and stop condition.
    - Preserve unresolved assumptions and ownership boundaries.
  must_not_do:
    - Load checkpoint-review or communication without a reason tied to the current output.
    - Pretend that the initiative is ready for execution.
    - Create tasks, schedule the next agent, or persist state.
    - Hide unresolved assumptions inside a polished summary.
acceptance_criteria:
  - The result gives another agent enough verified context to resume without reconstructing the full initiative.
  - The family explains why the selected path is sufficient for this round.
failure_signals:
  - The output is a generic project plan instead of a bounded slice and handoff.
  - Stop conditions, proof, or unresolved assumptions are missing.
notes: Synthetic family-entry validation case for selective continuity composition.
---

# Validation Case

## Scenario

An initiative is too large for the current session. The requester needs a smaller first slice
and a safe handoff to another agent tomorrow.

## Review focus

Confirm that the family chooses `task-chunking` first, adds `handoff-summary` only because the
work crosses sessions, and leaves scheduling, persistence, and unresolved human decisions
outside the skill's authority.
