---
title: AI Discovery workflows
description: Evidence-gated compositions for launch review, generative visibility, and agent action readiness.
---


Compositions are consultative routes, not an execution engine. Skip any step whose output is not needed.

## Pre-launch review

1. **Represent:** stabilize people, brands, methods, offerings, claims, and authoritative sources.
2. **Inspect search foundations:** evaluate intended access, indexability, canonical signals, architecture, and structured representation.
3. **Design measurement:** define the sample, raw records, metadata, variance, and comparison rule.
4. **Review generative visibility:** only after repeated observations exist, compare source presence, citations, extraction, and fidelity.
5. **Handoff:** assign each proposed change and recheck to an owner.

Stop when an entity decision, access permission, publication approval, or comparable baseline is missing.

## Generative visibility review

Use `ai-discovery-measurement` before `generative-visibility-optimization`. Preserve prompts, outputs, citations, run context, and unavailable fields. A missing citation is an observation, not proof that a source cannot be retrieved.

## Agent action readiness

Use `agent-capability-actionability` to define the user task and control contract. Pair it with `ai-discovery-measurement` to observe task completion, errors, confirmation, side effects, and recovery. Do not introduce MCP, A2A, WebMCP, or OpenAPI unless the task and existing interfaces justify them.

## Useful dependencies only

The capability overlay represents four relationships: entity representation informs search; search informs generative visibility; measurement informs generative visibility; actionability informs measurement. These links do not activate skills automatically.
