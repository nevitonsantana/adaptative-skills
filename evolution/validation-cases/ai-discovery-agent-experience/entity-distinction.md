---
id: vc-knowledge-entity-representation-distinction-001
skill_id: knowledge-entity-representation
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Review how the fictional digital property Aurora Living represents Dr. Mira Sol, the Aurora Living Method, and the related consultation and workbook offerings.
  context: Approved sources state that Mira is the author and practitioner, Aurora Living is the named method and brand, consultations are delivered by Mira using the method, and the workbook is a separate product. The home page calls Mira "Aurora Living", the about page calls the method a company, and product metadata assigns the workbook as the author of an article. No stable local identifiers exist.
expected_behavior:
  must_do:
    - Model Mira, Aurora Living, the consultations, and the workbook as distinct entities with typed relationships.
    - Separate source-backed facts from interpretation and mark missing identifiers as unresolved.
    - Identify the conflicting person, brand, method, company, product, and authorship representations.
    - Produce canonical representation guidance, verification checks, and human-owned decisions.
  must_not_do:
    - Collapse the person, method, brand, service, and product into one entity.
    - Invent legal organization status, identifiers, credentials, outcomes, or external corroboration.
    - Publish metadata or decide brand ownership on behalf of the consumer.
acceptance_criteria:
  - The output contains distinct entity records, relationships, authoritative sources, conflicts, confidence, and freshness.
  - Every material finding separates fact, inference, hypothesis, and unavailable evidence.
  - The handoff identifies which corrections need content, metadata, structured-data, or owner review.
failure_signals:
  - The review returns only revised marketing copy.
  - Missing identifiers are silently fabricated.
  - Conflicting entity types are hidden behind one canonical description.
notes: Synthetic baseline for person-brand-method-offering distinction.
---

# Validation Case

## Scenario

A fictional property uses the same name for an author, method, brand, service, and product
across several surfaces.

## Why this expectation is correct

The skill must stabilize the represented objects and their relationships before downstream
search, generative, or structured-data work can be trusted.

## How a reviewer checks it

Confirm that the output creates four distinct entities, names the source-backed relationships,
records the observed conflicts, preserves unknown identifiers, and hands publication decisions
to an owner.
