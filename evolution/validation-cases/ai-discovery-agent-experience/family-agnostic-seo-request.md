---
id: vc-ai-discovery-family-agnostic-seo-001
skill_id: ai-discovery-agent-experience
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task:
    request: "Improve our SEO so search engines and AI assistants can find us."
    property: unknown
    evidence: unavailable
expected_behavior:
  must_do:
    - Start with ai-discovery-agent-experience because the request is broad.
    - Separate search indexability, entity representation, generative visibility, and measurement as distinct questions.
    - Select one primary building block only after identifying the missing scope and evidence.
    - Mark property access and baseline evidence as unavailable.
    - Preserve implementation, authorization, and priority decisions for the responsible owner.
  must_not_do:
    - Load all five specialist skills by default.
    - Promise rankings, citations, traffic, or AI visibility.
    - Pretend to have crawled the property or measured a baseline.
    - Recommend deployment changes without authorized scope and evidence.
acceptance_criteria:
  - The response identifies the family entrypoint and explains why direct specialist selection is premature.
  - The response returns a bounded intake or next step before making technical claims.
  - Any selected supporting skill has an explicit evidence dependency.
failure_signals:
  - Treating SEO as a single method.
  - Selecting a specialist without naming the decision shape.
  - Presenting unsupported findings as observations.
notes: Synthetic family-entry validation case for selective building-block composition.
---

## Input

## Observable criteria

- The response identifies the family entrypoint and explains why direct specialist selection is premature.
- The response returns a bounded intake or next step before making technical claims.
- Any selected supporting skill has an explicit evidence dependency.

## Failure signals

- Treating “SEO” as a single method.
- Selecting a specialist without naming the decision shape.
- Presenting unsupported findings as observations.

## Minimum evidence

- Authorized property scope;
- intended audience and important surfaces;
- current decision owner;
- available crawl, search, content, or query evidence.

## Human decisions preserved

- priority and investment;
- canonical representation and brand claims;
- permission to inspect or change a property;
- deployment and governance decisions.
