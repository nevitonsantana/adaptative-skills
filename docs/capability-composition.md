---
title: Building blocks and capability families
description: Understand direct skill use, optional family entrypoints, and selective composition.
---

Adaptive Skills is a library of small, inspectable building blocks. A skill can be used
directly when the task is clear, or through a family entrypoint when the request is broad,
ambiguous, or composed.

## Two equivalent entry paths

### Direct building block

Use a known skill when its contract matches the task:

```text
"Review this page's indexability"
→ search-indexability-optimization
→ bounded findings and verification
```

### Family entrypoint

Use a family when the user knows the outcome but not the internal capability:

```text
"Improve our SEO"
→ AI Discovery & Agent Experience
→ diagnose the dominant uncertainty
→ select one primary building block
→ add supporting blocks only when evidence requires them
```

The family is a guided composition, not a replacement for its members.

## Selective composition

Families and skills must not load every descendant by default. New evidence may justify a
module or another skill during the work. Each activation should state its reason, expected
input, output, and verification. A rejected building block should be named when the choice
could otherwise be ambiguous.

## Boundaries

- A skill owns a bounded method and reviewable output.
- A module adds conditional depth inside a skill.
- A family or macro-capability describes a useful composition of building blocks.
- A harness owns tools, loading, authentication, execution, and logs.
- AletheIA owns macro intent, authorization, gates, and consequential decisions.

The family does not become an autonomous runtime, approve decisions, or change external
state. Advanced users may always bypass the family and invoke a canonical skill directly.

## When to choose each path

| Situation | Recommended path |
| --- | --- |
| One clear, bounded question | Direct building block |
| Unknown method or ambiguous goal | Family entrypoint |
| Several linked questions | Family entrypoint and selective composition |
| Known specialist contract | Direct building block |

See the [skill catalog](https://nevitonsantana.github.io/adaptive-skills/getting-started/skill-catalog/)
for direct discovery and the [capability model](https://nevitonsantana.github.io/adaptive-skills/capability-model/)
for the underlying composition model.
