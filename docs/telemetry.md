# Recommended Telemetry

This repository does not implement runtime telemetry.
It documents a recommended shape so projects can evolve skills intentionally instead of by anecdote.

## Recommended fields

- `skill_id`
- `domain`
- `modules_activated`
- `trigger_matches`
- `result`
- `handoff_required`
- `failure_type`
- `improvement_note`

## Reading guidance

Track telemetry only when it supports:
- skill improvement
- better projection defaults
- clearer handoff points
- evidence that a module should be promoted, changed, or removed

Do not instrument for vanity.
