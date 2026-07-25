---
id: vc-product-management-discovery-gap-001
skill_id: product-management
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "A team has six interview summaries, but the participants were selected from one enterprise account and none of the notes distinguish observed behavior from interpretation."
  context: "Synthetic case; no external source content is required."
expected_behavior:
  must_do:
    - "Classify the evidence as narrow and partly uninterpreted."
    - "Separate observations, interpretations, assumptions, and unknowns."
    - "Recommend a bounded evidence gap or follow-up rather than claiming broad demand."
  must_not_do:
    - "Generalize the account interviews to the whole market."
    - "Present interpretations as observed facts."
    - "Use a score or percentage not present in the input."
acceptance_criteria:
  - "The response names sample and interpretation limitations."
  - "The response preserves uncertainty in any product conclusion."
  - "The response identifies what additional evidence would change the decision."
failure_signals:
  - "The response generalizes the account's interviews to the whole market."
  - "The response presents interpretations as observed facts."
  - "The response uses a score or percentage not present in the input."
---

# Discovery evidence case

## Must do

- Label the source as a narrow evidence sample.
- Extract observations separately from interpretations and assumptions.
- State a concrete follow-up question or evidence-gathering step.

## Must not do

- Do not fabricate prevalence, market size, or confidence.
- Do not treat an interview summary as a validated outcome metric.
- Do not hide the account-selection bias.

## Observable evaluation

Pass when the output contains an evidence ledger and a decision-relevant gap. Fail when it makes a broad product recommendation from the sample alone.

## Minimum evidence and human decisions

Minimum evidence is traceable access to the interview notes and their selection context; humans decide whether the evidence threshold is sufficient for investment or further discovery.
