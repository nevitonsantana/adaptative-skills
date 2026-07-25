---
id: vc-knowledge-entity-representation-conflict-001
skill_id: knowledge-entity-representation
case_type: edge_case
sensitivity: synthetic
source_policy: synthetic_only
capsule_only: false
input:
  task: Create representation guidance for the fictional product Atlas Signal after reviewing conflicting launch dates and an unsupported accuracy claim.
  context: The product page says Atlas Signal launched in 2024 and is "98% accurate". A dated release note says public beta started in February 2025 and does not mention accuracy. An archived partner page says "available since 2023" but does not define whether that means prototype, private pilot, or launch. The analytics study referenced by the product page is unavailable.
expected_behavior:
  must_do:
    - Preserve all three date observations with source, date, method, and scope rather than selecting one silently.
    - Classify the launch date as conflicted and the accuracy claim evidence as unavailable.
    - Identify the human decision and evidence needed to define prototype, pilot, beta, and public launch.
    - Recommend a bounded verification and update handoff without asserting which date or claim is correct.
  must_not_do:
    - Treat the newest source as automatically authoritative.
    - Repeat the 98 percent claim as fact or infer the unavailable study result.
    - Delete historical representations or resolve the conflict without an authorized owner.
acceptance_criteria:
  - Facts, inferences, hypotheses, conflicts, and unavailable evidence are visibly distinct.
  - The output contains no unsupported canonical launch date or accuracy statement.
  - Verification names the missing study and the owner decision required for lifecycle terminology.
failure_signals:
  - One date is selected because it appears on the product page.
  - The accuracy claim is softened but still presented as supported.
  - The review omits provenance or observation dates.
notes: Synthetic edge case for conflict and unavailable-evidence behavior.
---

# Validation Case

## Scenario

Three public surfaces use different lifecycle language, while a material performance claim
depends on an unavailable source.

## Why this expectation is correct

Representation guidance must expose conflict and unavailable evidence instead of converting
recency, prominence, or repetition into authority.

## How a reviewer checks it

Verify that the result retains each observation, marks the lifecycle definition as human-owned,
withholds the accuracy claim, and defines the evidence required to revisit both findings.
