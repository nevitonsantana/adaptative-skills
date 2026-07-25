# AI Discovery & Agent Experience

> **Experimental domain pack, version 0.1.0.** This pack is domain-specific evidence for
> Adaptive Skills. It is not generic skill truth and is not included in the main APM
> payload.

## Purpose

Help teams review whether a digital property can be discovered, interpreted, represented,
measured, and—when a concrete user task exists—used safely by agents.

The pack provides an optional family entrypoint plus five independent building blocks. This
keeps broad requests easy to start while preserving direct specialist use:

| Skill | Status | Primary question |
|---|---|---|
| `knowledge-entity-representation` | available | Are entities, claims, relationships, and canonical descriptions coherent? |
| `search-indexability-optimization` | available | Can search systems discover, crawl, index, and interpret the property? |
| `ai-discovery-measurement` | available | Can discovery and representation outcomes be measured repeatedly? |
| `generative-visibility-optimization` | available | Can generative systems retrieve, cite, and faithfully use the information? |
| `agent-capability-actionability` | available | Can an agent discover and safely perform a meaningful user-owned action? |

The family entrypoint is `ai-discovery-agent-experience`. It diagnoses a broad goal and
selects the smallest sufficient building block. It does not load all five skills by default.

## Use this pack when

- a site or digital property needs a bounded search and AI-discovery review;
- people, brands, methods, products, or claims are confused across surfaces;
- generative visibility must be evaluated with repeatable evidence;
- an agent may need to perform a concrete action, with authorization and recovery;
- a team needs findings that separate facts, inferences, hypotheses, and unavailable evidence.

## Do not use this pack when

- the task is only to write content, build a checkout, or implement an API;
- no discovery, representation, measurement, or actionability decision exists;
- the requester expects guaranteed rankings, citations, traffic, conversion, or adoption;
- the work requires a crawler, analytics service, protocol server, or production agent runtime.

## Layer boundaries

- **Humans or a governance layer** own intent, priority, approval, escalation, and closure.
- **This pack** owns reusable methods, triggers, evidence shapes, verification, and handoffs.
- **A runtime or harness** owns browsing, crawling, APIs, authentication, execution, and logs.
- **The consumer project** owns local content, brand facts, analytics, permissions, and changes.

The skills declare findings and recommendations. They do not approve, block, deploy, or
change external state.

## Start with the smallest fit

Use the family entrypoint when the goal is broad or the dominant question is unknown. Use a
building block directly when the question is already specific:

Use one skill when it answers the dominant question:

- entity or claim ambiguity → `knowledge-entity-representation`;
- crawl, index, canonical, or architecture uncertainty → `search-indexability-optimization`;
- query sample, repeated runs, comparison, or variance → `ai-discovery-measurement`;
- retrieval, citation, answer coverage, or representation fidelity →
  `generative-visibility-optimization`;
- a concrete state-changing agent task → `agent-capability-actionability`.

The family is a guided composition, not a required wrapper. A direct specialist contract
remains valid for users and agents that already know the task shape.

Common compositions:

1. **Pre-launch review:** entity representation → search foundations → measurement →
   generative visibility. Add actionability only for a defined action.
2. **Generative baseline:** measurement → generative visibility → entity review when
   representation conflicts appear.
3. **Agent action readiness:** actionability → measurement of task completion, correctness,
   human intervention, side effects, and recovery.

Complete the [digital-property intake](templates/digital-property-intake.md), use only the
templates needed by the selected skills, and finish with reviewable findings and handoffs.

The templates are optional accelerators for full-pack use. The canonical `SKILL.md`
contract remains usable without them when projected independently.

See the [standards and sources register](references/standards-and-sources.md) for dated,
primary-source pointers. The register is context, not a universal tactic list.

## Evidence policy

Every material finding must identify its source, method, observation date, raw observation,
confidence, limitation, affected decision, verification, and handoff. Facts, inferences,
hypotheses, recommendations, and unavailable evidence remain distinct.

Provider-specific observations are dated context. They are not promoted into universal
Core Moves.

## Pilot policy

MoradaHarmoniA is the planned first consumer scaffold. It may preserve the public distinction
between Laís Gottlieb de Franco as authorial authority, MoradaHarmoniA as method and brand,
and the connected offerings. It must not contain private material or claim that a baseline
has been executed until raw, authorized evidence exists.
