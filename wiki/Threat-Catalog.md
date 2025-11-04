# Threat Catalog

The catalog below mirrors the `_threats/*.md` files that now power the site. Each entry pairs an
OWASP Top 10 for LLM Applications category with a healthcare-specific summary and the date it was
last refreshed during the documentation migration.

| OWASP ID | Risk | Healthcare summary | Last updated | Representative resources |
| --- | --- | --- | --- | --- |
| LLM01 | Prompt Injection | Malicious prompts cause tools/connectors to leak PHI or perform unsafe actions. | 2025-03-17 | [Nat Commun oncology VLM attack](https://doi.org/10.1038/s41467-024-55631-x)<br>[Surgical VLM medRxiv preprint](https://doi.org/10.1101/2025.07.16.25331645) |
| LLM02 | Insecure Output Handling | Applications treat LLM output as executable instructions, enabling unsafe routing or orders. | 2025-03-17 | [Nat Commun oncology VLM attack](https://doi.org/10.1038/s41467-024-55631-x)<br>[Commun Med assurance analysis](https://doi.org/10.1038/s43856-025-01021-3) |
| LLM03 | Training Data Poisoning | Tainted imaging or corpora subvert clinical models and introduce backdoors. | 2025-03-17 | [Nat Med poisoning study](https://doi.org/10.1038/s41591-024-03445-1)<br>[BadCLM EHR backdoor](https://pubmed.ncbi.nlm.nih.gov/40417555/) |
| LLM04 | Model Denial of Service | Cost spikes or downtime disrupt triage workflows and imaging support. | 2025-03-17 | — |
| LLM05 | Supply Chain Vulnerabilities | Managed services and libraries pull SSRF and unsafe deserialization into care delivery. | 2025-03-17 | [Azure Health Bot SSRF CVE-2024-38109](https://nvd.nist.gov/vuln/detail/CVE-2024-38109)<br>[Azure Health Bot SSRF CVE-2025-21384](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) |
| LLM06 | Sensitive Information Disclosure | PHI leaks via connectors, logging, or post-compromise exfiltration. | 2025-03-17 | [DIRI patient re-identification](../additions/2025-10/patient-reidentification-diri.md)<br>[Radiology anonymization pitfalls](../additions/2025-10/radiology-report-anonymization-llms.md) |
| LLM07 | Insecure Plugin / Connector Design | Over-trusted data connections behave like plugins and expose internal systems. | 2025-03-17 | [CVE-2024-38109](https://nvd.nist.gov/vuln/detail/CVE-2024-38109)<br>[CVE-2025-21384](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) |
| LLM08 | Excessive Agency | Over-permissioned agents trigger real-world actions without guardrails. | 2025-03-17 | — |
| LLM09 | Overreliance | Clinicians over-trust AI outputs, amplifying harmful hallucinations without governance. | 2025-03-17 | [Adversarial hallucination attacks](../additions/2025-10/adversarial-hallucination-attacks-cds.md)<br>[Declining medical safety disclaimers](../additions/2025-10/declining-safety-disclaimers.md) |
| LLM10 | Model Theft | Attackers steal tuned clinical models after runtime compromise or misconfiguration. | 2025-03-17 | [CVE-2025-58756](https://nvd.nist.gov/vuln/detail/CVE-2025-58756)<br>[CVE-2025-58757](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) |

### Working with the catalog

- Each Markdown file in `_threats/` contains front matter with the fields validated in CI. The wiki
  surfaces only the highlights; visit the files for CVE tables, mitigation notes, and references.
- Automated validation scripts live in `scripts/` and run through GitHub Actions to prevent broken
  front matter or malformed tables from landing in the repository.
- Programmatic consumers can pull the structured data from `assets/catalog.json`, which is generated
  via `npm run build:index`.
