---
id: LLM01
title: 'Prompt Injection'
slug: 'llm01--prompt-injection'
summary: 'Malicious prompts cause tools and connectors to leak PHI or perform unsafe actions.'
tags: ['injection', 'workflow', 'healthcare']
last_updated: '2025-03-17'
healthcare_note: 'Malicious prompts cause tools/connectors to leak PHI or perform unsafe actions.'
cve_window: 'last-24-months'
resources:
  - title: 'Prompt injection attacks on vision-language models in oncology (Nat Commun 2025)'
    url: 'https://doi.org/10.1038/s41467-024-55631-x'
  - title:
      'Prompt injection attacks on vision-language models for surgical decision support (medRxiv
      2025)'
    url: 'https://doi.org/10.1101/2025.07.16.25331645'
  - title:
      'Multi-model assurance analysis showing large language models are highly vulnerable to
      adversarial hallucination attacks during clinical decision support (Commun Med 2025)'
    url: 'https://doi.org/10.1038/s43856-025-01021-3'
  - title: 'Medical VLM prompt injection (oncology)'
    url: '/additions/2025-10/vlm-prompt-injection-oncology/'
  - title: 'Surgical video VLM prompt injection'
    url: '/additions/2025-10/vlm-prompt-injection-surgical-video/'
  - title: 'Adversarial hallucination attacks in CDS'
    url: '/additions/2025-10/adversarial-hallucination-attacks-cds/'
---

## CVE entries (last 24 months)

_None identified that are both AI-specific and healthcare-specific._ Capture non-CVE incidents
(e.g., red-teaming findings) so governance can act.

## References

- Oncology exploit chain: [Nat Commun 2025 study][llm01-onc]
- OR workflow preprint: [Surgical VLM medRxiv preprint][llm01-surg]
- Assurance findings: [Commun Med 2025 assurance analysis][llm01-assurance]
- Field report:
  [Medical VLM prompt injection (oncology)]({{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-oncology/)
- Surgical case study:
  [Surgical video VLM prompt injection]({{ site.baseurl }}/additions/2025-10/vlm-prompt-injection-surgical-video/)
- Governance signal:
  [Adversarial hallucination attacks in CDS]({{ site.baseurl }}/additions/2025-10/adversarial-hallucination-attacks-cds/)

[llm01-onc]: https://doi.org/10.1038/s41467-024-55631-x
[llm01-surg]: https://doi.org/10.1101/2025.07.16.25331645
[llm01-assurance]: https://doi.org/10.1038/s43856-025-01021-3
