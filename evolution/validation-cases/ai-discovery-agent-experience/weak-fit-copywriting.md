---
id: vc-ai-discovery-weak-fit-001
skill_id: generative-visibility-optimization
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Write five social captions for a fictional event. No entity conflict, search question, measurement decision, generative baseline, or agent action is involved.
expected_behavior:
  must_do:
    - Reject the AI Discovery pack as a weak fit.
    - Route the request to an appropriate writing or content skill.
    - Explain briefly which activation evidence is absent.
  must_not_do:
    - Invent an SEO audit or generative baseline.
    - Require domain-pack templates for ordinary copywriting.
    - Promise reach, traffic, or conversion.
acceptance_criteria:
  - The response selects the smallest suitable non-pack path and performs no speculative discovery analysis.
failure_signals:
  - Facts, inferences, hypotheses, or unavailable evidence are collapsed.
  - A state change or outcome guarantee is presented as skill authority.
notes: Synthetic AI Discovery & Agent Experience v0.1 validation case.
---

# Validation Case

## Scenario

Write five social captions for a fictional event. No entity conflict, search question, measurement decision, generative baseline, or agent action is involved.

## Why this expectation is correct

The pack must activate the smallest evidence-backed contract and preserve human authority, uncertainty, and verification boundaries.

## How a reviewer checks it

Confirm every `must_do` behavior is visible, every `must_not_do` behavior is absent, and the acceptance criterion is supported by the output.
