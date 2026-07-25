---
id: vc-product-management-stakeholder-conflict-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "Sales wants a customer-specific capability this quarter, support wants reliability work first, and engineering identifies a dependency that neither request addresses."
  context: "No shared outcome, decision owner, or agreed evidence threshold has been recorded."
expected_behavior:
  must_do:
    - "Frame the conflict as competing outcomes and constraints rather than voting between departments."
    - "Identify the missing decision owner, evidence, dependency, and trade-off criteria."
    - "Recommend stakeholder alignment or triad-check after the decision frame is explicit."
  must_not_do:
    - "Treat the loudest stakeholder as the decision owner."
    - "Resolve the conflict by inventing customer value or delivery certainty."
    - "Commit a roadmap item before the trade-off is accepted."
acceptance_criteria:
  - "The response identifies competing outcomes and the unresolved owner."
  - "The response names a bounded alignment step and its expected input."
  - "No departmental preference is presented as the final decision."
failure_signals:
  - "The output picks a winner without criteria or evidence."
  - "The output creates a roadmap commitment."
---

# Stakeholder conflict case

## Must do

- Surface the conflict, shared objective, constraints, and missing authority.
- Prepare a decision conversation that can be verified.
- Route cross-functional disagreement to the existing alignment contracts.

## Must not do

- Do not turn stakeholder advocacy into evidence.
- Do not use consensus language to conceal an unresolved trade-off.

## Observable evaluation

Pass when the response makes ownership and decision criteria explicit and proposes a bounded alignment handoff. Fail when it resolves the disagreement by organizational seniority.

## Minimum evidence and human decisions

Minimum evidence is the request from each stakeholder, affected outcome, dependency, and decision horizon. Humans own the trade-off and the final commitment.
