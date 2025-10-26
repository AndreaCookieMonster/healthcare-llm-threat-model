# LLM-based radiology report anonymization pitfalls

**Why it matters (impact)**  
Comparative evaluations show mixed de-identification performance and risk of over-redaction (loss of clinical signal) or under-redaction (PHI leakage) when using general-purpose LLMs—unsafe to “drop-in replace” traditional anonymizers.

**OWASP LLM Top-10 mapping**  
- LLM06: Sensitive Information Disclosure  
- LLM02: Insecure Output Handling

**Mitigations**  
- Prefer specialized de-ID pipelines with high-recall PHI detectors + calibrated post-processing.  
- Human QA for releases; require dataset-specific measurement of PHI recall/precision and leakage drills.

**Evidence (peer-reviewed)**  
- PubMed: PMID **39480533**, “Automated anonymization of radiology reports: comparison of publicly available NLP and large language models,” *Int J Med Inform* 2024.  
  https://pubmed.ncbi.nlm.nih.gov/39480533/

**Tags:** privacy, de-identification, radiology, PHI
