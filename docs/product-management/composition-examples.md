---
title: Product Management composition examples
description: See bounded Product Management journeys that hand off to existing Adaptive Skills contracts.
---

These examples show sequencing, not automatic orchestration. Each handoff requires the receiving skill's inputs and preserves human authority over the decision.

## 1. Requested feature with no problem

1. `product-management` activates `problem-framing`.
2. The output separates the requested solution from the user problem, desired outcome, context, and evidence gaps.
3. If the value mechanism is still unclear, use `revenue-lever-mapping` or `feature-value-governance` after the frame is accepted.
4. Only a bounded change moves to `feature-planning`.

The safe result is a framed question and next evidence step, not a feature approval or delivery date.

## 2. Data-poor prioritization

1. `product-management` classifies the decision as comparative sequencing with incomplete evidence.
2. `prioritization-and-method-selection` rejects unsupported RICE or ICE precision.
3. The team uses an explicit comparison with visible assumptions, dependencies, and human-owned weights.
4. `feature-value-governance` or `feature-complexity-audit` can deepen a specific investment question.

The output is a decision-ready comparison with uncertainty, not an invented ranking.

## 3. Activity metric presented as value

1. `metrics-and-outcomes` labels the reported activity signal and separates it from the intended outcome.
2. The team defines a measurement window, outcome signal, and guardrail.
3. `observability-review` checks whether the required events and diagnostics can support the claim.
4. A human owner decides whether the evidence supports continuation, change, or stop.

## A composition rule

When a request contains multiple questions, decompose it before loading modules. Each handoff should state its input, owner, expected result, and verification. If the next step crosses investment, roadmap, or macro-governance authority, escalate to the consumer governance layer or AletheIA instead of extending the skill's authority.
