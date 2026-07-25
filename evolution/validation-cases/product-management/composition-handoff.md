---
id: vc-product-management-composition-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "A product lead asks whether to build a requested feature, gives no problem statement, mentions a revenue goal, and asks engineering for a delivery date."
  context: "Synthetic case; no external source content is required."
expected_behavior:
  must_do:
    - "Use problem framing before value or delivery analysis."
    - "Route the revenue mechanism to revenue-lever-mapping or feature-value-governance when the frame is ready."
    - "Route a bounded confirmed change to feature-planning rather than promising a date."
    - "Keep investment and commitment decisions human-owned."
  must_not_do:
    - "Start with a delivery estimate."
    - "Invoke every product skill without a decision boundary."
    - "Treat a revenue goal as proof that the feature creates value."
acceptance_criteria:
  - "The response orders the modules and handoffs instead of running every capability at once."
  - "The response states the minimum inputs required before a delivery plan."
  - "The response does not approve the feature or commit an engineering date."
failure_signals:
  - "The response starts with a delivery estimate."
  - "The response invokes every product skill without a decision boundary."
  - "The response treats a revenue goal as proof that the feature creates value."
---

# Composition and handoff case

## Must do

- Decompose the compound request into framing, value, and delivery questions.
- Order handoffs and identify what each downstream skill must receive.
- Return unresolved authority boundaries explicitly.

## Must not do

- Do not collapse multiple decisions into one feature verdict.
- Do not make another skill's contract part of this skill's output.
- Do not convert a target date request into an implementation commitment.

## Observable evaluation

Pass when the response presents a bounded sequence with explicit prerequisites, handoffs, and verification. Fail when it produces a blended answer that hides which decision each claim supports.

## Minimum evidence and human decisions

Minimum evidence is a problem frame, intended outcome, value mechanism, and delivery constraints. Humans retain authority over investment, trade-offs, and commitment dates.
