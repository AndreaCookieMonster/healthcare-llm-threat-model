---
layout: default
title: Declining medical safety disclaimers in GenAI models
description: Safety disclaimers in general-purpose medical chatbots are eroding over time, increasing clinical risk.
permalink: /additions/2025-10/declining-safety-disclaimers/
---

# Declining medical safety disclaimers in GenAI models

**Why it matters (impact)**  
Across 2022–2025, medical disclaimers in LLM/VLM outputs fell to ~1%. As capability grew, safety messaging dropped—raising misuse/overreliance risk in patient-facing and clinician-adjacent contexts.

**OWASP LLM Top-10 mapping**  
- LLM02: Insecure Output Handling  
- LLM09: Overreliance

**Mitigations**  
- Enforce policy-driven, context-aware disclaimers and escalation language for clinical risk categories.  
- Governance tests: block production when disclaimer rates fall below thresholds for high-risk intents.

**Evidence (peer-reviewed)**  
- PubMed: PMID **41038984**, “A longitudinal analysis of declining medical safety messaging in generative AI models,” *npj Digit Med* 2025;8:592. PMCID **PMC12491556**. DOI: 10.1038/s41746-025-01943-1.  
  https://pubmed.ncbi.nlm.nih.gov/41038984/

**Tags:** safety, governance, disclaimers, patient-facing
