---
title: Choose an AI Discovery skill
description: Route an AI discovery or agent experience question to the smallest sufficient skill.
---


Use one building block by default when the question is clear. Start with the
`ai-discovery-agent-experience` family entrypoint when the request is broad, such as “improve
our SEO”. Compose only when the output of one block is necessary evidence for another.

The family entrypoint is optional. It helps users state an outcome without knowing the
specialist IDs; advanced users can continue directly with any skill below.

## Decision guide

| If the main uncertainty is… | Start with | Do not substitute it with… |
| --- | --- | --- |
| “What object, person, method, offer, or claim is this?” | `knowledge-entity-representation` | Search tactics or rewritten copy |
| “Can search systems access and interpret the intended surface?” | `search-indexability-optimization` | A rank promise or a single browser view |
| “How will we observe change repeatably?” | `ai-discovery-measurement` | Anecdotes or one prompt result |
| “How are generative answers sourcing and representing us?” | `generative-visibility-optimization` | General SEO advice without a repeated baseline |
| “Can an agent safely complete this user task?” | `agent-capability-actionability` | Choosing a protocol before defining controls |

## Weak fit

Do not use this pack when the request is only for copywriting, a generic analytics dashboard, an implementation with settled requirements, or guaranteed outcomes. Route those tasks to the relevant generic skill or implementation owner.

## Recovery paths

- **Entity scope is disputed:** pause downstream work and obtain an authorized representation decision.
- **Property or evidence access is unavailable:** record it as unavailable; do not simulate a crawl, baseline, or agent action.
- **A provider rule may have changed:** consult the pack's dated standards register and verify the current official source.
- **The intervention needs deployment:** hand off the bounded finding and verification method; the skill does not make the change.
