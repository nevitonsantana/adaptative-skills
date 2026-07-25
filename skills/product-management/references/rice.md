# RICE

```yaml
method_profile:
  id: rice
  decision_shape: Compare reasonably comparable initiatives when reach, impact, confidence, and effort can be estimated.
  best_when:
    - candidates affect a defined population
    - a shared horizon makes reach comparable
    - estimates can be challenged by the team
  minimum_inputs:
    - reach
    - impact
    - confidence
    - effort
  invalid_when:
    - reach or impact is invented
    - candidates are different decision types
    - effort estimates are not comparable
  failure_modes:
    - false precision
    - gaming the inputs
    - hiding strategic or dependency constraints
  evidence_requirements:
    - source or rationale for reach and impact
    - confidence basis
    - effort unit and horizon
  human_decisions:
    - scale definitions
    - strategic exceptions
    - acceptance of uncertainty
  sources:
    - https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
```

Use RICE as a transparent comparison aid. Keep the input rationale beside the score and run a sensitivity check when small changes alter the order.
