# Global Insurance Underwriting Handbook

A comprehensive, multi-volume professional reference for insurance underwriting — covering fundamentals, personal and commercial lines, rating and pricing, policy administration, claims, regulation, technology platforms, reinsurance, specialty lines, fraud, and API/InsurTech integration.

## What this handbook includes

- 📚 **Book format support**: content designed for PDF and DOCX publishing.
- 🌐 **CoverBridge Knowledge Center**: centralized insurance and underwriting knowledge.
- 🎓 **Insurance Learning Academy**: structured training resources for learners.
- 🤖 **AI Insurance Assistant (retrieval-augmented generation, RAG)**: assistant-ready knowledge for retrieval-augmented responses.
- 📖 **Searchable knowledge base**: organized content for fast lookup.
- 🧠 **Underwriting decision support**: practical guidance to improve underwriting outcomes.
- 💼 **Business Analyst training portal**: material tailored for BA onboarding and upskilling.

## Repository Structure

```
├── docs/                                # Handbook content (MkDocs source)
│   ├── index.md                         # Handbook home / table of contents
│   ├── glossary.md                      # Terminology glossary (A–Z)
│   ├── abbreviations.md                 # Common abbreviations & acronyms
│   ├── overview/                        # Scope & about underwriting
│   ├── volume-01-fundamentals/          # Insurance principles & the industry
│   ├── volume-02-personal/              # Auto, home, life, health, umbrella
│   ├── volume-03-commercial/            # Property, liability, BOP, specialty
│   ├── volume-04-underwriting/          # UW process, risk assessment (COPE)
│   ├── volume-05-rating-pricing/        # Pricing, classification, analytics
│   ├── volume-06-policy-administration/ # Issuance, endorsements, renewals
│   ├── volume-07-claims/                # FNOL, investigation, subrogation
│   ├── volume-08-us-market/             # US regulatory & market guidance
│   ├── volume-09-uk-market/             # UK (FCA/PRA) regulatory guidance
│   ├── volume-10-guidewire/             # Guidewire platform volumes
│   ├── volume-11-duck-creek/            # Duck Creek platform volumes
│   ├── volume-12-majesco/               # Majesco platform volumes
│   ├── volume-13-business-analyst/      # Business Analyst training
│   ├── volume-14-ai-insurance/          # AI in insurance
│   ├── volume-15-reinsurance/           # Reinsurance treaties, pricing
│   ├── volume-16-specialty-insurance/   # Aviation, marine, energy, and more
│   ├── volume-17-fraud/                 # Fraud detection & investigation
│   ├── volume-18-api-insurtech/         # APIs & InsurTech integration
│   ├── underwriting-checklists/         # Submission & LOB checklists
│   ├── proposal-forms/                  # Proposal & application forms
│   ├── clause-library/                  # Exclusion, limitation, condition clauses
│   ├── decision-trees/                  # Referral & risk decision guides
│   ├── references/                      # Regulators, bodies, vendors
│   ├── case-studies/                    # Worked scenarios
│   └── industry-data/                   # Loss ratios, premiums, fraud context
├── scripts/                             # Content generation utilities
├── templates/                           # Reusable template markdown
├── mkdocs.yml                           # MkDocs site configuration
├── index.html                           # GitHub Pages redirect
└── LICENSE                              # MIT License
```

## How to Use This Handbook

- **Browse online** — build the site with [MkDocs](https://www.mkdocs.org/) (`mkdocs serve`).
- **Browse as files** — all content is plain Markdown, readable in any editor or viewer.
- **Download a volume** — each volume lives in its own folder; copy or print as needed.

## Build the Documentation Site

Requires Python 3.8+ and pip.

```bash
pip install mkdocs
mkdocs serve          # local preview at http://127.0.0.1:8000
mkdocs build          # output to ./site
```

## Regenerate Generated Content

The generated volumes and knowledge-base sections are produced by scripts in `scripts/`:

```bash
python scripts/generate_volume16.py        # specialty insurance chapters
python scripts/generate_volume17.py        # fraud chapters
python scripts/generate_volume18.py        # API & InsurTech chapters
python scripts/generate_knowledge_base.py  # references, case studies, industry data
```

## License

MIT — see [LICENSE](LICENSE).

## Disclaimer

This handbook is an educational reference. It does not constitute legal, actuarial, or regulatory advice. Coverage forms, rates, rules and regulations vary by jurisdiction and insurer; always consult the applicable policy form, rate filing, and regulator before making underwriting decisions.