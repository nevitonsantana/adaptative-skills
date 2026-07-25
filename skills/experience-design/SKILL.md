---
name: experience-design
description: Guide broad experience-design requests to the smallest sufficient strategy, critique, writing, or design-system building block.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: design
---

# Overview

Use this optional family entrypoint when a requester names an experience outcome but the
dominant design question is unclear. It selects among `ux-strategy`, `ux-provocation`,
`heuristic-audit`, `ux-writing`, and `design-system-intelligence`.

Use a building block directly when the question is specific. This family does not design,
approve, implement, or promote patterns by itself.

# When to Use

- A request says “improve the experience” without identifying the design decision.
- Strategy, critique, content, or design-system concerns may be mixed.
- A team needs to choose the right design lens before producing an artifact.

# When NOT to Use

- The task clearly matches one design skill.
- The request is implementation-only or needs a product, engineering, or governance decision.
- The requester expects a final design, pattern promotion, or external change.

# Core Moves

1. **Frame the experience outcome.** Identify users, context, surface, desired behavior,
   constraints, evidence, and decision owner.
2. **Classify the dominant design question.** Distinguish strategy, hypothesis pressure-test,
   usability audit, content clarity, or design-system alignment.
3. **Select the smallest path.** Choose one primary building block and add support only when
   its output is required by the next design decision.
4. **Keep observation separate from proposal.** Label evidence, interpretation, hypothesis,
   recommendation, and unresolved design judgment.
5. **Verify and hand off.** Return a bounded result, decision owner, next check, and handoff
   without implementing or promoting design changes.

# Building Blocks

- `ux-strategy` — align experience direction with user, product, and business context.
- `ux-provocation` — pressure-test a hypothesis, assumption, or experience direction.
- `heuristic-audit` — inspect an interface against usability heuristics.
- `ux-writing` — improve interface language, clarity, and action guidance.
- `design-system-intelligence` — review artifacts against a declared design-system source.

Do not load all five blocks because the task mentions “UX”.

# Optional Modules

- **Experience intake** — bound audience, surface, outcome, and evidence.
- **Design-question classification** — distinguish direction, critique, content, and system concerns.
- **Selective composition** — add a supporting block only when its output is necessary.
- **Decision-owner check** — preserve product, design-system, and implementation ownership.

# Activation Triggers

- Direction or prioritization is unclear → `ux-strategy`.
- A hypothesis needs pressure-testing → `ux-provocation`.
- An existing interface needs inspection → `heuristic-audit`.
- Interface language is the primary issue → `ux-writing`.
- A declared design system is the source of truth → `design-system-intelligence`.

# Expected Output

```yaml
experience_design_review:
  outcome: <desired experience outcome>
  surface: <surface or unknown>
  dominant_question: strategy | provocation | audit | writing | design_system
  primary_building_block: <skill>
  supporting_building_blocks: [<only necessary skills>]
  evidence: [<observations or gaps>]
  recommendation: <bounded result>
  human_decisions: [<design or product decisions not delegated>]
  verification: <next check>
  handoffs: [<owner or next skill>]
```

# Verification

- The experience outcome and surface are explicit or unknown.
- The primary design question and building block are justified.
- Supporting blocks have a clear dependency.
- Evidence, interpretation, and proposal remain distinct.
- Ownership, verification, and handoff are explicit.
- No implementation, approval, or pattern promotion is claimed.

# Handoff Signals

- Product outcome or investment is unclear → `product-management`.
- Delivery or implementation is ready → `feature-planning` or implementation owner.
- Design-system owner decision is required → `design-system-intelligence` and owner review.
- Cross-functional trade-off is unresolved → `triad-check`.

# Pairs Well With

- `ux-strategy`
- `ux-provocation`
- `heuristic-audit`
- `ux-writing`
- `design-system-intelligence`
- `triad-check`

# Anti-patterns

- Treating every UX request as a strategy exercise.
- Loading every design block before identifying the design question.
- Presenting heuristic findings as user research evidence.
- Promoting a pattern without design-system owner review.
- Turning the family into a design generator or implementation runtime.
