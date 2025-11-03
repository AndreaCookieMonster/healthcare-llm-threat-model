---
layout: default
title: Healthcare LLM Threat Catalog
description: Catalog of healthcare-relevant LLM vulnerabilities mapped to the OWASP Top-10.
---

# Healthcare LLM Threat Catalog

**OWASP Top-10 for LLM Applications × Healthcare Context × CVEs (last two years)**  
**Updated:** 2025-03-17

This catalog maps recent, **healthcare-relevant AI vulnerabilities (CVEs)** to the **OWASP Top-10 for Large Language Model Applications**. It’s meant for practical use by clinicians, compliance leads, security teams, and community partners co-designing real health tech. It focuses on what can actually hurt people: data exposure, mis-routing, misdiagnosis, and operational disruption.

> ### Scope & Selection
> *Included*: public CVEs from ~2024–2025 that are both **AI-related** and **healthcare-relevant** (e.g., Azure Health Bot; MONAI imaging toolkit).  
> *Not yet included*: model-safety failures that aren’t tracked as CVEs (e.g., bias, hallucinations), but categories are listed so you can add incidents over time.

---

## Table of Contents
- [October 2025 additions (research highlights)](#october-2025-additions-research-highlights)
- [LLM01 — Prompt Injection](#llm01--prompt-injection)
- [LLM02 — Insecure Output Handling](#llm02--insecure-output-handling)
- [LLM03 — Training Data Poisoning](#llm03--training-data-poisoning)
- [LLM04 — Model Denial of Service](#llm04--model-denial-of-service)
- [LLM05 — Supply Chain Vulnerabilities](#llm05--supply-chain-vulnerabilities)
- [LLM06 — Sensitive Information Disclosure](#llm06--sensitive-information-disclosure)
- [LLM07 — Insecure Plugin / Connector Design](#llm07--insecure-plugin--connector-design)
- [LLM08 — Excessive Agency](#llm08--excessive-agency)
- [LLM09 — Overreliance](#llm09--overreliance)
- [LLM10 — Model Theft](#llm10--model-theft)
- [How to contribute](#how-to-contribute)
- [References](#references)

---

## October 2025 additions (research highlights)
- See the full roundup: [October 2025 Additions – High-Impact LLM Vulnerabilities in Healthcare]({{ '/additions/2025-10/' | relative_url }})
- Quick jump links by category:
  - **Prompt injection:** Medical VLM oncology study [paper](https://www.nature.com/articles/s41467-024-55631-x) · [code](https://github.com/KatherLab/prompt_injection_attacks) · [Surgical video VLM attacks](https://pubmed.ncbi.nlm.nih.gov/40778151/) · [Adversarial hallucination attacks in CDS](https://www.nature.com/articles/s43856-025-01021-3)
  - **Data poisoning & backdoors:** Medical LLM poisoning [paper](https://www.nature.com/articles/s41591-024-03445-1.pdf) · [Scorpius training-data attack repo](https://github.com/yjwtheonly/Scorpius) · [BadCLM clinical backdoor study](https://pubmed.ncbi.nlm.nih.gov/40417555/)
  - **Privacy & disclosure:** DIRI patient re-identification study (PubMed [40502277](https://pubmed.ncbi.nlm.nih.gov/40502277/)) · Radiology report anonymization pitfalls (PubMed [39480533](https://pubmed.ncbi.nlm.nih.gov/39480533/))
  - **Governance & safety messaging:** Declining medical safety disclaimers (PubMed [41038984](https://pubmed.ncbi.nlm.nih.gov/41038984/))

## LLM01 — Prompt Injection
**Healthcare note:** Malicious prompts cause tools/connectors to leak PHI or perform unsafe actions.

- **CVE entries (last 24 months):** _None identified that are both AI-specific and healthcare-specific._
  Add incidents here even if non-CVE (e.g., red-teaming findings), so governance can act.
- _October 2025 additions:_ [Prompt injection attacks on medical VLMs (Nat Commun 2025)](https://www.nature.com/articles/s41467-024-55631-x) · [Prompt Injection Attacks (KatherLab) code repo](https://github.com/KatherLab/prompt_injection_attacks) · [Prompt injection on surgical decision-support VLMs (medRxiv 2025)](https://pubmed.ncbi.nlm.nih.gov/40778151/) · [Adversarial hallucination attacks in CDS (Communications Medicine 2025)](https://www.nature.com/articles/s43856-025-01021-3)

---

## LLM02 — Insecure Output Handling
**Healthcare note:** App consumes LLM output as “instructions,” enabling abuse (e.g., unsafe routing/orders).

- **CVE entries (last 24 months):** _None identified that squarely fit this category._
  See LLM05/06 for post-compromise impact that can drive unsafe outputs.
- _October 2025 additions:_ [Prompt injection attacks on medical VLMs (Nat Commun 2025)](https://www.nature.com/articles/s41467-024-55631-x) · [Prompt injection on surgical decision-support VLMs (medRxiv 2025)](https://pubmed.ncbi.nlm.nih.gov/40778151/) · [Adversarial hallucination attacks in CDS (Communications Medicine 2025)](https://www.nature.com/articles/s43856-025-01021-3) · [DIRI adversarial re-identification study](https://pubmed.ncbi.nlm.nih.gov/40502277/) · [Radiology report anonymization benchmarking](https://pubmed.ncbi.nlm.nih.gov/39480533/) · [Declining medical safety disclaimers study](https://pubmed.ncbi.nlm.nih.gov/41038984/)

---

## LLM03 — Training Data Poisoning
**Healthcare note:** Tainted imaging/corpus subverts clinical models.

- **CVE entries (last 24 months):** _None identified yet as CVEs._
- _October 2025 additions:_ [Medical LLM data-poisoning attacks (Nat Med 2025)](https://www.nature.com/articles/s41591-024-03445-1.pdf) · [Scorpius poisoning framework (GitHub)](https://github.com/yjwtheonly/Scorpius) · [BadCLM backdoor in clinical LLMs (PubMed 40417555)](https://pubmed.ncbi.nlm.nih.gov/40417555/)

---

## LLM04 — Model Denial of Service (DoS)
**Healthcare note:** Cost spikes / unavailability disrupt triage or imaging support.

- **CVE entries (last 24 months):** _None identified yet as CVEs._

---

## LLM05 — Supply Chain Vulnerabilities
**Healthcare note:** Managed AI services, model bundles, and libraries bring “classic” vulns (SSRF, unsafe deserialization) into care delivery.

| CVE | Affected Component | Year | CVSS | Summary (plain English) | Links (NVD / Vendor or Advisory / Research) | Mitigations (operational + technical) | Impact (realistic patient-harm examples) |
|---|---|---:|---|---|---|---|---|
| **CVE-2024-38109** | **Microsoft Azure Health Bot** (managed AI health chatbot) | 2024 | **NVD:** 8.8 (v3.1) · **Microsoft CNA:** 9.1 | **SSRF** in “Data Connections”: authenticated users could make the service call **internal endpoints** → elevation of privilege / potential cross-tenant access. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38109) · [Tenable Research](https://www.tenable.com/security/research/tra-2024-27) | Egress allow-listing (block IMDS `169.254.169.254` & RFC1918), least-privilege service principals, tenant-isolation tests (canary SSRF), DLP on connector traffic, network micro-segmentation for bot↔EHR/FHIR, formal patch tracking of MSRC bulletins. | (1) Bot pulls **wrong tenant’s patient** via cross-boundary query; clinician acts on mis-linked PHI → **inappropriate care**. (2) Lateral move to triage transcript store → exposure of symptoms/meds tied to identities → **privacy harm and stigma**. |
| **CVE-2025-21384** | **Microsoft Azure Health Bot** | 2025 | **NVD:** 8.8 (v3.1) · **Microsoft CNA:** 8.3 | **Authenticated SSRF** to internal resources → elevation of privilege. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) · [MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21384) | Above + per-connector trust boundaries (read-only vs write), token lifetime minimization and secret rotation tied to patch windows, egress anomaly detection. | (1) Access to intranet file share with intake PDFs → **bulk PHI exfiltration**. (2) Manipulated routing/validation → delayed escalation for red-flag symptoms → **care delays and harm**. |
| **CVE-2025-58756** | **MONAI** (Medical Open Network for AI, imaging toolkit) | 2025 | **CNA (GitHub):** 8.8 (v3.1) | **Insecure checkpoint loading** (e.g., `torch.load`) can lead to **arbitrary code execution** when a malicious model file is loaded. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [GHSA](https://github.com/advisories/GHSA-6vm5-6jv9-rjpj) | Artifact trust policy (signed models only; verify before load), disallow unsafe deserialization on untrusted inputs, sandbox model-load jobs (no egress; read-only mounts), SBOM & provenance (SLSA) gates, strict secrets minimization for imaging workers. | (1) RCE siphons **DICOM archives** (images+metadata) → **mass privacy breach**. (2) Backdoor alters segmentation/classification → **missed tumor** or **false positive**, delaying/misdirecting treatment. |
| **CVE-2025-58757** | **MONAI** (imaging toolkit) | 2025 | **CNA (GitHub):** 8.8 (v3.1) | **Unsafe `pickle` deserialization** in `pickle_operations` → **RCE** when processing crafted data. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) · [GHSA](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm) | Remove/replace `pickle.loads`, require safe formats (Safetensors/ONNX) with signatures, integrity/attestation checks for bundles, network isolation for preprocessing nodes, continuous code-scanning rule to flag deserialization. | (1) **Clinical ransomware** on imaging nodes → canceled scans, care delays. (2) Exfiltration of imaging data + model weights → **privacy loss + model/IP theft**, undermining trust in AI-assisted reads. |
- _October 2025 additions:_ [Prompt injection attacks on medical VLMs (Nat Commun 2025)](https://www.nature.com/articles/s41467-024-55631-x) · [Medical LLM data-poisoning attacks (Nat Med 2025)](https://www.nature.com/articles/s41591-024-03445-1.pdf) · [BadCLM backdoor in clinical LLMs (PubMed 40417555)](https://pubmed.ncbi.nlm.nih.gov/40417555/)

---

## LLM06 — Sensitive Information Disclosure
**Healthcare note:** PHI leakage via connectors, logs/telemetry, or post-compromise exfiltration.

| CVE | Classification | Why it fits LLM06 | Links |
|---|---|---|---|
| **CVE-2024-38109** | Secondary | SSRF can bypass intended data scopes; potential cross-tenant resource visibility. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [Tenable](https://www.tenable.com/security/research/tra-2024-27) |
| **CVE-2025-21384** | Secondary | Authenticated SSRF → unauthorized internal data access. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) |
| **CVE-2025-58756 / -58757** | Secondary | RCE on imaging/AI nodes enables **DICOM/PHI exfiltration** after compromise. | [NVD 58756](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [NVD 58757](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) |
- _October 2025 additions:_ [DIRI adversarial re-identification study](https://pubmed.ncbi.nlm.nih.gov/40502277/) · [Radiology report anonymization benchmarking](https://pubmed.ncbi.nlm.nih.gov/39480533/)

**Mitigation emphasis (LLM06):** Context minimization (redact PHI at prompt/connector boundaries), DLP on egress, block metadata/private ranges, micro-segment AI runtimes ↔ EHR/FHIR, anomaly detection (bulk reads, unusual connector targets, atypical model-load behavior).

---

## LLM07 — Insecure Plugin / Connector Design
**Healthcare note:** “Data Connections” (FHIR, scheduling, KBs) behave like plugins; weak guardrails expose internals.

| CVE | Classification | Why it fits LLM07 | Links |
|---|---|---|---|
| **CVE-2024-38109** | Secondary | Connector path allowed SSRF; fix required stricter redirect/validation. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-38109) · [Tenable](https://www.tenable.com/security/research/tra-2024-27) |
| **CVE-2025-21384** | Secondary | Authenticated SSRF via connector-like data connections. | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-21384) |

**Mitigation emphasis (LLM07):** Capability-scoped connectors (e.g., “read-FHIR only”), outbound allow-lists, intent-gating for risky actions, full audit chain (bot session → connector call → resource), red-team SSRF tests.

---

## LLM08 — Excessive Agency
**Healthcare note:** Over-permissioned agents trigger real-world actions without checks.

- **CVE entries (last 24 months):** _None identified that are clearly CVE-tracked in healthcare+AI._

---

## LLM09 — Overreliance
**Healthcare note:** Clinicians over-trust AI outputs; governance gap rather than a CVE-type software defect.

- **CVE entries (last 24 months):** _None identified._
- _October 2025 additions:_ [Adversarial hallucination attacks in CDS (Communications Medicine 2025)](https://www.nature.com/articles/s43856-025-01021-3) · [Declining medical safety disclaimers study](https://pubmed.ncbi.nlm.nih.gov/41038984/)

---

## LLM10 — Model Theft
**Healthcare note:** Theft of tuned clinical models undermines validation/reproducibility; enables unsafe reuse elsewhere.

| CVE | Classification | Why it fits LLM10 | Links |
|---|---|---|---|
| **CVE-2025-58756 / -58757** | Secondary | Post-RCE actors can copy **model weights** and training artifacts. | [NVD 58756](https://nvd.nist.gov/vuln/detail/CVE-2025-58756) · [GHSA 58756](https://github.com/advisories/GHSA-6vm5-6jv9-rjpj) · [NVD 58757](https://nvd.nist.gov/vuln/detail/CVE-2025-58757) · [GHSA 58757](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm) |

**Mitigation emphasis (LLM10):** Model registry with signing/attestation, no-egress inference pods, access logging with review, watermarking/provenance to detect stolen/altered models.

---

## How to contribute
- Add new CVE rows to the relevant category table(s).  
- Use this schema: **CVE, Affected, Year, CVSS, Summary, Links, Mitigations, Impact**.  
- Prefer authoritative links (NVD, MSRC, GHSA) and add one clear research/explainer link when helpful.  
- Keep **Impact** grounded in patient realities (privacy, dignity, misdiagnosis, delays, financial harm).  
- For non-CVE incidents (e.g., safety reports), clearly label them and cite public evidence.

---

## References
- OWASP Top-10 for LLM Applications (Project page): <https://owasp.org/www-project-top-10-for-large-language-model-applications/>  
- NVD – CVE-2024-38109 (Azure Health Bot): <https://nvd.nist.gov/vuln/detail/CVE-2024-38109>  
- MSRC – CVE-2024-38109: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38109>  
- Tenable Research – Azure Health Bot SSRF: <https://www.tenable.com/security/research/tra-2024-27>  
- NVD – CVE-2025-21384 (Azure Health Bot): <https://nvd.nist.gov/vuln/detail/CVE-2025-21384>  
- MSRC – CVE-2025-21384: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21384>  
- NVD – CVE-2025-58756 (MONAI): <https://nvd.nist.gov/vuln/detail/CVE-2025-58756>  
- GHSA – CVE-2025-58756: <https://github.com/advisories/GHSA-6vm5-6jv9-rjpj>  
- NVD – CVE-2025-58757 (MONAI): <https://nvd.nist.gov/vuln/detail/CVE-2025-58757>  
- GHSA – CVE-2025-58757: <https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-p8cm-mm2v-gwjm>
