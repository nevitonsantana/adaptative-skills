---
name: ai-discovery-agent-experience
description: Route broad discovery, SEO, generative visibility, and agent-readiness goals to the smallest sufficient AI Discovery building blocks.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this family entrypoint when the requester names an outcome such as improving SEO,
discovery, generative visibility, or agent readiness without identifying the dominant
technical question. It diagnoses the work and recommends a selective path through the
specialist building blocks in this domain pack.

This entrypoint is optional. Use a specialist skill directly when its question is already
clear. The entrypoint does not crawl, measure, deploy, guarantee rankings or citations, or
perform state-changing agent actions.

# When to Use

- The request is broad, such as “improve our SEO” or “make this easier for agents to use.”
- Several discovery concerns may be connected but their order is unclear.
- The requester needs a primary skill, supporting skill, evidence gap, and handoff.
- The property, audience, decision owner, or available evidence needs to be bounded first.

# When NOT to Use

- The request clearly matches one specialist skill.
- The task is only copywriting, implementation, analytics production, or guaranteed growth.
- No authorized property scope or evidence source exists for the proposed review.
- The requester expects this skill to execute a crawl, change a property, or authorize an action.

# Core Moves

1. **Frame the outcome.** Identify the user's goal, property, audience, important surfaces,
   decision owner, and available evidence. Separate facts, hypotheses, and unavailable inputs.
2. **Classify the dominant question.** Choose among entity representation, search access and
   indexability, measurement, generative visibility, or agent capability actionability.
3. **Select the smallest path.** Name one primary specialist and add supporting specialists
   only when their output is necessary evidence for the next step. State rejected paths when
   the distinction matters.
4. **Preserve evidence boundaries.** Require authorized observations and dated sources. Never
   simulate a crawl, baseline, provider behavior, or agent authorization.
5. **Verify and hand off.** Return the selected path, reasons, evidence gaps, verification,
   owner, and implementation or governance handoff without changing external state.

# Building Blocks

- `knowledge-entity-representation` — entities, claims, relationships, and canonical meaning.
- `search-indexability-optimization` — discovery, access, crawling, rendering, indexing, and canonicals.
- `ai-discovery-measurement` — repeated samples, baselines, variance, and comparison.
- `generative-visibility-optimization` — retrieval, citation, extraction, and fidelity.
- `agent-capability-actionability` — user tasks, authorization, effects, confirmation, and recovery.

Activate only the block whose trigger matches the current evidence. A family membership does
not imply that all five blocks should be loaded.

# Optional Modules

- **Goal framing** — Bound the property, audience, outcome, owner, and evidence before routing.
- **Dominant question classification** — Distinguish entity, indexability, measurement,
  generative visibility, and actionability concerns.
- **Selective composition** — Add a supporting building block only when its output is needed
  by the primary path.
- **Evidence boundary** — Record unavailable access, dated provider context, and authorization
  limits before making a finding.

# Activation Triggers

- Activate **goal framing** when the request names only a broad outcome or uses “SEO” without
  a property, surface, or decision shape.
- Activate **dominant question classification** when more than one specialist could fit.
- Activate **selective composition** when one specialist's output is a required input for another.
- Activate **evidence boundary** whenever property access, baselines, or permissions are absent.

# Expected Output

```yaml
ai_discovery_family_review:
  goal: <user outcome>
  property_scope: <property or unknown>
  dominant_question: entity | indexability | measurement | generative_visibility | actionability
  primary_skill: <one building block>
  supporting_skills: [<only necessary blocks>]
  rejected_paths: [<block and reason>]
  evidence:
    available: [<authorized observations>]
    gaps: [<missing evidence>]
  verification: <repeatable proof>
  handoffs: [<owner or next skill>]
  human_decisions: [<decisions not delegated>]
```

# Verification

- The user goal and property scope are explicit or marked unknown.
- One primary building block is selected and justified.
- Supporting blocks are necessary, not merely adjacent.
- Direct specialist use remains valid for a clear question.
- Evidence gaps and authorization limits are visible.
- No ranking, citation, traffic, or action outcome is promised.
- The result contains verification and a bounded handoff.

# Handoff Signals

- Entity or claim ambiguity → `knowledge-entity-representation`.
- Crawl, index, canonical, or architecture uncertainty → `search-indexability-optimization`.
- Repeated baseline or variance required → `ai-discovery-measurement`.
- Retrieval, citation, or representation fidelity → `generative-visibility-optimization`.
- Concrete state-changing user task → `agent-capability-actionability`.
- Deployment, authorization, priority, or governance decision → consumer owner or AletheIA.

# Pairs Well With

- `knowledge-entity-representation`
- `search-indexability-optimization`
- `ai-discovery-measurement`
- `generative-visibility-optimization`
- `agent-capability-actionability`
- `intent-clarification` for an unresolved user goal

# Anti-patterns

- Loading all domain-pack skills for every broad request.
- Treating “SEO” as proof that indexability is the only issue.
- Using one prompt result as a visibility baseline.
- Inventing property access, provider behavior, or agent permissions.
- Turning the entrypoint into a crawler, scheduler, runtime, or deployment agent.
