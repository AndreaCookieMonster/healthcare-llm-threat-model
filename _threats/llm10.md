---
id: LLM10
title: 'Model Theft'
slug: 'llm10--model-theft'
summary: 'Attackers steal tuned clinical models after runtime compromise or misconfiguration.'
tags: ['intellectual-property', 'rce']
last_updated: '2025-03-17'
healthcare_note:
  'Theft of tuned clinical models undermines validation/reproducibility; enables unsafe reuse
  elsewhere.'
cve_window: 'last-24-months'
resources:
  - title: 'NVD entry for CVE-2025-58756'
    url: 'https://nvd.nist.gov/vuln/detail/CVE-2025-58756'
  - title: 'NVD entry for CVE-2025-58757'
    url: 'https://nvd.nist.gov/vuln/detail/CVE-2025-58757'
  - title: 'GHSA advisory for CVE-2025-58756'
    url: 'https://github.com/advisories/GHSA-6vm5-6jv9-rjpj'
  - title: 'GHSA advisory for CVE-2025-58757'
    url: 'https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm'
---

## CVE entries (last 24 months)

| CVE                         | Classification | Why it fits LLM10                                                  | Links                                                                                                                                                                                                                                                                                        |
| --------------------------- | -------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CVE-2025-58756 / -58757** | Secondary      | Post-RCE actors can copy **model weights** and training artifacts. | [NVD 58756](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [GHSA 58756](https://github.com/advisories/GHSA-6vm5-6jv9-rjpj) · [NVD 58757](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) · [GHSA 58757](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm) |

**Mitigation emphasis:** Model registry with signing/attestation, no-egress inference pods, access
logging with review, watermarking/provenance to detect stolen/altered models.
