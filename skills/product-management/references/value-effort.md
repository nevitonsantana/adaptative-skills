# Value versus effort

```yaml
method_profile:
  id: value-effort
  decision_shape: Sort a small set of comparable candidates by relative value and effort.
  best_when:
    - the team needs a quick shared visual comparison
    - candidates are still coarse
    - exact numbers would be misleading
  minimum_inputs:
    - shared definition of value
    - relative effort estimate
    - candidate scope
  invalid_when:
    - value means different things for different candidates
    - effort is not comparable
    - the grid is used to approve investment without evidence
  failure_modes:
    - vague axes
    - quadrant labels treated as decisions
    - political placement of items
  evidence_requirements:
    - definition of value
    - basis for effort
    - uncertainty notes
  human_decisions:
    - axis definitions
    - trade-offs
    - exceptions and follow-up evidence
  sources:
    - https://www.atlassian.com/agile/product-management/prioritization-framework
```

Use this method to expose disagreement and decide what needs better evidence.
