# AI Discovery & Agent Experience

> **Experimental domain-pack foundation.** This pack is domain-specific evidence for
> Adaptive Skills. It is not generic skill truth and is not included in the main APM
> payload.

## Purpose

Help teams review whether a digital property can be discovered, interpreted, represented,
measured, and—when a concrete user task exists—used safely by agents.

The pack separates five related intents instead of treating "SEO for AI" as one oversized
checklist:

| Skill | Status | Primary question |
|---|---|---|
| `knowledge-entity-representation` | available | Are entities, claims, relationships, and canonical descriptions coherent? |
| `search-indexability-optimization` | planned for v0.1 | Can search systems discover, crawl, index, and interpret the property? |
| `ai-discovery-measurement` | planned for v0.1 | Can discovery and representation outcomes be measured repeatedly? |
| `generative-visibility-optimization` | planned for v0.1 | Can generative systems retrieve, cite, and faithfully use the information? |
| `agent-capability-actionability` | planned for v0.1 | Can an agent discover and safely perform a meaningful user-owned action? |

Do not present the pack as complete until all five contracts and their validation cases
have landed.

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

## Foundation workflow

The first implemented skill is `knowledge-entity-representation`. Use it before search or
generative reviews when the target people, brands, products, methods, relationships, or
claims are ambiguous.

1. Complete the [digital-property intake](templates/digital-property-intake.md).
2. Create an [entity inventory](templates/entity-inventory.md).
3. Connect material claims to sources with the
   [claim-evidence map](templates/claim-evidence-map.md).
4. Record reviewable outcomes with the
   [prioritized finding](templates/prioritized-finding.md).
5. Hand implementation, approval, and follow-up measurement to the appropriate owner.

The templates are optional accelerators for full-pack use. The canonical `SKILL.md`
contract remains usable without them when projected independently.

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
