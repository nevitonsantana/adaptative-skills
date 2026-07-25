---
id: vc-generative-visibility-fidelity-001
skill_id: generative-visibility-optimization
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Review a repeated synthetic baseline in which a fictional brand appears in four of twelve answers, two citations support a different claim, and the founder is repeatedly confused with the method.
expected_behavior:
  must_do:
    - Compare source presence, citation support, extraction, and representation fidelity against canonical evidence.
    - Separate observed answer behavior from hypotheses about retrieval or content.
    - Prioritize entity correction and source-backed content hypotheses with verification.
    - Preserve run variance and unsupported citations as findings.
  must_not_do:
    - Call answer presence a ranking.
    - Assume why a model produced an answer.
    - Guarantee improved citations after a content change.
acceptance_criteria:
  - The output uses the repeated baseline, flags fidelity failures, and proposes bounded experiments rather than universal tactics.
failure_signals:
  - Facts, inferences, hypotheses, or unavailable evidence are collapsed.
  - A state change or outcome guarantee is presented as skill authority.
notes: Synthetic AI Discovery & Agent Experience v0.1 validation case.
---

# Validation Case

## Scenario

Review a repeated synthetic baseline in which a fictional brand appears in four of twelve answers, two citations support a different claim, and the founder is repeatedly confused with the method.

## Why this expectation is correct

The pack must activate the smallest evidence-backed contract and preserve human authority, uncertainty, and verification boundaries.

## How a reviewer checks it

Confirm every `must_do` behavior is visible, every `must_not_do` behavior is absent, and the acceptance criterion is supported by the output.
