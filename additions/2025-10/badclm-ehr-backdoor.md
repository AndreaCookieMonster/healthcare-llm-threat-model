---
layout: default
title: BadCLM backdoor attacks on clinical language models (EHR)
description:
  Poisoned EHR fine-tuning data can implant triggerable backdoors into clinical LLM assistants.
---

# BadCLM: backdoor attacks on clinical language models (EHR)

**Why it matters (impact)**  
Demonstrates implantable triggers during fine-tuning that cause targeted misbehavior when short
token sequences appear in EHR text—classic backdoor pattern plausible across vendor/partner
fine-tunes.

**OWASP LLM Top-10 mapping**

- LLM03: Training Data Poisoning
- LLM05: Supply Chain Vulnerabilities

**Mitigations**

- Fine-tune with strict data provenance; run backdoor detection (activation clustering, spectral
  methods).
- Disallow deployment without trigger-sweep tests and kill-switch policies.

**Evidence (preprint, NIH-indexed)**

- [BadCLM: Backdoor Attack in Clinical Language Models for Electronic Health Records (arXiv 2024)](https://pubmed.ncbi.nlm.nih.gov/40417555/)

**Tags:** backdoor, EHR, fine-tuning, poisoning
