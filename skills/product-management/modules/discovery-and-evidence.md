# Discovery and evidence

Use this module when a product decision depends on claims that are unverified, contradictory, stale, or too weak to support commitment.

## Procedure

1. List the claims the decision depends on.
2. Classify each claim as observed, reported, inferred, estimated, or unknown.
3. Identify the smallest evidence needed to reduce the most consequential uncertainty.
4. Choose a discovery method that fits the claim, access, ethical limits, and decision horizon.
5. Define what would strengthen, weaken, or falsify the claim.
6. Synthesize evidence without collapsing disagreement or uncertainty.
7. Hand off to the decision owner with the remaining evidence gap visible.

## Minimum input

- decision or hypothesis
- claims to investigate
- available sources or access limits
- decision horizon

## Expected output

```yaml
product_discovery_plan:
  decision_supported: <...>
  claims:
    - claim: <...>
      status: observed | reported | inferred | estimated | unknown
      consequence_if_wrong: low | medium | high
  evidence_gap: <...>
  proposed_method: <...>
  sample_or_source_boundary: <...>
  strengthen_signal: [<...>]
  weaken_signal: [<...>]
  stop_condition: <...>
  limitations: [<...>]
```

## Verification

- The plan tests a claim instead of collecting information without a decision.
- The method matches the claim and available access.
- No customer, market, or behavior result is invented.
- The stop condition and interpretation limits are explicit.

## Handoff

- Strategic synthesis → `business-design`.
- Opportunity tree update → `opportunity-tree-alignment`.
- User experience or interaction investigation → `ux-strategy`.
- Evidence-backed feature judgment → `feature-value-governance`.

## Anti-patterns

- Treating a larger research sample as proof of a badly framed question.
- Calling stakeholder opinion user evidence.
- Writing findings before collecting or inspecting the declared evidence.
- Hiding contradictory signals in an averaged conclusion.
