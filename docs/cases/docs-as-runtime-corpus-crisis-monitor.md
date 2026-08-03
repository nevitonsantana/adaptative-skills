---
title: Docs as runtime corpus — Crisis Monitor
description: Field case for documentation that serves both users and an assistant through a governed runtime corpus.
---

## Evidence label

**Field case.** This record summarizes a real documentation pilot in Crisis Monitor. It is evidence for a bounded pattern, not proof that every documentation system needs a runtime corpus.

## Why this case matters

Crisis Monitor used the `documentation` skill in a documentation project with two consumers:

- users reading a public Blume knowledge base;
- Cris, an assistant that must answer only from approved user-facing documentation.

That made the work stricter than ordinary publishing. The docs had to remain understandable to people, while also becoming a safe, traceable corpus for runtime use.

## Pattern observed

```text
private governed source
→ clean public export
→ static reader and agent artifacts
→ versioned assistant snapshot
→ focused runtime validation
```

The important design choice was separation of knowledge:

| Surface | Audience | Boundary |
|---|---|---|
| Private docs source | Maintainer and agents | Holds governance evidence and publication scripts. |
| Public Blume site | Users and Cris knowledge base readers | Contains only user-facing guidance. |
| Versioned snapshot | Cris backend runtime | Contains approved pages, paths, titles, Markdown, source commit, generated date, and hash. |
| Technical docs | Developer and internal agents | Stay out of the user corpus and out of the assistant snapshot. |

## Skill behavior that helped

The `documentation` skill was useful because it already pushed the work toward:

- reader maps for novice, practitioner, advanced, and maintainer readers;
- one primary Diátaxis purpose per page;
- a ledger of sources and exclusions;
- progressive journeys from orientation to recurring tasks, recovery, concepts, and reference;
- publication QA instead of treating a static build as sufficient proof.

## What needed to be added to the skill

The case exposed a reusable documentation concern: **docs as runtime corpus**.

When documentation feeds an assistant or retrieval layer, the author must also define:

- which corpus is approved for runtime use;
- which sources are excluded even if useful to maintainers;
- what provenance and freshness metadata the runtime receives;
- what happens when the corpus is missing, stale, invalid, or incompatible;
- how negative tests prove that technical content does not leak;
- how smoke tests prove that the published artifacts remain reachable.

## Validation evidence from the case

The Crisis Monitor pilot used proportional validation rather than one generic proof:

| Validation | Purpose |
|---|---|
| User-corpus validation | Block technical docs, environment variables, architecture, decisions, runbooks, and policies from the user corpus. |
| Blume validation and build | Prove the public documentation renders and links resolve. |
| Rendered-heading validation | Prevent duplicate H1 regressions from frontmatter plus body headings. |
| Public export validation | Prove the public repo excludes private governance overlays and technical material. |
| Cris snapshot validation | Prove the backend snapshot is structured, hashed, and fresh relative to the approved corpus. |
| Live smoke by manifest | Prove public routes, `llms*`, raw Markdown, and agent-readable artifacts are reachable. |
| Negative runtime tests | Prove Cris does not answer from APIs, env vars, architecture, or technical operations docs. |

Final live evidence recorded in the consumer project:

- `https://crisis-monitor.github.io/PUBLIC_EXPORT_MANIFEST.json` returned HTTP 200;
- the live manifest contained 15 routes, 15 raw Markdown endpoints, and 3 base artifacts;
- the public smoke ran with `manifestDriven: true`, 15 routes, 18 artifacts, and 0 failures.

## What the case did not prove

This case does not prove that:

- every docs site needs a runtime snapshot;
- static `llms*` artifacts are enough for assistant safety;
- Ask AI or MCP should be activated by default;
- manifest smoke replaces editorial review;
- Adaptive Skills should own a consumer project's runtime policy.

## Reusable heuristic

Use the `docs as runtime corpus` module only when at least one of these is true:

- documentation is exported into a snapshot, embedding set, retrieval index, or assistant knowledge base;
- documentation creates public `llms*`, raw Markdown, or manifest artifacts meant for agents;
- a user-facing assistant must refuse or fail safely when documentation is unavailable;
- internal technical sources are useful to maintainers but unsafe for user-facing answers.

If none of these are true, ordinary publication QA is usually enough.

## Related source evidence

- Crisis Monitor closeout: `Crisis-Monitor/Crisis-Monitor` — `ops/ai/reports/2026-08-03-governed-docs-pilot-closeout.md`.
- Public documentation: [Crisis Monitor Docs](https://crisis-monitor.github.io/).
- Public manifest: [PUBLIC_EXPORT_MANIFEST.json](https://crisis-monitor.github.io/PUBLIC_EXPORT_MANIFEST.json).
- Earlier field case: [Crisis Monitor case study](https://nevitonsantana.github.io/adaptive-skills/crisis-monitor-case-study/).

## How to apply this case safely

1. Start with the human reader journey.
2. Add runtime-corpus constraints only if an assistant or retrieval consumer exists.
3. Keep private/governance sources separate from user-facing sources.
4. Version the runtime corpus instead of pulling private GitHub content at runtime.
5. Add negative tests for restricted content.
6. Smoke the published artifacts that agents or runtimes are expected to read.
