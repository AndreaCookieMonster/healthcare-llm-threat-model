---
layout: default
title: Prompt injection on medical VLMs (oncology images)
description: Oncology-focused vision-language models can be subverted by hidden prompts embedded in clinical imagery.
permalink: /additions/2025-10/vlm-prompt-injection-oncology/
---

# Prompt injection on medical VLMs (oncology images)

**Why it matters (impact)**  
Embedded sub-visual or overlaid prompts inside medical images can reliably steer state-of-the-art VLMs (e.g., GPT-4o class) to harmful or incorrect outputs in oncology workflows—without parameter access. This is a practical supply-chain/user-content attack vector wherever external imaging or patient-submitted media enters clinical systems.

**OWASP LLM Top-10 mapping**  
- LLM01: Prompt Injection  
- LLM02: Insecure Output Handling  
- LLM05: Supply Chain Vulnerabilities

**Mitigations (pragmatic)**  
- Content provenance + image steganography scanning on ingest; block or quarantine assets with detected overlay text.  
- Strict tool/API isolation of VLM outputs from downstream systems unless validated (“human-in-the-loop” or rule-based allow-lists).  
- Defense-in-depth prompts + constrained decoding; adversarially trained detectors for overlaid/hidden text; evaluation gates before clinical use.

**Evidence (peer-reviewed & code)**
- PubMed: PMID **39890777**, “Prompt injection attacks on vision language models in oncology,” *Nat Commun* 2025;16(1):1239. PMCID **PMC11785991**. DOI: 10.1038/s41467-024-55631-x.
  https://pubmed.ncbi.nlm.nih.gov/39890777/  |  https://pmc.ncbi.nlm.nih.gov/articles/PMC11785991/
- Code: KatherLab “Prompt Injection Attacks” repo with reproducible oncology VLM exploits and evaluation scripts.
  https://github.com/KatherLab/prompt_injection_attacks

**Tags:** vlm, oncology, prompt-injection, supply-chain, patient-provided-data
