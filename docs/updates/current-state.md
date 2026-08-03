---
title: Current state
description: See the currently published Adaptive Skills inventory, supporting metadata, and maturity boundaries.
---

This page describes the repository state represented by current documentation and validation gates. Canonical files and automated validators take precedence if this summary drifts.

## Published capability surface

- **38 portable skills** under `skills/*/SKILL.md`.
- **9 domain-pack skills** across the crisis-management pack and the experimental
  AI Discovery & Agent Experience v0.1 pack.
- Portable skills remain the reusable public capability library.
- Domain-pack skills remain validation cases rather than part of the portable inventory.
- `documentation` is the portable `docs` skill for source-backed self-service journeys across novice, practitioner, advanced, and maintainer readers.
- `product-management` is the portable `product` entry point for modular, evidence-aware product decisions; its first release includes problem framing, discovery and evidence, prioritization and method selection, and metrics and outcomes.
- The AI Discovery pack now includes an optional family entrypoint plus five specialist
  building blocks for entity representation, search foundations, measurement, generative
  visibility, and agent actionability.

See the [complete skills catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/) for task triggers and expected outcomes.

Detailed public profiles are available for all 38 portable skills. Each profile is generated from its canonical `SKILL.md` contract and adds reader-facing orientation without creating a second source of authority.

## Supporting metadata

The repository validates capability metadata, per-skill harness requirements where declared, governed knowledge dependencies, evolution records, and projection consistency.

These layers support discovery, compatibility, and governance. They do not replace canonical skill instructions or create an autonomous runtime.

## Consumption and AletheIA

Adaptive Skills can be consumed independently through a compatible harness. AletheIA integration remains optional:

- AletheIA owns macro Work Slice governance.
- Adaptive Skills owns reusable micro-execution methods.
- Consumer harnesses own local loading and runtime mechanics.

The verified APM path uses the immutable `v0.1.2` tag: Claude Code materializes skills under `.claude/skills/`, while Codex and GitHub Copilot materialize them under `.agents/skills/`. These smoke tests used APM 0.26.0 and confirmed all 38 portable skills plus `apm compile --validate`. APM consumer projects do not expose the package manifest's convenience scripts through `apm run`.

## Documentation state

The public Blume site provides progressive paths for beginners, practitioners, advanced readers, and maintainers. Manual GitHub Pages publication remains the current release process.

The canonical `documentation` skill uses five durable Core Moves and context-triggered modules for reader journeys, information architecture, technical storytelling, controlled procedural clarity, editorial governance, change documentation, publication QA, and docs-as-runtime-corpus cases. A reusable checklist and field evidence from Crisis Monitor cover multi-level onboarding, executable procedures, mixed-corpus audits, snapshots, manifests, raw Markdown, `llms*` artifacts, and assistant-safe negative checks.

The complete skill reference uses stable `/skills/<name>/` routes, canonical metadata projection, complete contract rendering, and direct access to usage boundaries, outputs, verification, and handoff guidance. Registry validation now requires every canonical portable skill to have a public profile.

The public [Product Management guide](https://nevitonsantana.github.io/adaptive-skills/product-management/) explains the lifecycle, module selection, framework provenance, and bounded composition examples without duplicating the canonical contract.

The public [AI Discovery & Agent Experience guide](https://nevitonsantana.github.io/adaptive-skills/ai-discovery-agent-experience/) provides skill selection, evidence-gated workflows, measurement guidance, and a bounded MoradaHarmoniA pilot scaffold without adding the domain skills to the portable catalog.
The [building blocks and capability families guide](https://nevitonsantana.github.io/adaptive-skills/capability-composition/) documents direct skill use and optional family-led composition.
The [capability family audit](https://nevitonsantana.github.io/adaptive-skills/family-audit/) records which additional families are ready for a pilot and which should remain direct-use or on hold.
The Work Continuity & Efficiency family provides an optional entrypoint for chunking,
checkpoint, handoff, and communication needs. Crisis Response remains Crisis Monitor-specific
scope and is not part of the general-purpose family inventory.
Public documentation uses **portable skills** as the reader-facing label for the cross-domain library. The internal `generic` metadata and governance term remains unchanged. Rendered documentation validation now checks H1 tags with attributes and all published pages for exactly one visible H1.

## Maturity boundaries

Current documentation does not claim autonomous orchestration, automatic routing authority, universal effectiveness from pilots, automatic promotion from observation, formal ASD-STE100 compliance, elimination of all support dependency, or an AletheIA dependency.

The AI Discovery pack also does not claim a completed MoradaHarmoniA baseline,
search ranking, citation, traffic, conversion, or agent adoption outcome.

## How to verify

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_capabilities.py
python3 scripts/validate_harness_requirements.py
python3 scripts/validate_knowledge_deps.py
python3 scripts/validate_evolution.py
pnpm run docs:validate
```

## Next steps

- Browse [Cases and evidence](https://nevitonsantana.github.io/adaptive-skills/cases/) for bounded maturity records.
- Read [Changelog](https://nevitonsantana.github.io/adaptive-skills/updates/changelog/) for consumer-facing changes.
- Read [Updates and evolution](https://nevitonsantana.github.io/adaptive-skills/updates/) before interpreting roadmap material.

Knowledge Governance provides an optional entrypoint for source evaluation, conflict resolution, and restricted-context checks.

Experience Design provides an optional entrypoint for strategy, hypothesis pressure-testing, usability audit, UX writing, and design-system review.
