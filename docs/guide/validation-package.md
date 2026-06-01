# Computerized-system validation (validation-package)

Risk-based validation of the software you use to **run production or your QMS** — not the device software itself. Grounded in FDA's **Computer Software Assurance (CSA)** framework (final guidance, 2026-02-03), GAMP 5 (2nd ed.), and ISO 13485 §4.1.6 / §7.5.6 / §7.6.

## It's not "CSV vs CSA"

CSA defines one **risk-based spectrum**. Classic **CSV — robust scripted IQ/OQ/PQ — is the highest assurance tier** within it, applied to high-risk functions. So you don't choose a methodology per system; you make a **per-function risk determination** and the tier falls out of it:

| Tier | When | ≈ |
|---|---|---|
| Scripted — robust | high process risk | classic CSV / IQ-OQ-PQ |
| Scripted — limited | moderate | lighter CSV |
| Unscripted — scenario / error-guessing | lower | — |
| Unscripted — exploratory | lower | — |

The risk→tier mapping is **not rigid** (CSA §V.A.4) — the determination records your judgment.

## How to use it

1. **Compose the module** for your market:
   ```
   openqms validate --module medical-devices --module validation-package --module validation-package-fda
   ```
   The **FDA** overlay (`validation-package-fda` — CSA framework + 21 CFR Part 11 + Part 820/QMSR predicate) ships now; the **EU** overlay (`validation-package-eu` — Annex 11/15) arrives in P2.3. Compose both for US+EU products. The overlay sets the regulatory framing — the CSA clauses bind to the same Assurance Determination / Record templates, and Part 11 e-records/e-sig controls land in `ELECTRONIC-RECORDS-CONTROLS-TEMPLATE`.

2. **Inventory** your computerized systems (`SYSTEM-INVENTORY-TEMPLATE`) — classify each by intended use (directly / support / not part of production-or-QMS) and GAMP category.

3. **Determine assurance per function** (`ASSURANCE-DETERMINATION-TEMPLATE`) — FDA's 5-column table: function → intended use → risk analysis → tier. *High process risk* = failure foreseeably compromises safety.

4. **Specify requirements** (`URS-TEMPLATE`) and **record assurance** (`ASSURANCE-RECORD-TEMPLATE`, tier-aware) — the record carries intended use, risk result, testing, issues, conclusion, who/when, and approval where appropriate (CSA §V.A.6).

5. **Plan and maintain** (`VALIDATION-MASTER-PLAN-TEMPLATE`, `CHANGE-ASSESSMENT-TEMPLATE`) — VMP scope/approach + change-driven revalidation + periodic review.

## What it does and doesn't do

It ships the framework, the determination, the tier-aware record, and the traceability — and (with P15) proves the artifact set matches each declared tier. It does **not** decide whether a function is high-risk, nor prove a system is fit for use. Those are your QA judgment (OQ-080).

See `BUSINESS/companion_p2_validation_package.md` for the full design and the FDA-vs-EU market overlays.
