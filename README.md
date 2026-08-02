# Global Insurance Underwriting Handbook

A comprehensive, multi-volume professional reference for insurance underwriting — covering fundamentals, personal and commercial lines, rating and pricing, policy administration, claims, and regulation across US and UK markets.

## Repository Structure

```
├── docs/                          # Handbook content (MkDocs source)
│   ├── index.md                   # Handbook home / table of contents
│   ├── glossary.md                # Terminology glossary (A–Z)
│   ├── abbreviations.md           # Common abbreviations & acronyms
│   ├── volume-01-fundamentals/    # Insurance principles & the industry
│   ├── volume-02-personal/        # Auto, home, life, health, personal umbrella
│   ├── volume-03-commercial/      # Property, liability, BOP, marine, cyber…
│   ├── volume-04-underwriting/    # UW process, risk assessment, file management
│   ├── volume-05-rating-pricing/  # Manual rating, experience rating, loss ratios
│   ├── volume-06-admin/           # Policy issuance, endorsements, renewals, TAs
│   ├── volume-07-claims/          # FNOL, investigation, subrogation, fraud
│   ├── market-us/                 # US regulatory & state-specific guidance
│   ├── market-uk/                 # UK (FCA/PRA) regulatory guidance
│   ├── templates/                 # Proposal forms, checklists, templates
│   └── guidelines/                # Sample underwriting guidelines by line
├── mkdocs.yml                     # MkDocs site configuration
└── LICENSE                        # MIT License
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

## License

MIT — see [LICENSE](LICENSE).

## Disclaimer

This handbook is an educational reference. It does not constitute legal, actuarial, or regulatory advice. Coverage forms, rates, rules and regulations vary by jurisdiction and insurer; always consult the applicable policy form, rate filing, and regulator before making underwriting decisions.