# 🏥 LLM Threat Model for Healthcare

## 📄 About This Project
This project adapts the **[OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** to the **healthcare** domain — producing a **specialized threat model** that identifies, categorizes, and mitigates risks unique to medical, clinical, and public health contexts.

While OWASP's Top 10 for LLMs outlines general AI security concerns, healthcare systems operate in **high-stakes environments** where mistakes can directly impact patient safety, privacy, and trust.  
This resource bridges that gap by:

- **Mapping** each OWASP Top 10 risk to **real-world healthcare scenarios**
- **Extending** the model with **domain-specific threats** not covered in generic AI security guidance
- **Documenting mitigations** grounded in:
  - Clinical safety principles
  - Data governance best practices
  - Ethical AI deployment guidelines
- **Linking to resources** — academic research, regulatory standards, and practical implementation guides

---

## 🎯 Goals

1. **Raise awareness** of LLM-specific threats in healthcare IT and AI deployments.
2. **Provide a living, community-driven resource** for security engineers, developers, policymakers, and patient advocates.
3. **Enable safer adoption** of AI in healthcare through clear, actionable mitigations.
4. **Support compliance** with HIPAA, GDPR, HDS, and emerging AI safety regulations.

---

## 🩺 Why a Healthcare-Specific Threat Model?

Healthcare environments differ from other AI deployment contexts because:

- **Data Sensitivity:** Patient data is highly regulated and deeply personal.
- **Life-Critical Decisions:** AI errors can cause physical harm or death.
- **Complex Ecosystem:** Systems must interoperate across hospitals, insurers, labs, and research institutions.
- **Regulatory Landscape:** Compliance requirements (HIPAA, GDPR, HDS) and ethics standards are strict and often jurisdiction-specific.
- **Adversary Motivation:** Health data and systems are valuable targets for cybercrime, nation-state espionage, and corporate misuse.

---

## 📊 Structure of the Threat Catalog

Each threat entry includes:

| Field        | Description |
|--------------|-------------|
| **Threat Name** | Concise title of the risk scenario |
| **Category** | OWASP LLM Top 10 mapping + healthcare-specific classification |
| **Vector** | Attack surface or method |
| **Description** | Explanation of the threat and context |
| **Impact** | Potential consequences (clinical, legal, operational) |
| **Likelihood** | Estimated frequency or probability |
| **Severity** | Risk rating (low / medium / high) |
| **Mitigations** | Recommended controls or safeguards |
| **Detection** | How to identify exploitation or risk exposure |
| **Standards** | Related compliance or industry standards |
| **References** | Links to research, advisories, or best practices |

---

## 🔍 How to Use This Repository

1. **Browse the Threat Catalog**  
   - View online at: [GitHub Pages site](https://andreacookiemonster.github.io/healthcare-llm-threat-model/)  
   - Each entry contains embedded links to further reading.

2. **Search by OWASP Mapping**  
   - Identify which generic LLM risks align with your healthcare context.

3. **Prioritize Mitigation**  
   - Use severity and likelihood ratings to focus resources on the most urgent risks.

4. **Update Regularly**  
   - AI systems and attack vectors evolve — check back for updates or contribute your own.

---

## 🚀 Getting Started

You can consume this resource in two ways:

- **As a live reference**: Browse the [GitHub Pages site](https://andreacookiemonster.github.io/healthcare-llm-threat-model/).
- **As a dataset**: Download `data/LLM_Threat_Model_Healthcare-2.xlsx` to work with the threat model in your own tooling.

---

## 📊 Threat Catalog (Full Table)

> This table is generated from `data/LLM_Threat_Model_Healthcare-2.xlsx`  
> It includes threat descriptions, impacts, mitigations, and resource links.

*(Paste your generated table here so the README always shows the current catalog.)*

---

## 🤝 Contributing

We welcome contributions from:

- **Healthcare Security Engineers**
- **Clinicians and Researchers**
- **Patient Advocates**
- **AI Developers**
- **Policy Experts**

Ways to contribute:
- Add new threats or mitigations
- Improve resource links
- Suggest better mappings to OWASP Top 10 categories
- Flag outdated or inaccurate entries

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 🏛 Credits

- **Lead Maintainer:** Andrea Downing ([The Light Collective](https://lightcollective.org))
- **Framework:** Adapted from the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **Data & References:** Curated with input from patient advocates, clinicians, and AI safety researchers
- **License:** MIT (unless otherwise noted)

