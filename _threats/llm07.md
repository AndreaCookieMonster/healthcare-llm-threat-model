---
id: LLM07
title: 'Insecure Plugin / Connector Design'
slug: 'llm07--insecure-plugin-connector-design'
summary: 'Over-trusted data connections behave like plugins and expose internal systems.'
tags: ['connectors', 'ssrf', 'governance']
last_updated: '2025-03-17'
healthcare_note:
  '“Data Connections” (FHIR, scheduling, KBs) behave like plugins; weak guardrails expose internals.'
cve_window: 'last-24-months'
resources: []
---

## CVE entries (last 24 months)

| CVE                | Classification | Why it fits LLM07                                                       | Links                                                                                                                     |
| ------------------ | -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **CVE-2024-38109** | Secondary      | Connector path allowed SSRF; fix required stricter redirect/validation. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [Tenable](https://www.tenable.com/security/research/tra-2024-27) |
| **CVE-2025-21384** | Secondary      | Authenticated SSRF via connector-like data connections.                 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384)                                                                    |

**Mitigation emphasis:** Capability-scoped connectors (e.g., “read-FHIR only”), outbound
allow-lists, intent-gating for risky actions, full audit chain (bot session → connector call →
resource), red-team SSRF tests.
