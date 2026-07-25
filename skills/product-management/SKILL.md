---
name: product-management
description: Guide product decisions through a modular, evidence-aware workflow covering problem framing, discovery, prioritization, metrics, strategy, delivery handoffs, and outcome review. Use when a product request is ambiguous, crosses several product decisions, requires method selection, or needs explicit human decision boundaries.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: product
---

# Overview

Use this skill as the optional Product Management family entry point when the work spans
more than one product decision or when the correct method is not yet clear. It organizes a
small, context-appropriate product workflow instead of loading every framework at once.
When a specialist contract already matches the question, use that building block directly.

The skill is consultative. It may structure a decision, compare methods, identify missing
evidence, and hand off to another skill. It must not approve investment, change a roadmap,
create delivery tasks, or replace macro governance.

Read only the modules that match the current decision. Use the references in this skill for
method selection and limits; do not treat a framework score as an automatic decision.

# When to Use

- A product request contains several connected decisions.
- The problem, outcome, evidence, or decision owner is unclear.
- A team needs to choose a product method before applying it.
- The requester knows the desired product outcome but not which product capability to start with.
- A product decision needs explicit evidence gaps, human ownership, and a next handoff.
- A roadmap, metric, discovery, or prioritization discussion risks becoming activity without a decision.

# When NOT to Use

- The task already has a clear product decision and only needs one specialized skill.
- Delivery planning is ready and the question is only implementation sequencing (use `feature-planning`).
- The work is only research capture with no product interpretation (use an appropriate research or documentation workflow).
- The requester expects the skill to approve investment, alter a roadmap, create issues, or execute external actions.

# Core Moves

1. **Frame the work.** State the desired outcome, user or customer, problem, decision owner,
   current context, and evidence already available. Separate observed facts from hypotheses,
   assumptions, and requests.
2. **Classify the decision.** Identify the dominant stage (`frame`, `discover`, `decide`,
   `define`, `deliver`, or `learn`) and the decision shape (problem, opportunity, feature,
   portfolio bet, sequence, metric, or outcome review).
3. **Select the smallest sufficient path.** Activate only the modules needed for the decision.
   Hand off to existing skills when they already own the required contract. Name methods that
   were rejected and why.
4. **Execute with explicit uncertainty.** Apply the selected module and method. Label facts,
   evidence, estimates, inferences, assumptions, and unresolved conflicts. Do not manufacture
   customer data, business results, or confidence.
5. **Verify and hand off.** Check whether the output answers the decision, names its limits,
   preserves human decisions, and states the next action, stop condition, or specialized handoff.

# Optional Modules

- **Problem framing** — Read `modules/problem-framing.md` when the request starts from a feature,
  solution, or mandate without a stable problem and outcome.
- **Discovery and evidence** — Read `modules/discovery-and-evidence.md` when evidence is missing,
  contradictory, or too weak to support a product claim.
- **Prioritization and method selection** — Read `modules/prioritization-and-method-selection.md`
  when competing work must be compared or a framework choice is contested. Load only the relevant
  method profile from `references/`.
- **Metrics and outcomes** — Read `modules/metrics-and-outcomes.md` when the work needs an outcome,
  metric, proxy, guardrail, owner, or review cadence.
- **Stakeholder alignment** — Planned module for a later slice; use `triad-check` or `communication`
  for current cross-functional alignment needs.
- **Strategy and opportunity** — Planned module for a later slice; use `business-design` and
  `opportunity-tree-alignment` for the current strategy and opportunity contracts.
- **Roadmap and sequencing** — Planned module for a later slice; use `feature-planning` after a
  value decision is ready, and state sequencing limits explicitly.
- **Learning review** — Planned module for a later slice; use `observability-review` and
  `checkpoint-review` for current signal and review needs.

# Activation Triggers

- Activate **problem framing** when the request names a solution before a problem, outcome, or
  user is clear.
- Activate **discovery and evidence** when the decision depends on unverified user, market, or
  behavior claims.
- Activate **prioritization and method selection** when multiple candidates compete for scarce
  capacity, or when a scoring framework is proposed without sufficient inputs.
- Activate **metrics and outcomes** when success is expressed only as activity, output, or a
  vague goal.
- Hand off to `feature-value-governance` when the question is whether a proposed feature deserves
  investment.
- Hand off to `opportunity-tree-alignment` when the question is how opportunities and features
  connect to outcomes and value levers.
- Hand off to `feature-planning` only after the work is judged worth doing and the first delivery
  slice can be defined.
- Hand off to `observability-review` when the metric or signal requires instrumentation, owner,
  threshold, or operational action.
- Escalate unresolved human ownership, policy, authorization, or cross-boundary decisions rather
  than resolving them inside the skill.

# Expected Output

```yaml
product_management_review:
  decision:
    question: <decision to support>
    stage: frame | discover | decide | define | deliver | learn
    shape: problem | opportunity | feature | portfolio | sequence | metric | outcome_review
  framing:
    outcome: <desired outcome or unknown>
    user_or_customer: <who is affected or unknown>
    problem: <problem statement or unresolved>
    decision_owner: <person or group, if known>
  evidence:
    observed: [<facts or source-backed observations>]
    hypotheses: [<claims to test>]
    assumptions: [<unverified premises>]
    gaps: [<missing evidence>]
  path:
    primary_module: <module>
    supporting_modules: [<module>]
    handoffs: [<skill and reason>]
    rejected_methods: [<method and reason>]
  result:
    recommendation_or_finding: <bounded result>
    confidence: high | medium | low | not_assessed
    limitations: [<limits>]
  human_decisions: [<decisions not delegated>]
  verification:
    success_condition: <what would show the output is useful>
    next_step: <next action, stop, or handoff>
```

# Verification

- The product question, stage, decision shape, and decision owner are explicit or marked unknown.
- Facts, hypotheses, assumptions, and evidence gaps are separated.
- Only necessary modules and references were loaded.
- A method is selected because it fits the decision shape and available evidence, not because it is familiar.
- Rejected methods and their reasons are visible when method choice matters.
- Existing skills are handed off instead of being restated or duplicated.
- The output states confidence, limitations, human decisions, and a verifiable next step.
- No investment, roadmap, delivery, or external side effect is approved by this skill.

# Handoff Signals

- Missing outcome, success definition, or decision owner → `intent-clarification`.
- Feature worthiness is unresolved → `feature-value-governance`.
- Outcome, opportunity, lever, and feature links are unclear → `opportunity-tree-alignment`.
- Business thesis needs structured interpretation → `business-design`.
- Complexity or reversibility is decisive → `feature-complexity-audit`.
- A feature is worth doing and needs an executable slice → `feature-planning`.
- Metric instrumentation or operational thresholds are required → `observability-review`.
- Decision crosses product, design, and engineering → `triad-check`.
- A value claim needs a business or revenue mechanism → `revenue-lever-mapping`.
- Existing capability may need to be limited, deprecated, or removed → `sunset-decision`.

# Pairs Well With

- `intent-clarification`
- `business-design`
- `feature-value-governance`
- `opportunity-tree-alignment`
- `revenue-lever-mapping`
- `feature-complexity-audit`
- `feature-planning`
- `observability-review`
- `triad-check`
- `sunset-decision`

# Anti-patterns

- Loading every Product Management framework before understanding the decision.
- Treating a numerical score as a decision rather than a conversation aid.
- Inventing reach, impact, confidence, customer evidence, revenue, or outcomes.
- Writing a PRD, roadmap, or delivery plan before the underlying decision is ready.
- Duplicating the contract of an existing Adaptive Skill inside a module.
- Creating a new skill when a module is sufficient.
- Hiding uncertainty behind polished product language.
- Treating stakeholder pressure, executive preference, or a loud request as evidence of value.
- Making a human-owned investment, policy, authorization, or governance decision on the user's behalf.
