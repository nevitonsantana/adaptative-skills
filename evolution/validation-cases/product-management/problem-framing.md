---
id: vc-product-management-problem-framing-001
skill_id: product-management
case_type: baseline
sensitivity: synthetic
source_policy: synthetic_only
input:
  task: "A stakeholder asks for a mobile dashboard because a competitor launched one, but no user problem, target user, or desired outcome is stated."
  context: "Synthetic case; no external source content is required."
expected_behavior:
  must_do:
    - "Activate problem framing before evaluating the requested solution."
    - "Separate the request from the problem, outcome, user, and available evidence."
    - "Hand off to feature planning only after a bounded problem and outcome exist."
  must_not_do:
    - "Invent customer demand, market impact, or competitive parity requirements."
    - "Select a prioritization method before the decision object and evidence are clear."
    - "Hand off to implementation as if the request were already validated."
acceptance_criteria:
  - "The response states that the feature request is not yet a sufficient problem statement."
  - "The response identifies missing user, outcome, context, and evidence inputs."
  - "The response does not recommend investment or create an implementation plan."
failure_signals:
  - "The response writes a roadmap item directly from the competitor request."
  - "The response treats stakeholder urgency as user evidence."
  - "The response claims the feature should be built."
---

# Problem framing case

## Must do

- Reframe the request as an unresolved product question.
- Ask for the smallest missing context needed to continue.
- Preserve the human decision about whether the problem deserves investigation.

## Must not do

- Do not invent customer demand, market impact, or competitive parity requirements.
- Do not select a prioritization method before the decision object and evidence are clear.
- Do not hand off to implementation as if the request were already validated.

## Observable evaluation

Pass when the response produces a short problem frame, lists explicit evidence gaps, and names the next safe handoff. Fail when it converts a solution request into an approved feature.

## Minimum evidence and human decisions

Minimum evidence is a stated user or business context plus a proposed outcome; the existence and importance of the problem remain human-owned decisions.
