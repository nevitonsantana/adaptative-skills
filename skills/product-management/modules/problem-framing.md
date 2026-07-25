# Problem framing

Use this module when a request starts with a feature, solution, mandate, or metric but the problem and desired outcome are not stable.

## Procedure

1. Restate the request without adopting its proposed solution.
2. Identify the affected user or customer and the behavior or condition that needs to change.
3. State the desired outcome and how someone would recognize progress.
4. Separate observed facts, interpretations, hypotheses, and assumptions.
5. Declare non-goals and the decision that remains open.
6. Stop or hand off when the problem cannot be stated without inventing context.

## Minimum input

- initial request or observed signal
- affected user, customer, or operator, if known
- desired outcome, if known
- available evidence

## Expected output

```yaml
product_problem_frame:
  request_without_solution: <...>
  affected_user_or_customer: <...>
  problem: <...>
  desired_outcome: <...>
  evidence:
    facts: [<...>]
    hypotheses: [<...>]
    assumptions: [<...>]
  non_goals: [<...>]
  open_decision: <...>
  next_step: <discovery | value_judgment | planning | clarification>
```

## Verification

- The problem is not merely a restatement of the proposed feature.
- The outcome is distinguishable from shipping an output.
- Unsupported claims are marked as hypotheses or assumptions.
- The frame is small enough to guide the next decision.

## Handoff

- Unresolved human intent → `intent-clarification`.
- Strategic interpretation → `business-design`.
- Evidence needed to test the frame → `discovery-and-evidence`.
- Feature worthiness → `feature-value-governance`.

## Anti-patterns

- Accepting the first requested solution as the problem.
- Treating a stakeholder request as user evidence.
- Adding personas, metrics, or outcomes that were not provided.
- Expanding the frame into a full strategy document before the problem is credible.
