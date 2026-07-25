# Metrics and outcomes

Use this module when success is expressed as activity, output, adoption without value, or a vague aspiration.

## Procedure

1. State the product decision or outcome the signal must support.
2. Define the behavior or condition expected to change.
3. Choose a primary outcome metric and distinguish it from proxies.
4. Add guardrails for important harm, quality, or cost risks.
5. Define owner, population, window, direction, cadence, and action.
6. State what the metric cannot establish and what evidence would be needed next.
7. Hand off instrumentation or operational threshold design when the contract needs engineering work.

## Expected output

```yaml
product_outcome_measurement:
  decision_supported: <...>
  intended_outcome: <...>
  expected_behavior_change: <...>
  primary_metric:
    name: <...>
    direction: increase | decrease | maintain
    population: <...>
    window: <...>
  proxies: [<...>]
  guardrails:
    - metric: <...>
      must_not: <...>
  owner: <...>
  review_cadence: <...>
  action_if_signal_changes: <...>
  limitations: [<...>]
```

## Verification

- The metric is attached to a decision and an intended outcome.
- Activity and value are not conflated.
- Population, direction, window, owner, and action are explicit.
- Guardrails cover consequential failure modes.
- The metric is not presented as proof of causality without a suitable design.

## Handoff

- Instrumentation, alerts, or diagnostics → `observability-review`.
- Delivery slice or implementation dependency → `feature-planning`.
- Business or revenue mechanism → `revenue-lever-mapping`.
- Cross-functional metric decision → `triad-check`.

## Anti-patterns

- Calling launches, clicks, or completed tasks outcomes by default.
- Choosing a metric because it is easy to collect.
- Omitting guardrails because the primary metric is improving.
- Treating a correlation as causal evidence.
