#!/usr/bin/env python3
"""Repair broken cross-reference links found by `mkdocs build --strict`.

Fixes two classes of issues:
1. Double `.md.md` extensions (introduced by generate_volume16.py).
2. Legacy links to renamed directories / files (volume-06-admin, market-us,
   market-uk, guidelines, old volume-07 claims filenames, etc.).
"""
import pathlib

DOCS = pathlib.Path("docs")
FIXES = {
    # Double extension bug
    ".md.md": ".md",
    # Renamed directories / files
    "../guidelines/index.md": "../volume-04-underwriting/09-underwriting-guidelines.md",
    "../market-us/index.md": "../volume-08-us-market/index.md",
    "../market-uk/index.md": "../volume-09-uk-market/index.md",
    "../volume-06-admin/01-policy-documents.md": "../volume-06-policy-administration/01-policy-lifecycle.md",
    "../volume-06-admin/01-policy-issuance.md": "../volume-06-policy-administration/02-policy-issuance.md",
    "../volume-06-admin/05-renewals.md": "../volume-06-policy-administration/04-renewals.md",
    "../volume-06-admin/06-transactional-accuracy.md": "../volume-06-policy-administration/06-premium-handling-audits.md",
    "../volume-06-admin/index.md": "../volume-06-policy-administration/index.md",
    "../volume-07-claims/02-claims-process.md": "../volume-07-claims/02-notification-investigation.md",
    "../volume-07-claims/04-loss-evaluation.md": "../volume-07-claims/04-claims-resolution.md",
    "../volume-07-claims/05-subrogation-recoveries.md": "../volume-07-claims/06-reinsurance-subrogation.md",
    "../volume-05-rating-pricing/05-loss-ratios-profitability.md": "../industry-data/loss-ratios.md",
    "../volume-04-underwriting/07-underwriting-management.md": "../volume-04-underwriting/07-portfolio-management.md",
    "../volume-03-commercial/03-commercial-auto.md": "../volume-03-commercial/04-commercial-auto.md",
    "06-premium-handling.md": "06-premium-handling-audits.md",
}

changed = 0
for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in FIXES.items():
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"fixed: {path}")
        changed += 1

print(f"\n{changed} file(s) repaired.")