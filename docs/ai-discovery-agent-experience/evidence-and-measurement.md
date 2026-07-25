---
title: Evidence and measurement for AI Discovery
description: The shared finding contract and a repeatable path from raw observation to bounded recommendation.
---


A finding is useful only when another reviewer can see what was observed, what was interpreted, and how to verify the next decision.

## Shared finding contract

Every material finding exposes:

- skill, module, target, and finding type;
- source, observation method, date, and raw observation;
- confidence and unavailable evidence;
- fact, inference, and hypothesis as separate fields;
- impact, recommendation, verification, and handoff.

The eight pack templates are optional accelerators. Each `SKILL.md` remains executable by itself.

## Build a baseline

1. Name the decision and observation dimensions.
2. Define a bounded sample: queries or tasks, properties, platforms, models or interfaces, locales, dates, and run count.
3. Capture raw records before summarizing.
4. Record variance, errors, confounders, and unavailable fields.
5. Compare only equivalent conditions; otherwise report a directional observation, not a before/after result.
6. State what the evidence cannot prove.

## Interpretation example

- **Fact:** three recorded runs returned no source citation.
- **Inference:** citation coverage was absent in this sample.
- **Hypothesis:** clearer source-backed passages might improve extractability.
- **Not supported:** “the platform never uses the source” or “the change will earn citations.”

## Recovery

If repeatability fails, shrink the question, stabilize metadata, and run again. If evidence access fails, preserve the study design and mark the baseline blocked rather than manufacturing observations.
