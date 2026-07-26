---
observation_id: obs-2026-07-25-ai-discovery-family-routing
skill_id: ai-discovery-agent-experience
context: cross-family-routing-recovery-contract-review
domain: ai-discovery-agent-experience
date: 2026-07-25
modules_activated: Goal framing, dominant-question classification, selective composition
action_triggers: broad SEO request; unavailable property scope and evidence
trigger_matches: broad SEO must start with family intake, while direct indexability work requires authorized property scope and technical evidence
observed_issue_type: routing-and-evidence-boundary
evidence_refs: domain-packs/ai-discovery-agent-experience/skills/ai-discovery-agent-experience/SKILL.md, domain-packs/ai-discovery-agent-experience/skills/search-indexability-optimization/SKILL.md, evolution/validation-cases/ai-discovery-agent-experience/family-agnostic-seo-request.md, evolution/validation-cases/ai-discovery-agent-experience/search-foundations.md
attribution_guess: the existing family and specialist contracts correctly distinguish broad intake from direct use and block unsupported indexability claims
result_mode: reinforced
---

# Observation

## Summary

Synthetic routing tests confirmed that a broad SEO request starts at the optional AI Discovery
family, while a clear indexability question can use the specialist directly only after property
scope and authorized technical evidence are available.

## Why this attribution is plausible

The observed behavior follows the family contract's selective-composition rule and the
indexability contract's explicit evidence boundary. No extra router or specialist was needed.

## Why this result mode is valid

`reinforced` is appropriate: the test found no contract gap and did not establish runtime
behavior or real search outcomes.

## Follow-up

Collect real routed requests before proposing a trigger, family, or skill change.
