---
id: vc-product-management-learning-review-001
skill_id: product-management
case_type: regression
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "Review a launch six weeks later when adoption is up, support contacts are mixed, and the team cannot tell whether the intended customer outcome changed."
  context: "The original hypothesis and guardrail definitions were incomplete, and the data window changed during the rollout."
expected_behavior:
  must_do:
    - "Separate observed changes, attribution limits, hypothesis status, and missing outcome evidence."
    - "Identify the measurement and instrumentation gaps before recommending continuation or rollback."
    - "Route the measurement review to observability-review and preserve a human renewal decision."
  must_not_do:
    - "Call the launch successful because adoption increased."
    - "Infer causality from a changing measurement window."
    - "Recommend keep, expand, or stop without naming the missing evidence."
acceptance_criteria:
  - "The response distinguishes adoption, support signals, outcome, and guardrails."
  - "The response states what can and cannot be concluded."
  - "The response defines a bounded next review and decision owner."
failure_signals:
  - "The response converts adoption into customer value."
  - "The response hides the instrumentation and window changes."
---

# Learning review case

## Must do

- Reconstruct the original hypothesis and measurement contract.
- Compare observed signals with outcome and guardrail evidence.
- Make the next learning step and decision owner explicit.

## Must not do

- Do not treat a post-launch review as a celebration metric summary.
- Do not claim causality where the data window and instrumentation changed.

## Observable evaluation

Pass when the review preserves uncertainty and defines a concrete evidence repair. Fail when it gives a continuation recommendation from adoption alone.

## Minimum evidence and human decisions

Minimum evidence is the original hypothesis, event definitions, windows, segment, and support context. Humans decide whether the product bet should continue, change, or stop.
