# ICE

```yaml
method_profile:
  id: ice
  decision_shape: Make a fast comparison of experiments or initiatives using impact, confidence, and ease.
  best_when:
    - the decision needs a lightweight first pass
    - candidates have roughly comparable scopes
    - the team can explain each estimate
  minimum_inputs:
    - impact
    - confidence
    - ease
  invalid_when:
    - ease is used as a proxy for strategic value
    - candidates require different evidence horizons
    - scores conceal a high-risk dependency
  failure_modes:
    - overvaluing easy work
    - multiplying subjective estimates into false precision
    - ignoring reach or opportunity cost
  evidence_requirements:
    - rationale for each estimate
    - explicit confidence basis
    - known dependencies
  human_decisions:
    - score anchors
    - strategic exceptions
    - whether speed should dominate
  sources:
    - https://www.savio.io/product-roadmap/ice-scoring-model/
```

Use ICE for a fast conversation, not as a substitute for discovery or feature-worthiness judgment.
