# MoradaHarmoniA pre-publication readiness

This is a labeled, documentation-only pilot record. It does not claim that the
MoradaHarmoniA website is published, crawlable, indexed, or visible in generative
systems.

## Scope and evidence boundary

- **Property:** MoradaHarmoniA brand and planned public website
- **Corpus:** `WEBSITE/*-Production.md`, `WEBSITE/Website-Production-Index.md`, and
  `SEO/SEO-AI-Search-Spec.md` from the MHKS OpenKnowledge repository
- **Observed at:** 2026-07-25
- **Method:** targeted OpenKnowledge reads of the named documents
- **Excluded:** private material, `MATERIALS/`, `OPERATIONS/`, live crawl data,
  search-console data, analytics, model runs, and unpublished credentials

## Entity representation

| Entity | Type | Supported relationship | Evidence status |
|---|---|---|---|
| Lais Gotlib | person | authorial authority and founder | documented; credentials require validation |
| MoradaHarmoniA | brand | expression of Lais's vision | documented |
| MoradaHarmoniA method | method | organizes the person–home–life-cycle relationship | documented; final wording requires owner review |
| Diagnóstico da Morada | service/experience | proposed entry point | documented; implementation dependencies remain |
| Consultorias | service | personalized application of the method | documented; formats require confirmation |
| Calendário Cabalístico Prático | product/experience | co-created with Sandra Strauss | documented; current offer and links require confirmation |
| Cursos e Palestras | educational service | learning and speaking offer | documented; active inventory requires confirmation |

## Prioritized findings

### MH-001 — Preserve person, brand, method, and offer boundaries

- **Type:** opportunity
- **Fact:** the production pages and SEO spec name these as distinct entities.
- **Inference:** repeating the distinction across Home, About, FAQ, and summaries should reduce ambiguity.
- **Hypothesis:** generative answers will be less likely to collapse Lais into the brand or method when the relationship is explicit.
- **Recommendation:** keep separate canonical descriptions and typed relationships.
- **Verification:** compare each production page and future generated answer against the entity table.
- **Handoff:** knowledge-entity-representation → documentation/implementation.

### MH-002 — Mark offer readiness before publishing rich metadata

- **Type:** risk
- **Fact:** the production index lists pending validation for formats, links, availability, and contact paths.
- **Inference:** an offer can be structurally documented without being currently available.
- **Recommendation:** classify each offer as confirmed, planned, or awaiting validation before CTA and schema implementation.
- **Verification:** owner approval plus a published destination with matching visible content.
- **Handoff:** human owner → search-indexability-optimization.

### MH-003 — Treat SEO guidance as an implementation contract

- **Type:** opportunity
- **Fact:** `SEO-AI-Search-Spec.md` provides entity definitions, page metadata, FAQs, AI Search summaries, and conditional schema guidance.
- **Inference:** it is a useful comparison baseline for production content.
- **Limitation:** it does not prove that any metadata or schema is deployed.
- **Recommendation:** reconcile each production page with the spec during implementation review.
- **Verification:** compare visible content, metadata, and structured data in the published environment.
- **Handoff:** search-indexability-optimization → implementation owner.

### MH-004 — Contact is a documented gap

- **Type:** blocker
- **Fact:** `Contato-Production.md` is recommended as a pending page in the production index.
- **Recommendation:** do not count contact as a complete public surface until its destination and content exist.
- **Verification:** published URL, accessible content, working CTA, and consent handling.
- **Handoff:** implementation owner.

## Deferred live checks

The following require a public or otherwise authorized environment: HTTP access, robots,
sitemap, canonicals, redirects, rendering, schema validation, indexation, citations,
generative retrieval, and before/after measurement.

## Definition of done for this pilot slice

- [x] Scope and evidence boundary are explicit.
- [x] Production corpus and SEO contract are named.
- [x] Entity distinctions and material gaps are recorded.
- [x] Findings separate facts, inferences, hypotheses, and limitations.
- [ ] Live-site checks are intentionally deferred until publication.
