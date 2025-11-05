---
id: LLM06
title: 'Sensitive Information Disclosure'
slug: 'llm06--sensitive-information-disclosure'
summary: 'PHI leaks via connectors, logging, or post-compromise exfiltration.'
tags: ['privacy', 'ssrf', 'exfiltration']
last_updated: '2025-03-17'
healthcare_note: 'PHI leakage via connectors, logs/telemetry, or post-compromise exfiltration.'
cve_window: 'last-24-months'
resources:
  - title: 'DIRI patient re-identification'
    url: "{{ '/additions/2025-10/patient-reidentification-diri/' | relative_url }}"
  - title: 'Radiology report anonymization pitfalls'
    url: "{{ '/additions/2025-10/radiology-report-anonymization-llms/' | relative_url }}"
  - title:
      'DIRI: Adversarial Patient Reidentification with Large Language Models for Evaluating Clinical
      Text Anonymization (arXiv 2025)'
    url: 'https://pubmed.ncbi.nlm.nih.gov/40502277/'
  - title: 'Automated anonymization of radiology reports (Int J Med Inform 2024)'
    url: 'https://pubmed.ncbi.nlm.nih.gov/39480533/'
---

## CVE entries (last 24 months)

| CVE                         | Classification | Why it fits LLM06                                                                 | Links                                                                                                                       |
| --------------------------- | -------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **CVE-2024-38109**          | Secondary      | SSRF can bypass intended data scopes; potential cross-tenant resource visibility. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [Tenable](https://www.tenable.com/security/research/tra-2024-27)   |
| **CVE-2025-21384**          | Secondary      | Authenticated SSRF → unauthorized internal data access.                           | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384)                                                                      |
| **CVE-2025-58756 / -58757** | Secondary      | RCE on imaging/AI nodes enables **DICOM/PHI exfiltration** after compromise.      | [NVD 58756](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [NVD 58757](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) |

**Mitigation emphasis:** Context minimization (redact PHI at prompt/connector boundaries), DLP on
egress, block metadata/private ranges, micro-segment AI runtimes ↔ EHR/FHIR, anomaly detection
(bulk reads, unusual connector targets, atypical model-load behavior).

## References

- De-identification red team:
  [DIRI patient re-identification]({{ '/additions/2025-10/patient-reidentification-diri/' | relative_url }})
- Imaging privacy audit:
  [Radiology report anonymization pitfalls]({{ '/additions/2025-10/radiology-report-anonymization-llms/' | relative_url }})
- Clinical anonymization benchmark:
  [DIRI: Adversarial Patient Reidentification with Large Language Models for Evaluating Clinical Text Anonymization (arXiv 2025)](https://pubmed.ncbi.nlm.nih.gov/40502277/)
- Operational anonymizer study:
  [Automated anonymization of radiology reports: comparison of publicly available NLP and large language models (Int J Med Inform 2024)](https://pubmed.ncbi.nlm.nih.gov/39480533/)
