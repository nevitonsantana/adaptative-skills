# Opportunity scoring

```yaml
method_profile:
  id: opportunity-scoring
  decision_shape: Compare unmet importance and satisfaction for a defined outcome or need.
  best_when:
    - an outcome or need is already framed
    - user evidence can distinguish importance from satisfaction
    - the comparison is within a coherent opportunity set
  minimum_inputs:
    - outcome or need
    - importance evidence
    - satisfaction evidence
    - segment context
  invalid_when:
    - opportunities are not comparable
    - importance is assumed from feature requests
    - the outcome is not defined
  failure_modes:
    - mistaking dissatisfaction for opportunity value
    - ignoring strategic or feasibility constraints
    - treating a survey score as a complete decision
  evidence_requirements:
    - source and population of importance data
    - source and population of satisfaction data
    - segment and context limits
  human_decisions:
    - opportunity framing
    - evidence quality
    - investment and sequencing
  sources:
    - https://strategyn.com/2015/10/09/what-is-opportunity-scoring/
```

Use opportunity scoring only after the outcome and opportunity language are stable. Hand off to `opportunity-tree-alignment` when the tree itself is unclear.
