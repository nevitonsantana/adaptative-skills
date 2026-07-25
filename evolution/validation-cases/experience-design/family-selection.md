---
id: vc-experience-design-family-selection-001
skill_id: experience-design
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task:
    request: "The onboarding experience feels confusing. What should we do?"
    artifact: unknown
    user_evidence: unavailable
expected_behavior:
  must_do:
    - Start with experience-design because the request is broad.
    - Ask or identify whether the dominant need is strategy, hypothesis pressure-testing, usability audit, or writing clarity.
    - Avoid treating a heuristic review as proof of user behavior.
    - Select one primary building block and state the evidence gap.
    - Preserve product, design, and implementation ownership.
  must_not_do:
    - Load all five design skills by default.
    - Invent user research or declare a final design.
    - Rewrite the interface before the design question is bounded.
acceptance_criteria:
  - The response returns a bounded intake or primary design path with a verification step.
  - Evidence gaps and human decisions remain visible.
failure_signals:
  - “Confusing” is treated as validated user research.
  - The response mixes strategy, audit, copy, and implementation without selection.
notes: Synthetic family-entry validation case for selective Experience Design composition.
---

# Validation Case

## Scenario

An onboarding experience is described as confusing, but no artifact, research, or dominant
design question has been supplied.

## Review focus

Confirm that the family asks for the missing design context, selects the smallest useful block,
and does not invent user evidence or implementation authority.
