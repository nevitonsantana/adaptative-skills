---
id: vc-search-indexability-foundations-001
skill_id: search-indexability-optimization
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Review a fictional site migration where product URLs return 200, old URLs redirect inconsistently, filtered duplicates expose conflicting canonicals, and the new collection is absent from navigation.
expected_behavior:
  must_do:
    - Bound the property, environments, important surfaces, and intended indexability.
    - Preserve the response, redirect, canonical, and navigation observations as separate evidence.
    - Classify blockers, degradations, hypotheses, unavailable index-state evidence, and verification owners.
    - Distinguish crawl access and technical eligibility from actual indexing, ranking, traffic, or value.
  must_not_do:
    - Claim that a 200 response proves indexing.
    - Guarantee canonical selection or rankings.
    - Change redirects, canonicals, navigation, or structured data.
acceptance_criteria:
  - The output prioritizes source-backed technical findings and a repeatable recheck without inventing webmaster evidence.
failure_signals:
  - Facts, inferences, hypotheses, or unavailable evidence are collapsed.
  - A state change or outcome guarantee is presented as skill authority.
notes: Synthetic AI Discovery & Agent Experience v0.1 validation case.
---

# Validation Case

## Scenario

Review a fictional site migration where product URLs return 200, old URLs redirect inconsistently, filtered duplicates expose conflicting canonicals, and the new collection is absent from navigation.

## Why this expectation is correct

The pack must activate the smallest evidence-backed contract and preserve human authority, uncertainty, and verification boundaries.

## How a reviewer checks it

Confirm every `must_do` behavior is visible, every `must_not_do` behavior is absent, and the acceptance criterion is supported by the output.
