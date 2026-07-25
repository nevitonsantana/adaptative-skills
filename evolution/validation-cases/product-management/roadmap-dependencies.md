---
id: vc-product-management-roadmap-dependencies-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "Shape a sequence for three accepted initiatives when one depends on an API migration and another competes for the same specialist team."
  context: "Confidence, dependency timing, and capacity are partially known; the requester asks for fixed dates."
expected_behavior:
  must_do:
    - "Separate accepted product choices from sequencing and delivery uncertainty."
    - "Map dependencies, capacity constraints, confidence, and conditions for reordering."
    - "Hand off a bounded sequence question to feature-planning without promising fixed dates."
  must_not_do:
    - "Treat a roadmap sequence as a guaranteed schedule."
    - "Hide dependencies inside feature descriptions."
    - "Commit dates without capacity and dependency evidence."
acceptance_criteria:
  - "The response includes dependencies, assumptions, confidence, and review conditions."
  - "The response distinguishes roadmap narrative from delivery commitment."
  - "The response names the next owner and verification needed for sequencing."
failure_signals:
  - "The output gives fixed dates from incomplete capacity information."
  - "The output omits the API migration or shared-team conflict."
---

# Roadmap dependency case

## Must do

- Show how dependencies and capacity alter sequence confidence.
- State which conditions would trigger a reorder.
- Hand off only after the decision and sequence scope are bounded.

## Must not do

- Do not turn uncertain sequencing into a promise.
- Do not substitute a calendar for a decision model.

## Observable evaluation

Pass when the sequence has explicit dependency logic, confidence, and review triggers. Fail when it presents an unqualified delivery calendar.

## Minimum evidence and human decisions

Minimum evidence is dependency status, capacity constraint, initiative outcomes, and planning horizon. Humans own the accepted trade-offs and any commitment made to stakeholders.
