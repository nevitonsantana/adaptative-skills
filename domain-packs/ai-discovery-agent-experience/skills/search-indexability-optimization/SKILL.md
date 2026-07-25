---
name: search-indexability-optimization
description: Evaluate whether search systems can discover, access, crawl, render, index, canonicalize, interpret, and navigate a digital property using available evidence.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this skill to diagnose search discovery and indexability foundations before proposing
content or generative-visibility interventions. It separates observed blockers and
degradations from opportunities and unavailable evidence.

The skill does not operate a crawler, change directives, deploy redirects, guarantee
indexing, or infer search-engine state from a single page inspection.

# When to Use

- Search systems may not discover, access, render, index, or interpret important surfaces.
- Duplicate, migrated, localized, filtered, dynamic, or legacy URLs create conflicting signals.
- Navigation, hierarchy, internal links, or orphaned content affect discoverability.
- Structured data or meaningful text may not match visible content.
- Search performance evidence must be connected to technical hypotheses.

# When NOT to Use

- The dominant issue is inconsistent people, brands, methods, products, or claims; use
  `knowledge-entity-representation`.
- The task is only to write or restructure content without a search-access decision.
- The requester wants rank guarantees, a production crawl, monitoring, or automated changes.
- The review has no authorized property scope or evidence source.

# Core Moves

1. **Bound the indexability intent.** Name property, environments, audiences, important
   surfaces, expected access, exclusions, decision owner, and available evidence.
2. **Inspect discovery and access signals.** Review available URL inventories, responses,
   directives, sitemaps, rendering, authentication, resources, and crawler observations.
3. **Evaluate interpretation paths.** Review canonicalization, duplication, hierarchy,
   navigation, internal relationships, accessible text, metadata, and structured representation.
4. **Classify evidence.** Separate blockers, degradations, risks, opportunities, and unknowns;
   distinguish observed facts from inferences and hypotheses.
5. **Prioritize verification and handoff.** Connect each finding to consequence, bounded
   remediation, owner, and an observable recheck without changing the property.

# Optional Modules

- **Crawl access review** — Inspect directives, response behavior, authentication, resources,
  rendering dependencies, and crawler access.
- **Indexability and canonicalization review** — Inspect canonicals, redirects, `noindex`,
  duplication, pagination, locale, versions, filters, and conflicting URLs.
- **Information architecture review** — Inspect hierarchy, navigation, internal links,
  discoverability depth, semantic grouping, and orphaned surfaces.
- **Structured-data consistency review** — Compare structured data with visible content,
  supported types, entities, and relationships.
- **Content accessibility review** — Check whether meaningful content is available as accessible
  text rather than only in images, interaction, or client-only states.
- **Search performance baseline** — Use authorized webmaster or analytics evidence to compare
  technical hypotheses with observed discovery and search behavior.

# Activation Triggers

- Activate **crawl access review** when access is blocked, dynamic, authenticated, inconsistent,
  or environment-dependent.
- Activate **indexability and canonicalization review** for duplicates, migrations, locales,
  filters, pagination, multiple versions, or legacy URLs.
- Activate **information architecture review** when several offerings, audiences, content types,
  or future expansion paths exist.
- Activate **structured-data consistency review** when structured data exists or rich-result and
  entity interpretation matter.
- Activate **content accessibility review** for JavaScript-heavy, visual, multimedia, or
  interaction-dependent surfaces.
- Activate **search performance baseline** only when authorized performance evidence exists.

# Expected Output

```yaml
search_indexability_review:
  scope:
    property:
    environments: []
    important_surfaces: []
    indexability_intent:
    observed_at:
  findings:
    - finding_id:
      skill: search-indexability-optimization
      module:
      target:
      finding_type: blocker | degradation | risk | opportunity | unknown
      evidence:
        source:
        observed_at:
        method:
        raw_observation:
      confidence: high | medium | low | unavailable
      fact:
      inference:
      hypothesis:
      impact:
      recommendation:
      verification:
      handoff:
  remediation_sequence: []
  unavailable_evidence: []
  limitations: []
```

# Verification

- Scope, environment, important surfaces, expected access, and intended exclusions are explicit.
- Access, crawl, render, index, and performance claims identify their evidence and date.
- Canonical, redirect, directive, structured-data, and architecture findings describe the
  observed target rather than a remembered provider rule.
- Missing access or performance evidence remains unavailable.
- Findings distinguish eligibility from actual indexing, visibility, ranking, traffic, and value.
- Every remediation has an owner and a repeatable verification method.
- No ranking, indexing, rich result, traffic, or conversion outcome is guaranteed.

# Handoff Signals

- Entity or claim ambiguity blocks interpretation → `knowledge-entity-representation`.
- Repeated generative retrieval or citation behavior must be studied →
  `ai-discovery-measurement` and `generative-visibility-optimization`.
- A finding requires code, infrastructure, content, redirect, metadata, or deployment changes →
  the relevant implementation owner.
- Access requires credentials, production logs, webmaster data, or policy approval → authorized
  consumer owner.
- A business prioritization decision remains unresolved → human or governance review.

# Pairs Well With

- `knowledge-entity-representation`
- `ai-discovery-measurement`
- `generative-visibility-optimization`
- `documentation`
- `architecture-review`
- `qa-review`
- `observability-review`

# Anti-patterns

- Treating a page response or manual browser view as proof of crawler or index state.
- Reporting eligibility, indexing, ranking, traffic, and conversion as the same outcome.
- Recommending every possible SEO tactic instead of the smallest evidence-backed remediation.
- Treating schema, a sitemap, or `llms.txt` as universally required.
- Ignoring authentication, environment, locale, duplication, rendering, or canonical conflicts.
- Inferring a performance problem without authorized search-performance evidence.
- Making machine access less safe, accessible, or understandable for people.
