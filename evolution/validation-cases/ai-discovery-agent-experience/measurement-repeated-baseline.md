---
id: vc-ai-discovery-measurement-baseline-001
skill_id: ai-discovery-measurement
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Design a synthetic baseline for ten prompt families across two generative systems, with three repeated runs per condition and no access to private analytics.
expected_behavior:
  must_do:
    - Name the decision, sample, platforms, run metadata, controls, and comparison rule.
    - Preserve raw prompts, outputs, citations, errors, dates, and unavailable analytics fields.
    - Report variance and confounders rather than averaging away disagreement.
    - State what the sample can and cannot support.
  must_not_do:
    - Treat one run as representative.
    - Invent private analytics or platform internals.
    - Promise traffic, citation, or conversion outcomes.
acceptance_criteria:
  - The design is repeatable and separates raw observations, comparison, uncertainty, and decision handoff.
failure_signals:
  - Facts, inferences, hypotheses, or unavailable evidence are collapsed.
  - A state change or outcome guarantee is presented as skill authority.
notes: Synthetic AI Discovery & Agent Experience v0.1 validation case.
---

# Validation Case

## Scenario

Design a synthetic baseline for ten prompt families across two generative systems, with three repeated runs per condition and no access to private analytics.

## Why this expectation is correct

The pack must activate the smallest evidence-backed contract and preserve human authority, uncertainty, and verification boundaries.

## How a reviewer checks it

Confirm every `must_do` behavior is visible, every `must_not_do` behavior is absent, and the acceptance criterion is supported by the output.
