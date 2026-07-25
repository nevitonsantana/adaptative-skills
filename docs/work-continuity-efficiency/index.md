---
title: Work Continuity & Efficiency
description: Use optional continuity guidance to make work smaller, resumable, reviewable, and clear to hand off.
---

Work Continuity & Efficiency is an optional family entrypoint over four existing building
blocks. Use it when the outcome is continuity, not when you already know the exact skill.

## Choose the entry path

- Clear oversized task → use `task-chunking` directly.
- Unclear whether to continue or stop → use `checkpoint-review` directly.
- Another operator must resume → use `handoff-summary` directly.
- A status, decision, failure, or handoff needs clarity → use `communication` directly.
- Several of these needs are connected → start with the family entrypoint.

The family selects a primary building block and only adds supporting blocks when their output
is necessary. It does not track work, schedule agents, persist state, or make governance
decisions.

## Typical composition

```text
Oversized initiative
→ task-chunking
→ smallest useful slice and stop condition
→ handoff-summary
→ verified context for the next round
```

If the current round has meaningful proof or uncertainty, add `checkpoint-review`. Use
`communication` when the result needs to be presented clearly to another owner.

The canonical [skill contract](https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/work-continuity-efficiency/SKILL.md)
remains the source of authority.
