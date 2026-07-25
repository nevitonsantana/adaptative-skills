---
name: agent-capability-actionability
description: Evaluate whether an agent can discover, understand, request, execute, confirm, and recover from a meaningful user-owned action with explicit authority and side-effect boundaries.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this skill only when an agent needs to do more than retrieve information. It maps a
user-owned task to capability, precondition, input, output, authorization, confirmation,
side effect, error, recovery, and audit boundaries before any interface or protocol is built.

The skill is read-only and consultative. It cannot authorize an agent, execute a transaction,
send data, create an obligation, expose a tool, or select a protocol without human ownership.

# When to Use

- An agent may schedule, submit, buy, update, cancel, request, compare-and-act, or otherwise
  change state.
- A human interface may need to support browser agents safely.
- A backend capability may be exposed through a tool, API, or protocol.
- Authorization, consent, sensitive data, reversibility, idempotency, or recovery matters.
- Agent-task success needs a defined contract before implementation or measurement.

# When NOT to Use

- The task is only search, retrieval, citation, summarization, or representation.
- No concrete user-owned action, consumer, or authority boundary exists.
- The requester wants immediate protocol implementation or production automation.
- The action is prohibited, unowned, or cannot be verified safely.

# Core Moves

1. **Define the user-owned task.** Name the user goal, agent role, allowed action, decision owner,
   preconditions, exclusions, and required human control.
2. **Model the capability contract.** Define inputs, constraints, outputs, states, errors, side
   effects, confirmation, idempotency, cancellation, and reversibility.
3. **Inspect available interfaces.** Evaluate the human interface and any authorized machine
   interface without assuming a new protocol is required.
4. **Review control and recovery.** Identify authorization, consent, data, security, trust,
   observability, partial completion, retry, rollback, revocation, and escalation gaps.
5. **Recommend the smallest exposure path.** Compare no exposure, human-interface improvement,
   browser-local tooling, or backend capability exposure and define verification without building it.

# Optional Modules

- **Agent capability inventory** — Map meaningful actions, inputs, side effects, owners, and
  preconditions rather than UI controls.
- **Task contract review** — Define task intent, parameters, constraints, result, confirmation,
  state, and error semantics.
- **Human-interface actionability** — Review forms, labels, state, policies, confirmations, and
  recovery for people and browser agents.
- **Browser-local tool readiness** — Assess whether browser-local capability exposure adds value
  relative to accessible UI or backend integration.
- **Backend tool and API readiness** — Assess schemas, authorization, errors, observability,
  stability, and consumer needs.
- **Agent-to-agent readiness** — Assess a discoverable agent-to-agent contract only when
  collaboration goes beyond tool invocation.
- **Agentic commerce readiness** — Review catalog, availability, price, policy, checkout,
  authorization, payment, confirmation, and post-purchase behavior.
- **Authorization and consent review** — Review delegated authority, scope, expiry, sensitive data,
  confirmation, audit, and revocation.
- **Failure and recovery review** — Review idempotency, retry, rollback, cancellation, partial
  completion, compensation, and human escalation.

# Activation Triggers

- Activate **agent capability inventory** when the agent must do more than retrieve information.
- Activate **task contract review** when a capability may become a form action, tool, API, or
  automated flow.
- Activate **human-interface actionability** when no dedicated machine interface exists.
- Activate **browser-local tool readiness** when shared live-page state is material.
- Activate **backend tool and API readiness** when a direct backend consumer is named.
- Activate **agent-to-agent readiness** only for a concrete autonomous service collaboration.
- Activate **agentic commerce readiness** when purchase or financial commitment is in scope.
- Activate **authorization and consent review** for sensitive data, state change, resource
  commitment, communication, or obligation.
- Activate **failure and recovery review** whenever failure can produce meaningful side effects.

# Expected Output

```yaml
agent_actionability_review:
  task:
    user_goal:
    agent_role:
    allowed_action:
    owner:
    preconditions: []
    prohibited_or_out_of_scope: []
  capability:
    inputs: []
    constraints: []
    outputs: []
    states: []
    errors: []
    side_effects: []
    confirmation:
    idempotency:
    cancellation:
    recovery:
  control:
    authorization:
    consent:
    sensitive_data: []
    audit:
    revocation:
  findings:
    - finding_id:
      skill: agent-capability-actionability
      module:
      target:
      finding_type: blocker | degradation | risk | opportunity | unknown
      evidence:
        source:
        observed_at:
        method:
        raw_observation:
      confidence: high | medium | low | unavailable
      fact:
      inference:
      hypothesis:
      impact:
      recommendation:
      verification:
      handoff:
  exposure_recommendation:
    smallest_path: no_exposure | improve_human_interface | browser_local | backend_capability
    rejected_paths: []
    implementation_owner:
  limitations: []
```

# Verification

- A concrete user-owned task and authorized decision owner exist.
- Retrieval-only behavior is not mislabeled as an action capability.
- Preconditions, inputs, constraints, outputs, states, errors, and side effects are explicit.
- Authority, consent, sensitive data, confirmation, audit, expiry, and revocation are addressed.
- Retry, idempotency, partial completion, cancellation, rollback or compensation, and escalation
  match the action's risk.
- Protocol or interface choice follows the task and consumer, not novelty.
- The recommendation does not execute, authorize, expose, purchase, submit, or change state.

# Handoff Signals

- The need is informational rather than state-changing → use another discovery skill.
- The capability needs an API or tool contract → `api-design` and the implementation owner.
- Interface language, forms, state, or recovery are unclear → `ux-writing` or `heuristic-audit`.
- Permissions, secrets, sensitive context, or external instructions are unsafe →
  `restricted-context-check` and security ownership.
- Task success and side effects need repeatable measurement → `ai-discovery-measurement`.
- Financial, legal, policy, or consequential authority remains unresolved → human or governance gate.

# Pairs Well With

- `ai-discovery-measurement`
- `api-design`
- `ux-writing`
- `heuristic-audit`
- `restricted-context-check`
- `premortem`
- `observability-review`
- `qa-review`

# Anti-patterns

- Treating buttons, links, or DOM selectors as the capability inventory.
- Selecting WebMCP, MCP, A2A, OpenAPI, or another protocol before defining the task and consumer.
- Hiding authorization or consent inside a generic "agent allowed" flag.
- Allowing irreversible or financial action without explicit confirmation and recovery.
- Retrying state-changing actions without idempotency or partial-completion handling.
- Exposing private data, internal tools, or broad authority because an agent can technically use them.
- Treating a successful happy path as proof of safety or readiness.
- Implementing the proposed exposure path inside this read-only skill.
