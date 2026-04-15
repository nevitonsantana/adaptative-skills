---
observation_id: obs-2026-04-13-feature-planning-expansion-trigger-gap
skill_id: feature-planning
context: crisis-monitor-two-round-pilot
domain: engineering
date: 2026-04-13
modules_activated: Risk review
trigger_matches: a successful first slice still needed an explicit reason not to expand immediately
observed_issue_type: template-gap
evidence_refs: docs/crisis-monitor-case-study.md, docs/first-consumer-pilot.md
attribution_guess: the core skill remains sound, but a future template refinement may help teams record why expansion is deferred until a real trigger appears
result_mode: proposal-created
---

# Observation

## Summary
The Crisis Monitor case repeatedly reinforced the rule that expansion should happen only when a real trigger appears. The current feature-planning skill supports smallest-slice discipline, but the existing sidecar template does not make that decision legible enough.

## Why this attribution is plausible
This is not a reason to edit `Core Moves`. It suggests a possible template refinement so the output can record why the next slice is not yet justified.

## Why this result mode is valid
`proposal-created` is appropriate because the evidence points to a small sidecar opportunity, not a conceptual defect in the skill.

## Follow-up
Track whether this same gap appears in another project before promoting the proposal beyond a deferred state.
