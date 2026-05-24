# CMMC Level 1 — Open QMS sub-overlay

Sub-overlay on the `cmmc` cross-cutting overlay. **CMMC Level 1 — Basic Safeguarding** per 32 CFR Part 170 § 170.14(c)(1) + FAR 52.204-21.

## Scope

DoD contractors handling **Federal Contract Information (FCI)** but NOT Controlled Unclassified Information (CUI). FCI per FAR 52.204-21(a) — info not marked as public AND provided by or generated for the Government under contract.

## Standards covered

5 clauses across CMMC Level 1 framework:
- FAR 52.204-21 17 basic safeguarding requirements
- Scope — FCI vs CUI distinction
- Annual self-assessment + SPRS scoring + senior official affirmation
- No POAM allowance at Level 1
- DFARS 7012 vs 7021 applicability

## Composition

`defense-cui + cmmc + cmmc-level-1`. Note: defense-cui targets CUI handlers per DFARS 252.204-7012 — Level 1 contractors handling ONLY FCI do not necessarily need defense-cui's NIST SP 800-171 scope; `cmmc + cmmc-level-1` alone may suffice. Self-assessing organisations confirm scope before adopting both.

## Assessment regime

- **Annual self-assessment** by the contractor
- SPRS score entered
- Senior official affirmation per § 170.16
- No third-party C3PAO assessor required
- No POAM allowance — all 17 requirements MET at assessment time

## When to use

- DoD contractor processing FCI only (not CUI)
- Sub-contractor receiving Level 1 flow-down from prime
- Pre-contract self-assessment for FCI-bearing solicitations

## When NOT to use

- Processing CUI → use cmmc-level-2 instead
- Handling national-security-critical CUI → use cmmc-level-3
- Non-DoD federal contract (FAR 52.204-21 still applies to most fed contracts but CMMC certification is DoD-specific)
