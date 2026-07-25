# Cost of delay

```yaml
method_profile:
  id: cost-of-delay
  decision_shape: Sequence work when waiting has a meaningful economic, user, risk, or deadline consequence.
  best_when:
    - timing materially changes value or risk
    - delay cost can be discussed in a shared unit
    - duration or sequencing constraints are visible
  minimum_inputs:
    - consequence of delay
    - duration or time window
    - dependency and deadline context
  invalid_when:
    - delay consequences are invented
    - urgency is only stakeholder pressure
    - duration estimates are not comparable
  failure_modes:
    - urgency inflation
    - ignoring long-term value
    - treating a deadline as evidence of importance
  evidence_requirements:
    - source of the timing constraint
    - affected outcome or cost line
    - confidence in duration
  human_decisions:
    - acceptable risk
    - deadline trade-offs
    - whether the cost is worth the intervention
  sources:
    - https://www.atlassian.com/agile/product-management/prioritization-framework
```

Use cost of delay to make timing consequences explicit; do not let urgency bypass feature-worthiness or evidence checks.
