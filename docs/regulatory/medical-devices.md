# Medical Devices Regulatory Module

This module maps Open QMS capabilities to medical device regulations and standards.

## Standards covered

- **ISO 13485:2016** — Quality management systems for medical devices
- **21 CFR Part 820** — FDA Quality System Regulation
- **21 CFR Part 11** — Electronic records and electronic signatures
- **EU MDR 2017/745** — Regulation on medical devices
- **IEC 62304:2006+A1:2015** — Medical device software lifecycle
- **IEC 62366-1:2015+A1:2020** — Usability engineering

## Strengths

GitHub-based QMS is strongest for:

- **IEC 62304 software lifecycle** (§5.5, §8): Git IS configuration management. Code review, CI testing, and release management are native.
- **Design control traceability** (ISO 13485 §7.3, 820.30): Issue-to-PR linking provides built-in traceability when used consistently.
- **Document version control** (ISO 13485 §4.2.4, 820.40): Git provides complete, immutable revision history.

## Known gaps

The following require supplementary controls:

- **Part 11 electronic signatures**: PR approval shows who and when, but not the regulatory "meaning" of the signature. Supplement with GPG signing and structured commit messages that include role and meaning.
- **Point-of-use access for manufacturing**: Production personnel need rendered documents, not Git repositories. Use the MkDocs site or PDF rendering.
- **Formal design review records**: PR comments capture discussion but may not constitute formal design review minutes. Supplement with structured review templates.
- **Complaint and adverse event records**: May contain PHI/PII requiring access controls beyond standard repository permissions.

## Recommended repository structure for medical devices

```
my-org/
├── qms/                    # This repo — SOPs, policies, forms
├── product-alpha-dhf/      # Design history file for Product Alpha
├── product-alpha-sw/       # Software repo for Product Alpha (IEC 62304)
├── product-alpha-risk/     # Risk management file (ISO 14971)
└── qms-complaints/         # Access-restricted complaint records
```

Each product gets its own DHF repo. The QMS repo holds organization-level procedures. Complaint records are separated for access control.
