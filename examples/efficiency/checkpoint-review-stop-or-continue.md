# Checkpoint Review — Stop or Continue Example

Use `checkpoint-review` when a round is no longer obviously small and the next move should be chosen deliberately.

## What changed
One bounded slice has already been completed and validated.

## What is now proved
- the local objective for this round is met
- the current proof is enough for this slice

## What remains open
- broader expansion is still optional
- another round would need a fresh justification

## Decision
Stop this round and only continue if a real trigger appears.
