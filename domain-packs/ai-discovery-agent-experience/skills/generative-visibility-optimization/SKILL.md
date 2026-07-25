---
name: generative-visibility-optimization
description: Evaluate generative retrieval, source selection, citation, answer coverage, and representation fidelity, then form bounded improvement hypotheses with repeatable verification.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this skill when a digital property's information must be evaluated in generative answers.
It connects repeated query evidence, observed sources, answer coverage, citations, canonical
claims, and bounded interventions without promising control over external systems.

The skill does not manipulate models, guarantee citations, write content by default, or treat a
single answer as reliable measurement.

# When to Use

- A product, service, person, brand, method, or claim is absent or misrepresented in generative
  answers.
- Retrieval, source selection, citation relevance, or answer coverage needs investigation.
- Long, diffuse, promotional, or ambiguous content may be difficult to extract faithfully.
- Authority, authorship, freshness, methodology, or claim support affects source use.
- A before/after generative-visibility intervention needs bounded hypotheses.

# When NOT to Use

- Search discovery and indexability foundations are unknown; start with
  `search-indexability-optimization`.
- No repeated, dated query or run evidence can be collected; use `ai-discovery-measurement`
  to design the baseline.
- The dominant issue is canonical entity or claim ambiguity; use
  `knowledge-entity-representation`.
- The task is only content writing, reputation management, or guaranteed AI influence.

# Core Moves

1. **Define the representation objective.** Name audiences, intents, query families, target
   entities, important claims, desired fidelity, and unacceptable distortion.
2. **Establish a repeated baseline.** Use a dated, platform-aware sample with preserved inputs,
   outputs, source observations, citations, and run metadata.
3. **Inspect retrieval and answer behavior.** Compare source presence, answer coverage, citation
   support, extractability, freshness, and representation fidelity with canonical evidence.
4. **Form bounded hypotheses.** Connect observed gaps to content, evidence, structure, entity,
   or source-authority interventions without turning correlations into rules.
5. **Define verification and handoff.** Select a small intervention, comparison method, owner,
   limitations, and stop condition.

# Optional Modules

- **Generative query research** — Map intents into query families, reformulations, comparisons,
  subtasks, and fan-out candidates.
- **Retrieval and source analysis** — Identify observed retrieved or cited sources and relevant
  source classes.
- **Answer extractability review** — Check whether definitions, comparisons, procedures,
  limitations, and evidence can be extracted without distortion.
- **Citation quality review** — Check attribution, prominence, relevance, freshness, and whether
  cited material supports the answer.
- **Representation fidelity review** — Compare generated descriptions with canonical entities,
  facts, terminology, relationships, and limitations.
- **Content evidence review** — Inspect authorship, dates, methodology, primary evidence, claim
  support, and corroboration.
- **Competitive generative landscape** — Compare representation with alternatives without
  treating mention count as business value.

# Activation Triggers

- Activate **generative query research** when no stable evaluation set exists.
- Activate **retrieval and source analysis** when sources or citations can be observed.
- Activate **answer extractability review** when content is long, diffuse, ambiguous,
  interaction-dependent, or heavily promotional.
- Activate **citation quality review** when attribution and source support are part of the
  decision.
- Activate **representation fidelity review** when a person, brand, method, product, or material
  claim must remain accurate.
- Activate **content evidence review** when trust, authority, or consequential claims are weak
  or disputed.
- Activate **competitive generative landscape** only when comparison or category selection is
  decision-relevant.

# Expected Output

```yaml
generative_visibility_review:
  objective:
    audiences: []
    intents: []
    target_entities: []
    important_claims: []
    desired_representation:
  baseline:
    query_set:
    run_records:
    observed_at:
    systems: []
  findings:
    - finding_id:
      skill: generative-visibility-optimization
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
  intervention_hypotheses:
    - change:
      expected_signal:
      comparison_method:
      owner:
      stop_condition:
  limitations: []
```

# Verification

- The query set, systems, dates, run conditions, raw outputs, and source observations are traceable.
- Representation is compared with source-backed canonical entities and claims.
- Citation presence is separated from citation relevance, support, prominence, referral, and value.
- Correlation and provider-specific behavior remain hypotheses or dated observations.
- Each proposed intervention has an expected signal and comparable repeat-measurement method.
- Human readability, accessibility, originality, and brand integrity are preserved.
- No ranking, retrieval, citation, traffic, influence, or conversion outcome is guaranteed.

# Handoff Signals

- Target entities or canonical claims are unstable → `knowledge-entity-representation`.
- Search access or indexability may block retrieval → `search-indexability-optimization`.
- The baseline or comparison protocol is weak → `ai-discovery-measurement`.
- Content, documentation, structured data, or source packaging must change → the relevant
  content or implementation skill and owner.
- Reputation, legal, credential, or brand decisions require authority → human or governance review.

# Pairs Well With

- `ai-discovery-measurement`
- `knowledge-entity-representation`
- `search-indexability-optimization`
- `documentation`
- `knowledge-source-evaluation`
- `domain-language-alignment`
- `observability-review`

# Anti-patterns

- Generalizing from one generated answer or one platform.
- Treating citations, mentions, recommendations, referrals, and conversions as one metric.
- Inventing a model-ranking factor or universal content formula.
- Rewriting for machines while making information less clear, original, accessible, or accurate.
- Recommending `llms.txt`, schema, feeds, or protocol exposure as mandatory.
- Treating a cited source as support without checking the cited passage and claim.
- Hiding platform variance, unavailable sources, or conflicting canonical evidence.
