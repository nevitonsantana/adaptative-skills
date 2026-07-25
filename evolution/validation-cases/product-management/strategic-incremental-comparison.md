---
id: vc-product-management-strategic-incremental-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "Compare a platform investment that reduces future delivery cost with a small onboarding improvement that has direct usage evidence."
  context: "The platform investment has strategic dependency value but uncertain near-term outcome; the onboarding improvement has stronger local evidence but limited scope."
expected_behavior:
  must_do:
    - "Classify the items as different decision shapes before comparing them."
    - "Keep strategic option value, dependencies, evidence quality, and incremental impact visible."
    - "Recommend a comparison and human trade-off discussion rather than forcing both items into one unsupported score."
  must_not_do:
    - "Treat strategic value as automatically superior."
    - "Treat local usage evidence as sufficient to dismiss platform constraints."
    - "Invent a common numeric scale without naming assumptions and weights."
acceptance_criteria:
  - "The response explains what is and is not comparable."
  - "The response names the dependency and evidence trade-offs."
  - "The response preserves human ownership of the portfolio choice."
failure_signals:
  - "One item wins only because it has more precise-looking numbers."
  - "The platform dependency is omitted from the comparison."
---

# Strategic versus incremental case

## Must do

- Explain the difference between a strategic platform bet and an incremental improvement.
- Make evidence, dependency, reversibility, and option value explicit.
- State which portfolio trade-off needs human acceptance.

## Must not do

- Do not collapse unlike decision objects into a false-precision ranking.
- Do not use strategic language to hide weak evidence.

## Observable evaluation

Pass when the comparison makes the mismatch in evidence and decision shape legible. Fail when a single score hides the trade-off.

## Minimum evidence and human decisions

Minimum evidence is the dependency rationale, expected outcome, local usage evidence, cost horizon, and reversibility. Humans decide the portfolio balance and acceptable strategic risk.
