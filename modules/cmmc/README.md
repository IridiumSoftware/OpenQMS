# cmmc — Open QMS cross-cutting overlay

Cybersecurity Maturity Model Certification 2.0 overlay. Per 32 CFR Part 170 final rule (Dec 2024) with phased rollout 2025-2028. Composes with any vertical.

## Scope

DoD contractors handling Federal Contract Information (FCI) and/or Controlled Unclassified Information (CUI). Effectively required for non-COTS DoD relationships — CMMC adds certification verification on top of defense-cui's NIST SP 800-171 baseline.

## Standards covered

PUBLIC license:

- CMMC 2.0 (32 CFR Part 170)

6 clauses across the 3 levels + process elements:

| Element | Specifics |
|---|---|
| **Level 1 (Foundational)** | 17 practices from FAR 52.204-21; FCI only; annual self-assessment + senior affirmation |
| **Level 2 (Advanced)** | 110 practices = NIST SP 800-171 Rev 3; CUI; triennial C3PAO certification for national-security-critical CUI; self-assessment + senior affirmation where DoD permits |
| **Level 3 (Expert)** | Level 2 + 24 additional NIST SP 800-172 practices; most sensitive CUI; triennial government assessment |
| C3PAO assessment process | Engagement → readiness → assessment → QA → Cyber-AB authorization → DoD upload; CCP / CCA / CCAI certified lead assessors; SPRS + eMASS reporting |
| POAM allowance | Limited POAM at Level 2; specific controls (MFA, FIPS crypto) cannot be POAMed; 180-day max remediation |
| Phased rollout | DFARS 252.204-7021 progressive implementation through 2028 |

## Composition

```bash
openqms validate --module <vertical> --module cmmc
# Typical DoD contractor full stack:
openqms validate --module aerospace --module aerospace-defense --module defense-cui --module cmmc --module iso-27001
```

## When to use

Any DoD contractor or subcontractor handling FCI/CUI. Required for contract eligibility per DFARS 252.204-7021 (phased per contract solicitation).

## When NOT to use

Non-DoD organizations; COTS-only DoD relationships. Use defense-cui alone if NIST SP 800-171 compliance is required without formal CMMC certification (rare — most DoD contracts require both).

## Standards licensing

PUBLIC.

## Forward work

- Per-Level detailed control mapping (Level 1 17 / Level 2 110 / Level 3 134 controls)
- C3PAO assessment readiness template (engagement → readiness → mock assessment → final)
- SPRS score calculation + eMASS submission workflow
- Subcontractor CMMC flow-down template (prime contractor responsibility per DFARS 252.204-7019)
