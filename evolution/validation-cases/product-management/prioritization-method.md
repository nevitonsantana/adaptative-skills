---
id: vc-product-management-prioritization-method-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "Five initiatives must be discussed for next quarter. Reach and confidence are unknown, effort is only a rough t-shirt size, and one initiative is a strategic platform dependency."
  context: "Synthetic case; no external source content is required."
expected_behavior:
  must_do:
    - "Classify the decision as comparative quarterly sequencing with mixed evidence."
    - "Reject unsupported precision from RICE or ICE unless the missing inputs are supplied."
    - "Recommend a transparent comparison that keeps the platform dependency visible as a strategic constraint."
    - "State the weighting and override decisions that require human acceptance."
  must_not_do:
    - "Invent reach, impact, confidence, or numeric rankings."
    - "Apply several frameworks without explaining their purpose."
    - "Treat the platform dependency as an ordinary feature."
acceptance_criteria:
  - "The response names the evidence limitations before selecting a method."
  - "The response selects one primary approach and at most one useful alternative."
  - "The response does not output invented scores or a final investment approval."
  - "The response includes sensitivity, dependencies, and human decision points."
failure_signals:
  - "The response invents reach, impact, confidence, or numeric rankings."
  - "The response applies several frameworks without explaining their purpose."
  - "The response treats the platform dependency as an ordinary feature."
---

# Prioritization method case

## Must do

- Diagnose the decision shape and evidence quality first.
- Explain why unsupported scoring methods are rejected or deferred.
- Produce a comparison structure that can be completed with human-owned weights.

## Must not do

- Do not pretend a t-shirt size is an effort estimate with numeric precision.
- Do not let a method decide strategic trade-offs automatically.
- Do not use a framework catalog as a substitute for a decision.

## Observable evaluation

Pass when the method choice is justified, assumptions are visible, and no unsupported ranking is asserted. Fail when the response gives a precise score or approval from incomplete inputs.

## Minimum evidence and human decisions

Minimum evidence is the initiative list, decision horizon, dependency context, and available confidence level. Humans own strategic weighting, overrides, and the commitment decision.
