# Kano

```yaml
method_profile:
  id: kano
  decision_shape: Understand how different requirements may affect customer satisfaction and dissatisfaction.
  best_when:
    - customer requirements can be investigated
    - satisfaction effects differ by feature or quality
    - the decision concerns perceived value, not only delivery effort
  minimum_inputs:
    - requirement or feature description
    - customer evidence or questionnaire design
    - satisfaction interpretation
  invalid_when:
    - categories are guessed from team opinion
    - no customer evidence is available
    - the question is only delivery sequencing
  failure_modes:
    - freezing a category as permanent
    - confusing delight with strategic value
    - overgeneralizing from a small sample
  evidence_requirements:
    - customer responses or authorized evidence
    - segment and context
    - confidence and decay assumptions
  human_decisions:
    - requirement interpretation
    - segment trade-offs
    - investment decision
  sources:
    - https://kanomodel.com/discovering-the-kano-model/
    - https://asq.org/quality-resources/kano-model
```

Use Kano to investigate satisfaction dynamics. Do not use it as an automatic ranking of all product work.
