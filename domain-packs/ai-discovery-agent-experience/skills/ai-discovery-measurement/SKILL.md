---
name: ai-discovery-measurement
description: Design repeatable, dated evaluations for search discovery, generative retrieval and citation, entity representation, and agent-task outcomes without hiding variance or uncertainty.
metadata:
  version: "0.1.0"
  owner: adaptive-skills
  category: ai-discovery-agent-experience
---

# Overview

Use this skill when a discovery or agent-experience decision needs repeatable evidence rather
than a one-off search, prompt, or task run. It defines samples, run conditions, raw records,
comparisons, uncertainty, and decision-linked conclusions.

It does not create a universal visibility score, operate monitoring infrastructure, set
business targets, or claim that external systems behave deterministically.

# When to Use

- A baseline or before/after comparison is needed.
- Generative outputs, citations, rankings, or agent runs may vary.
- More than one platform, model, engine, environment, or task must be compared.
- Entity or claim fidelity needs a repeatable evaluation.
- Agent-task completion, correctness, intervention, side effects, or recovery must be measured.

# When NOT to Use

- The decision can be answered by one direct, deterministic repository check.
- No target decision, sample, run record, or comparison condition can be defined.
- The requester wants a universal score or deterministic forecast.
- The task is to build analytics, monitoring, experimentation, or data infrastructure.

# Core Moves

1. **Name the decision and dimensions.** Define what the measurement must support and whether
   discovery, citation, representation, action, or outcome evidence matters.
2. **Design a reproducible sample.** Specify properties, surfaces, queries, platforms, models,
   runs, tasks, dates, controls, and comparison conditions.
3. **Capture raw observations first.** Preserve prompts, queries, outputs, citations, responses,
   task states, metadata, errors, and unavailable fields before summarizing.
4. **Compare with uncertainty.** Report variance, confounders, platform differences, limitations,
   and non-comparable results instead of smoothing them into confidence.
5. **Connect evidence to a decision.** Produce dimensional findings, verification, next
   experiment, stop condition, and human-owned interpretation.

# Optional Modules

- **Prompt and query-set design** — Build representative, versioned query families and task prompts.
- **Multi-platform run protocol** — Define comparable conditions while preserving platform
  differences.
- **Repeated-run evaluation** — Measure variance across nondeterministic executions.
- **Citation measurement** — Record source presence, prominence, relevance, and support.
- **Representation-fidelity measurement** — Compare factual and semantic fidelity with canonical
  records.
- **Agent-task success evaluation** — Measure completion, correctness, human intervention,
  duration, cost, side effects, and recovery.
- **Before-after experiment** — Compare a bounded intervention against a baseline.
- **Continuous-observation design** — Define cadence and meaningful-change thresholds without
  creating monitoring infrastructure.

# Activation Triggers

- Activate **prompt and query-set design** when no stable evaluation sample exists.
- Activate **multi-platform run protocol** when more than one external system is assessed.
- Activate **repeated-run evaluation** when output is nondeterministic or consistency matters.
- Activate **citation measurement** only when citations are observable and decision-relevant.
- Activate **representation-fidelity measurement** when canonical entity or claim records exist.
- Activate **agent-task success evaluation** only when a concrete executable task exists.
- Activate **before-after experiment** after a bounded intervention with comparable conditions.
- Activate **continuous-observation design** when the property or external systems change over time.

# Expected Output

```yaml
ai_discovery_measurement:
  decision:
  dimensions: [discovery | citation | representation | action | outcome]
  sample:
    properties: []
    surfaces: []
    queries_or_tasks: []
    platforms_or_environments: []
    run_count:
    window:
  protocol:
    controlled_conditions: []
    known_differences: []
    raw_record_location:
  observations:
    - run_id:
      observed_at:
      system_context:
      input:
      raw_output:
      citations_or_sources: []
      task_state:
      errors: []
      unavailable_fields: []
  findings:
    - finding_id:
      skill: ai-discovery-measurement
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
  variance_and_confounders: []
  limitations: []
```

# Verification

- The supported decision and measured dimensions are explicit.
- Every reported metric states method, sample, date, source, unit, and limitations.
- Raw observations exist before aggregation and can be traced to findings.
- Platform, model, environment, and run differences are retained.
- Non-comparable or unavailable results remain labeled rather than imputed.
- No single composite score hides distinct discovery, citation, representation, action, or
  outcome dimensions.
- The conclusion states what the evidence can and cannot support.

# Handoff Signals

- The sample depends on canonical entities or claims → `knowledge-entity-representation`.
- Search access or indexability is unclear → `search-indexability-optimization`.
- Generative findings need interpretation and bounded intervention hypotheses →
  `generative-visibility-optimization`.
- A state-changing agent task requires authority and recovery review →
  `agent-capability-actionability`.
- Instrumentation or production monitoring must be built → `observability-review` and the
  implementation owner.
- The result changes business priority, budget, or policy → human or governance review.

# Pairs Well With

- `knowledge-entity-representation`
- `search-indexability-optimization`
- `generative-visibility-optimization`
- `agent-capability-actionability`
- `observability-review`
- `testing`
- `premortem`

# Anti-patterns

- Reporting one search, prompt, citation, or task run as a durable baseline.
- Comparing platforms while hiding different dates, models, settings, or available features.
- Inventing missing samples, denominators, citations, costs, or task outcomes.
- Averaging away failure modes or nondeterministic variance.
- Creating a universal AI visibility score with unsupported weights.
- Treating citation, mention, ranking, referral, engagement, and conversion as interchangeable.
- Running continuous observation without an owner, decision, threshold, or stop condition.
