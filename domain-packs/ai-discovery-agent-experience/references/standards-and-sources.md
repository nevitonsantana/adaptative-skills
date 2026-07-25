# Standards and Official Sources Register

**Reviewed:** 2026-07-25

**Status:** dated implementation context, not invariant skill canon

Use this register only when an activated module needs current protocol, provider, or vocabulary detail. Recheck the source and applicable version at the time of use. A listed mechanism is not a universal recommendation.

| Surface | Source | Status at review | Conditional use |
| --- | --- | --- | --- |
| Crawler access | [RFC 9309: Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) | Internet Standard | Interpret `robots.txt` behavior; it does not prove indexing or ranking. |
| Search discovery | [Google Search crawling and indexing documentation](https://developers.google.com/search/docs/crawling-indexing) | Provider-specific guidance | Use only for the relevant provider and observed property. |
| Canonicalization | [Google canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | Provider-specific guidance | Diagnose duplicate signals; canonical hints do not guarantee selection. |
| Structured data | [Google structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) and [Schema.org documentation](https://schema.org/docs/documents.html) | Provider policy plus shared vocabulary | Use supported types that match visible, source-backed content; do not promise rich results. |
| HTTP API descriptions | [OpenAPI Specification](https://spec.openapis.org/oas/) | Published specification | Consider when an authorized HTTP API is the right action surface; OpenAPI does not supply authorization or safe task design by itself. |
| Tool context protocol | [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/index) | Versioned specification | Consider only when MCP fits an existing integration and trust boundary. |
| Agent-to-agent protocol | [A2A Protocol specification](https://a2a-protocol.org/latest/specification/) | Evolving specification | Consider only for justified interoperable agent collaboration. |
| Browser capabilities | [WebMCP draft](https://webmachinelearning.github.io/webmcp/) | Draft Community Group Report | Treat as experimental; do not make it a readiness prerequisite. |
| LLM-oriented site summary | [`llms.txt` proposal](https://llmstxt.org/) | Community proposal, not adopted here as a normative standard | Test only as a bounded experiment with a measurable question. |

## Use rules

1. Start with the user task, evidence, and failure mode—not a preferred technology.
2. Record the exact source, version or review date, and observed behavior used in a finding.
3. Treat schema, `llms.txt`, WebMCP, MCP, A2A, and OpenAPI as conditional implementation options.
4. Do not infer discovery, citation, ranking, conversion, or agent adoption from technical eligibility.
5. Escalate authorization, policy, publication, and production changes to their owners.
