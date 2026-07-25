---
id: vc-product-management-metrics-outcome-001
skill_id: product-management
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "A launch review reports that 92% of invited users opened the new workflow and concludes that the launch improved customer value. No retention, completion, or customer outcome is available."
  context: "Synthetic case; no external source content is required."
expected_behavior:
  must_do:
    - "Classify invitation opens as an activity or adoption signal, not proof of value."
    - "Separate the observed metric from the desired outcome and guardrails."
    - "Recommend a follow-up measurement path without claiming launch success."
  must_not_do:
    - "Equate opens with customer value."
    - "Invent retention or satisfaction results."
    - "Recommend scaling solely from the activity metric."
acceptance_criteria:
  - "The response labels the metric's scope and limitation."
  - "The response proposes an outcome metric and relevant guardrail with a measurement window."
  - "The response preserves the human decision about whether the evidence supports continuation."
failure_signals:
  - "The response equates opens with customer value."
  - "The response invents retention or satisfaction results."
  - "The response recommends scaling solely from the activity metric."
---

# Metrics and outcomes case

## Must do

- Name the observed activity signal precisely.
- Connect it to a proposed user or business outcome only as a hypothesis.
- Define what would be measured next and how a guardrail would protect against harm.

## Must not do

- Do not rename an activity metric as an outcome metric.
- Do not claim causality from a launch review with no comparison or outcome evidence.
- Do not set a target without identifying its measurement window and owner.

## Observable evaluation

Pass when the response distinguishes activity, outcome, and guardrail signals and defines a next measurement step. Fail when it treats the reported percentage as proof of value.

## Minimum evidence and human decisions

Minimum evidence is the metric definition, population, time window, and event source. Humans decide whether the outcome threshold is adequate to continue, change, or stop the initiative.
