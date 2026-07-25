---
name: knowledge-entity-representation
description: Review and stabilize how people, organizations, brands, products, methods, claims, and relationships are represented across human-readable and machine-readable surfaces.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this skill when a digital property depends on entities and claims that systems or
people may confuse. It creates a source-backed representation contract before downstream
search, generative-visibility, structured-data, or agent-action work.

The skill is consultative. It may identify ambiguity, propose canonical descriptions, and
recommend updates. It must not invent facts, choose business positioning without an owner,
publish metadata, or decide that a disputed claim is true.

# When to Use

- A person, organization, brand, method, product, service, or offer is confused with another.
- Names, descriptions, roles, dates, attributes, or relationships vary across surfaces.
- Search or generative systems need stable target entities and canonical claims.
- Structured or machine-readable representation is being considered.
- Material authority, outcome, credential, or differentiator claims need provenance.

# When NOT to Use

- The task is only terminology cleanup inside one codebase; use `domain-language-alignment`.
- The primary question is whether a knowledge source may enter governed context; use
  `knowledge-source-evaluation`.
- The entities and claims are already stable and the dominant need is crawl/index review,
  generative measurement, or action execution.
- The requester expects the skill to settle a legal, ownership, brand, or policy dispute.

# Core Moves

1. **Bound the representation decision.** Name the target property, audiences, entity types,
   affected surfaces, decision owner, required freshness, and evidence currently available.
2. **Model entities and relationships.** Identify canonical names, aliases, types, identifiers,
   roles, attributes, versions, and relationships that must remain distinguishable.
3. **Compare representations.** Inspect available pages, metadata, structured data, profiles,
   repositories, and approved external references without treating absence as proof.
4. **Connect claims to evidence.** Separate facts, inferences, hypotheses, recommendations,
   conflicts, and unavailable evidence; record source, method, date, owner, and limitations.
5. **Produce a bounded representation handoff.** Recommend canonical descriptions, relationship
   corrections, ownership, verification, and downstream work without mutating consumer surfaces.

# Optional Modules

- **Entity inventory** — Inventory entities, aliases, types, identifiers, relationships, and
  authoritative surfaces when several entities or historical names exist.
- **Canonical description design** — Draft short, medium, and detailed source-backed descriptions
  when systems or readers receive inconsistent explanations.
- **Entity consistency audit** — Compare names, dates, roles, categories, attributes, and
  relationships across multiple surfaces.
- **Claim-evidence mapping** — Connect material claims to evidence, dates, owners, and limitations
  when authority, expertise, outcomes, credentials, numbers, or differentiation matter.
- **Knowledge-graph readiness** — Check whether entity types and relationships are explicit enough
  for graph-like interpretation when a concrete representation consumer exists.
- **Machine-readable packaging** — Evaluate schema, feeds, sitemaps, documentation forms, or other
  packaging only when a named consumer or retrieval problem justifies it.
- **Version and freshness governance** — Distinguish current, historical, deprecated, and
  time-sensitive representations when offerings or organizations evolve.

# Activation Triggers

- Activate **entity inventory** when more than one person, brand, method, organization, offering,
  alias, or version appears.
- Activate **canonical description design** when descriptions vary materially or blur authority,
  brand, method, product, or offering.
- Activate **entity consistency audit** when representations span several owned or external
  surfaces.
- Activate **claim-evidence mapping** when a material claim influences trust, eligibility,
  comparison, or a consequential decision.
- Activate **knowledge-graph readiness** only when structured entity reconciliation is a stated
  objective.
- Activate **machine-readable packaging** only when a concrete consumer and failure mode are named;
  no tactic is mandatory by default.
- Activate **version and freshness governance** when descriptions, offers, teams, facts, or
  evidence change over time.

# Expected Output

```yaml
entity_representation_review:
  scope:
    target_property: <property or corpus>
    decision: <representation decision>
    owner: <human owner or unknown>
    observed_at: <date or unavailable>
  entities:
    - id: <stable local id>
      canonical_name: <name or unresolved>
      type: <person | organization | brand | method | product | service | other>
      aliases: [<alias>]
      relationships: [<typed relationship>]
      authoritative_surfaces: [<source>]
      freshness: <current | historical | deprecated | unknown>
  findings:
    - finding_id: <stable id>
      skill: knowledge-entity-representation
      module: <activated module>
      target: <entity, claim, relationship, or surface>
      finding_type: blocker | degradation | risk | opportunity | unknown
      evidence:
        source: <source or unavailable>
        observed_at: <date or unavailable>
        method: <inspection method>
        raw_observation: <observation or unavailable>
      confidence: high | medium | low | unavailable
      fact: <source-backed fact or unavailable>
      inference: <bounded interpretation or none>
      hypothesis: <testable proposition or none>
      impact: <affected understanding or decision>
      recommendation: <bounded recommendation>
      verification: <observable check>
      handoff: <owner or skill>
  canonical_guidance:
    descriptions: [<source-backed description candidate>]
    relationship_corrections: [<correction>]
    unresolved_conflicts: [<conflict or missing evidence>]
  limitations: [<scope or evidence limit>]
```

# Verification

- Every entity has a stable local identifier or is explicitly unresolved.
- Canonical names, aliases, types, roles, relationships, versions, and authoritative surfaces are
  source-backed or marked unknown.
- Facts, inferences, hypotheses, recommendations, conflicts, and unavailable evidence are distinct.
- Material claims identify evidence, observation date, method, owner, and limitations.
- Proposed descriptions preserve human clarity and do not hide disagreement behind polished copy.
- Machine-readable packaging is recommended only for a concrete consumer and supported type.
- The output names verification and ownership without making external changes or business decisions.

# Handoff Signals

- The representation problem is primarily wording or terminology inside one domain →
  `domain-language-alignment` or `documentation`.
- Source eligibility or precedence is unresolved → `knowledge-source-evaluation` or
  `knowledge-conflict-resolution`.
- The target entities are stable and the next need is discovery/crawl review →
  `search-indexability-optimization`.
- Repeated generative representation must be measured → `ai-discovery-measurement`.
- A legal, ownership, credential, policy, or brand decision lacks an authorized owner → human or
  governance review.
- A schema, feed, page, profile, or repository must be changed → implementation owner.

# Pairs Well With

- `domain-language-alignment`
- `documentation`
- `knowledge-source-evaluation`
- `knowledge-conflict-resolution`
- `restricted-context-check`
- `observability-review`
- `search-indexability-optimization`
- `ai-discovery-measurement`
- `generative-visibility-optimization`

# Anti-patterns

- Treating a search result, generated answer, or repeated phrase as authoritative by itself.
- Inventing identifiers, relationships, credentials, outcomes, dates, or corroboration.
- Collapsing a person, organization, brand, method, product, and offering into one entity for
  convenience.
- Treating missing evidence as evidence of absence or falsehood.
- Resolving disputed ownership, positioning, or policy without an authorized decision owner.
- Recommending schema, `llms.txt`, feeds, or a knowledge graph without a concrete consumer problem.
- Converting a provider-specific observation into universal representation truth.
- Optimizing machine-readable descriptions at the expense of accurate, accessible human meaning.
