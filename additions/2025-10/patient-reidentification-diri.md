---
layout: default
title: Adversarial re-identification on de-identified clinical text (DIRI)
description:
  Targeted prompts can re-identify patients from supposedly de-identified clinical narratives.
---

# Adversarial re-identification on de-identified clinical text (DIRI)

**Why it matters (impact)**  
Demonstrates that LLMs can facilitate adversarial re-identification against de-identified notes,
challenging naïve assumptions about text anonymization when models infer latent identifiers.

**OWASP LLM Top-10 mapping**

- LLM06: Sensitive Information Disclosure
- LLM02: Insecure Output Handling

**Mitigations**

- Layered de-identification (rule-based + ML) plus risk-based release; red-teaming with
  re-identification probes before data sharing.
- Minimize model access to longitudinal context unless essential; apply privacy-attacks testing in
  ML governance.

**Evidence (preprint, NIH-indexed)**

- [DIRI: Adversarial Patient Reidentification with Large Language Models for Evaluating Clinical Text Anonymization (arXiv 2025)](https://pubmed.ncbi.nlm.nih.gov/40502277/)

**Tags:** privacy, re-identification, de-identification, PHI
