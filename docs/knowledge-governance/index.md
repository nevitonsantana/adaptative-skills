---
title: Knowledge Governance
description: Select the right building block for evaluating, reconciling, and safely using knowledge sources.
---

Knowledge Governance is an optional family entrypoint over three existing governance building
blocks. It helps users state a source-governance outcome without needing to know which specialist
check comes first.

## Choose the entry path

- New source or framework → use `knowledge-source-evaluation` directly.
- Conflicting sources → use `knowledge-conflict-resolution` directly.
- Sensitive or cross-boundary source → use `restricted-context-check` directly.
- Several concerns are connected → start with the family entrypoint.

The family selects a primary building block and adds supporting checks only when their output is
needed. It never registers a source, grants access, exposes restricted content, or replaces
AletheIA knowledge governance.

## Typical composition

```text
Proposed client source
→ knowledge-source-evaluation
→ restricted-context-check
→ knowledge-conflict-resolution if a decision-relevant conflict is confirmed
```

Unknown ownership, provenance, sensitivity, or authorization remain blockers rather than being
inferred. The canonical [skill contract](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/knowledge-governance/SKILL.md)
is the source of authority.
