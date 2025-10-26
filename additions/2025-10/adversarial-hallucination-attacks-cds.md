# Adversarial hallucination attacks in clinical decision support

**Why it matters (impact)**  
Planting a single fabricated detail inside a clinical vignette induces models to elaborate the falsehood (50–82% baseline across models). Temperature tweaks didn’t help; mitigation prompts reduced but didn’t eliminate risk.

**OWASP LLM Top-10 mapping**  
- LLM01: Prompt Injection (indirect)  
- LLM02: Insecure Output Handling  
- LLM09: Overreliance

**Mitigations**  
- Structured input validation (strict schemas) to strip disallowed entities and confront contradictions.  
- Forced-citation with retrieval-checking for high-risk claims; adversarial evaluation sets in acceptance tests.  
- UI guardrails that flag/require justification for “new facts” not present in source data.

**Evidence (peer-reviewed)**  
- PubMed: PMID **40753316**, “Multi-model assurance analysis showing large language models are highly vulnerable to adversarial hallucination attacks during clinical decision support,” *Communications Medicine* 2025;5(1):330. PMCID **PMC12318031**. DOI: 10.1038/s43856-025-01021-3.  
  https://pubmed.ncbi.nlm.nih.gov/40753316/ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12318031/

**Tags:** adversarial, hallucination, cds, safety
