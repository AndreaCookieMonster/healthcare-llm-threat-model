---
layout: default
title: Healthcare LLM Threat Catalog
description: Catalog of healthcare-relevant LLM vulnerabilities mapped to the OWASP Top-10.
---

# Healthcare LLM Threat Catalog

**OWASP Top-10 for LLM Applications × Healthcare Context × CVEs (last two years)**  
**Updated:** 2025-03-17

This catalog maps recent, **healthcare-relevant AI vulnerabilities (CVEs)** to the **OWASP Top-10
for Large Language Model Applications**. It’s meant for practical use by clinicians, compliance
leads, security teams, and community partners co-designing real health tech. It focuses on what can
actually hurt people: data exposure, mis-routing, misdiagnosis, and operational disruption.

> ### Scope & Selection
>
> - _Included_: public CVEs from ~2024–2025 that are both **AI-related** and **healthcare-relevant**
>   (e.g., Azure Health Bot; MONAI imaging toolkit).
> - _Not yet included_: model-safety failures that aren’t tracked as CVEs (e.g., bias,
>   hallucinations), but categories are listed so you can add incidents over time.

---

## Threat catalog

- Browse the [full threat list](/threats/) with filters, stable slugs, and JSON index support for
  search.
- Each threat lives in `_threats/` with structured front matter validated in CI.

---

## October 2025 additions (research highlights)

- See the full roundup: [October 2025 Additions – High-Impact LLM Vulnerabilities in
  Healthcare]({{ site.baseurl }}/additions/2025-10/index.md)
- Quick jump links by category:
  - **Prompt injection:** [Medical VLMs
    (oncology)]({{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-oncology.md), [Surgical
    video VLMs]({{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-surgical-video.md),
    [Adversarial hallucination attacks in
    CDS]({{ site.baseurl }}/additions/2025-10/adversarial-hallucination-attacks-cds.md)
  - **Data poisoning & backdoors:** [Training-data poisoning of medical
    LLMs]({{ site.baseurl }}/additions/2025-10/training-data-poisoning-med-llms.md), [BadCLM
    backdoor in EHR models]({{ site.baseurl }}/additions/2025-10/badclm-ehr-backdoor.md)
  - **Privacy & disclosure:** [DIRI patient
    re-identification]({{ site.baseurl }}/additions/2025-10/patient-reidentification-diri.md),
    [Radiology report anonymization
    pitfalls]({{ site.baseurl }}/additions/2025-10/radiology-report-anonymization-llms.md)
  - **Governance & safety messaging:** [Declining medical safety
    disclaimers]({{ site.baseurl }}/additions/2025-10/declining-safety-disclaimers.md)

---

## How to contribute

- Add new CVE rows to the relevant threat file under `_threats/` and update `assets/catalog.json`
  via `npm run build:index`.
- Use this schema: **CVE, Affected, Year, CVSS, Summary, Links, Mitigations, Impact**.
- Prefer authoritative links (NVD, MSRC, GHSA) and add one clear research/explainer link when
  helpful.
