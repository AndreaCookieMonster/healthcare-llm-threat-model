# October 2025 Additions

These research highlights complement the Top 10 catalog with healthcare incidents that have not yet
resulted in CVE assignments. They mirror the `additions/2025-10/*.md` cards introduced in the recent
pull request.

| Theme | Summary | Primary references |
| --- | --- | --- |
| Prompt injection (oncology VLM) | Demonstrates how adversarial instructions in medical imaging workflows can override guardrails in oncology-focused VLMs. | [Nat Commun 2025](https://doi.org/10.1038/s41467-024-55631-x) |
| Prompt injection (surgical video VLM) | Shows surgical decision-support VLMs executing malicious prompts that drive unsafe tool actions. | [medRxiv 2025](https://doi.org/10.1101/2025.07.16.25331645) |
| Adversarial hallucination in CDS | Assurance analysis uncovering high success rates for hallucination attacks in clinical decision support. | [Commun Med 2025](https://doi.org/10.1038/s43856-025-01021-3) |
| Training-data poisoning | Empirical poisoning of medical LLMs that undermines clinical reasoning and triage support. | [Nat Med 2025](https://doi.org/10.1038/s41591-024-03445-1) |
| BadCLM EHR backdoor | Backdoor attacks on clinical language models tailored to electronic health records. | [PubMed 40417555](https://pubmed.ncbi.nlm.nih.gov/40417555/) |
| DIRI patient re-identification | Adversarial re-ID of patients from supposedly anonymised clinical text, highlighting PHI leakage risks. | [PubMed 40502277](https://pubmed.ncbi.nlm.nih.gov/40502277/) |
| Radiology report anonymization pitfalls | Evaluates automated anonymization pipelines powered by LLMs and the privacy gaps that remain. | [Int J Med Inform 2024](https://pubmed.ncbi.nlm.nih.gov/39480533/) |
| Declining safety disclaimers | Large models reduce or remove medical disclaimers over time, weakening governance controls. | [npj Digit Med 2025](https://doi.org/10.1038/s41746-025-01111-3) |

## How to use the additions

- Treat each entry as an early warning. If similar systems are deployed internally, map mitigations
  and monitoring before the issue graduates into a tracked vulnerability.
- Contributions are welcome—follow the pattern in `additions/2025-10/*.md` and include citations,
  mitigation notes, and the relevant OWASP mapping.
- When an issue receives a CVE, move it into the main `_threats/` entry and update
  `assets/catalog.json` via `npm run build:index`.
