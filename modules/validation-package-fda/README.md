# Open QMS — validation-package-fda market overlay

The **US market dial** for the P2 validation family. Refines the neutral [`validation-package`](../validation-package/) baseline with:

- **FDA Computer Software Assurance (CSA)** — final guidance (2026-02-03): intended-use classification (V.A.1), high-process-risk determination (V.A.2), risk-commensurate assurance + Table 1 tiers (V.A.4), the assurance record (V.A.6), and software-change handling (V.A.3). For production/QMS software, CSA **supersedes Section 6** of the General Principles of Software Validation.
- **21 CFR Part 11** — electronic-records/signature controls and the §V.B applicability determination.
- **21 CFR Part 820 (QMSR)** — the predicate, which incorporates ISO 13485:2016 by reference (effective 2026-02-02), placing the validation obligations at ISO 13485 §4.1.6/§7.5.6/§7.6.

## Compose it

```
openqms validate --module validation-package --module validation-package-fda
openqms validate --module medical-devices --module validation-package --module validation-package-fda
```

The CSA clauses bind to the baseline's Assurance Determination, Assurance Record, System Inventory, VMP, and Change Assessment templates (the FDA framing lives in those documents); Part 11 controls bind to a dedicated `ELECTRONIC-RECORDS-CONTROLS-TEMPLATE`. Rigor stays a **per-function determination output** — classic **CSV is the robust-scripted tier**, not a separate module.

EU adopters use [`validation-package-eu`](../validation-package-eu/) instead (or compose both for US+EU products). See `BUSINESS/companion_p2_validation_package.md`.
