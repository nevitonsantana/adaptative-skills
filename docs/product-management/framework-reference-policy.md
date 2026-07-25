---
title: Product Management framework reference policy
description: Learn how Product Management uses external methods without turning them into copied or authoritative contracts.
---

Frameworks are methods that can support a decision. They are not independent skills and they do not make a decision on behalf of the product owner.

Each local method profile records:

- the decision shape it supports;
- when it is useful and when it is invalid;
- minimum inputs and evidence requirements;
- failure modes and human decisions;
- provenance links to the source used for the independent synthesis.

## Method selection rules

- Choose a method after classifying the decision and evidence quality.
- Prefer one primary method and, at most, one meaningful alternative.
- Reject numeric precision when required inputs are estimates or missing.
- Keep strategic dependencies, overrides, and trade-offs visible rather than hiding them in a score.
- Treat a score as decision support, not approval.

The initial profiles cover RICE, ICE, value versus effort, Cost of Delay, Kano, opportunity scoring, and outcome-oriented measurement. See the canonical references under [`skills/product-management/references/`](https://github.com/nevitonsantana/adaptive-skills/tree/main/skills/product-management/references/).

## Provenance and licensing

The repository uses independent wording and links to public source material. It does not copy incompatible repository content into the Apache-2.0 core. Source links currently include [Intercom's RICE explanation](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/), [Atlassian's prioritization overview](https://www.atlassian.com/agile/product-management/prioritization-framework), [Kano Model](https://kanomodel.com/discovering-the-kano-model/), [ASQ's Kano overview](https://asq.org/quality-resources/kano-model), [Savio's ICE overview](https://www.savio.io/product-roadmap/ice-scoring-model/), and [Strategyn's opportunity scoring explanation](https://strategyn.com/2015/10/09/what-is-opportunity-scoring/).

External references inform method profiles; the canonical `SKILL.md` controls how the skill behaves. If a source is unavailable, conflicting, restricted, or insufficient for the decision, the output must say so.
