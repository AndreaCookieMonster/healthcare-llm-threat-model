---
id: LLM05
title: 'Supply Chain Vulnerabilities'
slug: 'llm05--supply-chain-vulnerabilities'
summary:
  'Managed AI services and libraries pull SSRF and unsafe deserialization into care delivery.'
tags: ['supply-chain', 'ssrf', 'rce']
last_updated: '2025-03-17'
healthcare_note:
  'Managed AI services, model bundles, and libraries bring “classic” vulns (SSRF, unsafe
  deserialization) into care delivery.'
cve_window: 'last-24-months'
resources:
  - title: 'Medical VLM prompt injection (oncology)'
    url: '{{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-oncology/'
  - title: 'Training-data poisoning of medical LLMs'
    url: '{{ site.baseurl }}/additions/2025-10/training-data-poisoning-med-llms/'
  - title: 'BadCLM backdoor in EHR models'
    url: '{{ site.baseurl }}/additions/2025-10/badclm-ehr-backdoor/'
---

## CVE entries (last 24 months)

| CVE                | Affected Component                                         | Year | CVSS                                         | Summary (plain English)                                                                                                                                          | Links (NVD / Vendor or Advisory / Research)                                                                                                                                                                       | Mitigations (operational + technical)                                                                                                                                                                                                                        | Impact (realistic patient-harm examples)                                                                                                                                                                                                                |
| ------------------ | ---------------------------------------------------------- | ---: | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CVE-2024-38109** | **Microsoft Azure Health Bot** (managed AI health chatbot) | 2024 | **NVD:** 8.8 (v3.1) · **Microsoft CNA:** 9.1 | **SSRF** in “Data Connections”: authenticated users could make the service call **internal endpoints** → elevation of privilege / potential cross-tenant access. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38109) · [Tenable Research](https://www.tenable.com/security/research/tra-2024-27) | Egress allow-listing (block IMDS `169.254.169.254` & RFC1918), least-privilege service principals, tenant-isolation tests (canary SSRF), DLP on connector traffic, network micro-segmentation for bot↔EHR/FHIR, formal patch tracking of MSRC bulletins.    | (1) Bot pulls **wrong tenant’s patient** via cross-boundary query; clinician acts on mis-linked PHI → **inappropriate care**. (2) Lateral move to triage transcript store → exposure of symptoms/meds tied to identities → **privacy harm and stigma**. |
| **CVE-2025-21384** | **Microsoft Azure Health Bot**                             | 2025 | **NVD:** 8.8 (v3.1) · **Microsoft CNA:** 8.3 | **Authenticated SSRF** to internal resources → elevation of privilege.                                                                                           | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21384)                                                                             | Above + per-connector trust boundaries (read-only vs write), token lifetime minimization and secret rotation tied to patch windows, egress anomaly detection.                                                                                                | (1) Access to intranet file share with intake PDFs → **bulk PHI exfiltration**. (2) Manipulated routing/validation → delayed escalation for red-flag symptoms → **care delays and harm**.                                                               |
| **CVE-2025-58756** | **MONAI** (Medical Open Network for AI, imaging toolkit)   | 2025 | **CNA (GitHub):** 8.8 (v3.1)                 | **Insecure checkpoint loading** (e.g., `torch.load`) can lead to **arbitrary code execution** when a malicious model file is loaded.                             | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [GHSA](https://github.com/advisories/GHSA-6vm5-6jv9-rjpj)                                                                                                | Artifact trust policy (signed models only; verify before load), disallow unsafe deserialization on untrusted inputs, sandbox model-load jobs (no egress; read-only mounts), SBOM & provenance (SLSA) gates, strict secrets minimization for imaging workers. | (1) RCE siphons **DICOM archives** (images+metadata) → **mass privacy breach**. (2) Backdoor alters segmentation/classification → **missed tumor** or **false positive**, delaying/misdirecting treatment.                                              |
| **CVE-2025-58757** | **MONAI** (imaging toolkit)                                | 2025 | **CNA (GitHub):** 8.8 (v3.1)                 | **Unsafe `pickle` deserialization** in `pickle_operations` → **RCE** when processing crafted data.                                                               | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) · [GHSA](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm)                                                                   | Remove/replace `pickle.loads`, require safe formats (Safetensors/ONNX) with signatures, integrity/attestation checks for bundles, network isolation for preprocessing nodes, continuous code-scanning rule to flag deserialization.                          | (1) **Clinical ransomware** on imaging nodes → canceled scans, care delays. (2) Exfiltration of imaging data + model weights → **privacy loss + model/IP theft**, undermining trust in AI-assisted reads.                                               |

## References

- Prompt-injection mitigation pack:
  [Medical VLM prompt injection (oncology)]({{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-oncology/)
- Poisoning response drill:
  [Training-data poisoning of medical LLMs]({{ site.baseurl }}/additions/2025-10/training-data-poisoning-med-llms/)
- EHR-specific backdoor fallout:
  [BadCLM backdoor in EHR models]({{ site.baseurl }}/additions/2025-10/badclm-ehr-backdoor/)
