---
title: "Domain Taxonomy"
description: "Reference documentation for Domain Taxonomy in Adaptive Skills."
---

## Portable skills

Portable skills live under `skills/` and are designed to work across products with little or no project-specific adaptation.

Current portable domains:
- business
- cross-functional
- design
- docs
- efficiency
- engineering
- governance
- metrics
- planning
- product
- quality

## Domain packs

Domain packs live under `domain-packs/`.

They are explicitly domain-specific and should stay separate from the portable library.

Current packs:
- `crisis-management`
- `ai-discovery-agent-experience` — experimental five-skill v0.1 domain pack for
  representation, search foundations, measurement, generative visibility, and agent actions

## Decision rule

A skill belongs in the portable library only if it can be used in another project without inheriting local operating rules or domain-specific vocabulary.

If the skill depends on a specific product worldview, vocabulary, or context model, it should be a domain pack.

The portable `product-management` skill is a modular entry point inside the `product` domain. Its modules and framework references extend one contract; they do not create separate domains or independent skills by default.

`generic` remains an internal metadata and governance term. Public guidance uses `portable` to emphasize reuse, inspectability, and cross-domain applicability rather than simplicity or limited capability.
