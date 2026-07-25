---
title: Capability family audit
description: Identify coherent family entrypoints without replacing direct building-block use.
---

This audit reviews the current portable skill inventory for user-facing families. A category
is not a family by itself. A family is justified only when it offers a recognizable entry
question, a small set of reusable building blocks, a bounded composition, and a useful gain
for users or agents.

## Decision vocabulary

- **Established** — family entrypoint exists and has a validated composition contract.
- **Pilot candidate** — the building blocks and entry question are sufficiently coherent for
  a focused contract pilot.
- **Needs framing** — related skills exist, but the family boundary or primary outcome is not
  yet clear.
- **Direct use** — individual building blocks are clearer than a family at current maturity.
- **Hold** — do not create a family until usage evidence or ownership boundaries improve.

## Inventory

| Candidate family | Entry question | Building blocks | Decision | Reason |
| --- | --- | --- | --- | --- |
| Product Management | “What product decision are we trying to make?” | `product-management`, `feature-value-governance`, `opportunity-tree-alignment`, `feature-planning`, `observability-review`, `triad-check` | Established | Existing entry contract and validated modular workflow. |
| AI Discovery & Agent Experience | “What prevents this property from being discovered, represented, measured, or safely used?” | Family entrypoint plus five domain-pack specialists | Established | Existing family entrypoint and selective composition contract. |
| Work Continuity & Efficiency | “How do we make this work smaller, resumable, and safe to hand off?” | `task-chunking`, `checkpoint-review`, `handoff-summary`, `communication` | Pilot candidate | Clear outcome and small building-block set; good next pilot. |
| Experience Design | “What experience decision needs to become clearer or safer?” | `ux-strategy`, `ux-provocation`, `heuristic-audit`, `ux-writing`, `design-system-intelligence` | Needs framing | Strong members, but strategy, critique, writing, and system review are different entry questions. |
| Knowledge Governance | “Can this knowledge be trusted, reconciled, and used within its boundary?” | `knowledge-source-evaluation`, `knowledge-conflict-resolution`, `restricted-context-check`, `domain-language-alignment` | Pilot candidate | Coherent evidence and boundary problem, but ownership and source scope need a focused pilot. |
| Engineering Delivery | “What is the smallest safe path from change intent to proven implementation?” | `workflow`, `feature-planning`, `testing`, `debugging`, `lean-implementation`, `architecture-review`, `api-design`, `refactoring`, `code-style` | Needs framing | Broad lifecycle family risks becoming a second workflow runtime. Start with a narrower delivery question. |
| Business & Value | “How does this initiative create or protect value?” | `business-design`, `revenue-lever-mapping`, Product Management value skills | Hold | Significant overlap with Product Management and unresolved decision ownership. |
| Quality & Observability | “What evidence shows the system or outcome is healthy?” | `qa-review`, `observability-review`, `testing` | Hold | Quality, testing, and metrics cross several existing families. |
| Crisis Response | “How should a high-impact incident be understood, monitored, communicated, and coordinated?” | `crisis-analyst`, `monitoring-architect`, `cris-voice`, crisis companion skills | Needs framing | Strong domain workflow exists, but requires explicit crisis entry contract and authority boundaries. |
| Planning & Intent | “What must be clarified or stress-tested before work begins?” | `intent-clarification`, `premortem`, `workflow` | Direct use | Small, cross-cutting building blocks are clearer than a new family. |
| Documentation | “How do we create a self-service document for this reader and task?” | `documentation` and its internal modules | Direct use | The skill already provides the appropriate primary entrypoint. |

## Recommended sequence

1. Pilot **Work Continuity & Efficiency** with a small family entry contract.
2. Pilot **Knowledge Governance** only after defining source ownership and restricted-context
   boundaries.
3. Frame Experience Design around one entry question before composing its members.
4. Keep Business & Value and Quality & Observability on hold until their overlaps are resolved.
5. Revisit Engineering Delivery and Crisis Response as dedicated workflows, not automatically
   as broad families.

## Family creation gate

Before creating a new family, require:

- one outcome-oriented entry question;
- at least two building blocks with independent direct-use contracts;
- a selective composition path, not an all-members checklist;
- explicit exclusions and authority boundaries;
- at least one synthetic case for direct use and one for family-led composition;
- a verification result and named handoff;
- evidence that the family reduces user or agent routing ambiguity.

Until these conditions are met, keep the skills discoverable and usable directly in the catalog.
