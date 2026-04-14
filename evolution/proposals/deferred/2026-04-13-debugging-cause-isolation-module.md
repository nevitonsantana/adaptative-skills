---
proposal_id: prop-2026-04-13-debugging-cause-isolation-module
skill_id: debugging
source_observations: obs-2026-04-13-debugging-cause-isolation-seed
target_surface: Optional Modules
change_type: module-candidate
automation_level: governed-autoevolution
status: deferred
rationale: a cause-isolation module could help reduce fix-by-guess behavior, but the evidence is still seed-level and not enough for canonical writeback
global_consistency_risk: medium
---

# Proposal

## Proposed change
Add an optional module focused on narrowing the failure surface before jumping to a fix.

## Why now
The need is plausible but not yet field-proven across multiple cases.

## Why the target surface is appropriate
A contextual module is safer than touching `Core Moves` or changing the skill boundary.

## Why this is not just local residue
The pattern could recur across engineering work, but current evidence does not yet justify a canon update.

## Decision notes
Deferred until a second real observation supports the same gap.
