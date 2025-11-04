# Healthcare LLM Threat Catalog

The wiki mirrors the structure of the published site and the Markdown refactor introduced in
[#8](https://github.com/AndreaCookieMonster/healthcare-llm-threat-model/pull/8). It centers on
healthcare-ready interpretations of the **OWASP Top 10 for LLM Applications** and adds
high-impact research that has not yet produced CVEs.

## Scope & selection criteria

- Public CVEs from roughly the last 24 months that are **both AI-related and healthcare-relevant**
  (for example Azure Health Bot or the MONAI imaging toolkit).
- Peer-reviewed or practitioner evidence that demonstrates how an LLM issue manifests inside
  clinical or operational healthcare workflows.
- Incidents that do **not** have CVE coverage yet are captured as "additions"
  so that risk owners can still act on them.

## What changed in the documentation refactor

The latest documentation update introduced:

- **Structured threat files (`_threats/*.md`)** with required front matter validated in CI.
- A generated **JSON catalog (`assets/catalog.json`)** that can be consumed by downstream tooling.
- Markdown linting, YAML validation, and spell-check scripts (`scripts/*.js`,
  `scripts/*.py`) that run in GitHub Actions for quality control.
- Updated README and contribution guidance so non-technical collaborators know how to add threats
  via Markdown or spreadsheets.

## Quick links

- [Threat Catalog](Threat-Catalog) — top-level OWASP × healthcare mapping with summaries.
- [October 2025 Additions](October-2025-Additions) — curated incidents that supplement the Top 10.
- [Repository README](../README.md) — broader project overview and motivations.
- [Contribution guidelines](../CONTRIBUTING.md) — step-by-step instructions for spreadsheet and
  Markdown updates.

## How to use this catalog

1. Identify the OWASP category that matches your system’s workflow.
2. Review the healthcare summary and linked resources to understand clinical impact.
3. Pull the relevant entries from `assets/catalog.json` or the `_threats/` Markdown for integration
   into governance, risk, and compliance tooling.
4. Track emerging incidents via the additions page until they receive CVE identifiers.

## Feedback & contributions

Issues and pull requests are welcome. If you have sensitive incident data, coordinate privately with
maintainers first so we can avoid exposing regulated information in a public repository.
