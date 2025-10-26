# Training-data poisoning of medical LLMs

**Why it matters (impact)**  
Small, targeted poisoning of medical corpora can implant persistent harmful behaviors and degrade safety—high leverage for adversaries given open data pipelines and fine-tuning trends.

**OWASP LLM Top-10 mapping**  
- LLM03: Training Data Poisoning  
- LLM05: Supply Chain Vulnerabilities

**Mitigations**  
- Curate signed/provenanced datasets; poisoning-resistant training pipelines with outlier/gradient-based screening.  
- Canary prompts and poison-trigger scans post-train; quarantine fine-tunes without clean eval on red-team suites.

**Evidence (peer-reviewed)**  
- PubMed: PMID **39779928**, “Medical large language models are vulnerable to data-poisoning attacks,” *Nat Med* 2025;31(2):618-626. PMCID **PMC11835729**. DOI: 10.1038/s41591-024-03445-1.  
  https://pubmed.ncbi.nlm.nih.gov/39779928/

**Tags:** poisoning, supply-chain, training, fine-tuning
