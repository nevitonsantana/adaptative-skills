# Prioritization and method selection

Use this module when several candidates compete for scarce capacity or when someone proposes a framework without checking whether its inputs and decision shape fit.

## Procedure

1. Identify the objects being compared: opportunities, features, initiatives, bets, or sequencing options.
2. State the horizon, constraint, outcome, and decision owner.
3. Assess evidence quality for value, reach, impact, confidence, effort, time, and dependencies.
4. Select one primary method and at most one alternative from the method profiles.
5. Reject methods whose assumptions or inputs do not fit.
6. Apply the method transparently, preserving the reasoning behind each estimate.
7. Stress-test sensitivity, strategic overrides, dependencies, and unknowns.
8. Return a recommendation for human acceptance, not an automatic ranking authority.

## Method selection

Read `references/framework-selection.md` first. Then load only the relevant profile from `references/`. Do not load every method profile by default.

## Expected output

```yaml
prioritization_decision:
  decision_object: <...>
  horizon: <...>
  constraint: <...>
  method:
    selected: <method>
    alternative: <method or none>
    why_fit: <...>
    rejected: [<method and reason>]
  candidates:
    - id: <...>
      value_evidence: <...>
      score_or_position: <...>
      confidence: high | medium | low
      assumptions: [<...>]
  sensitivity: [<change that could alter the result>]
  human_overrides: [<accepted or pending override>]
  recommendation: <bounded recommendation>
```

## Verification

- The comparison objects are comparable for the chosen decision.
- Each required input is present or marked unknown.
- The method is not used to manufacture precision.
- Sensitivity, dependencies, and overrides are visible.
- The final ranking remains a human-owned judgment.

## Handoff

- Feature worthiness → `feature-value-governance`.
- Outcome and opportunity structure → `opportunity-tree-alignment`.
- Permanent cost or reversibility → `feature-complexity-audit`.
- Delivery sequence after commitment → `feature-planning`.

## Anti-patterns

- Choosing RICE, ICE, or another score because it is familiar.
- Ranking incomparable objects in one table without stating the consequence.
- Treating low confidence as a small number without explaining the missing evidence.
- Replacing a strategic decision with arithmetic.
