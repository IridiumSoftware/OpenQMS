# defense-cui — Open QMS cross-cutting overlay

US DoD Controlled Unclassified Information (CUI) handling per DFARS 252.204-7012 + NIST SP 800-171 Rev 3 (May 2024). Composes with any vertical (typically aerospace-defense + automotive-defense + other DoD-customer scopes).

## Scope

DoD contractors + subcontractors handling Covered Defense Information (CDI). CDI = unclassified controlled technical information OR other information requiring safeguarding/dissemination controls per law/regulation/government-wide policy AND collected/developed/received/transmitted/used/stored by contractor in support of contract.

## Standards covered

PUBLIC license:

- DFARS 252.204-7012 (DoD contract clause)
- NIST SP 800-171 Rev 3 (May 2024)

6 clauses:

| Element | Specifics |
|---|---|
| DFARS 7012 applicability | Included in all DoD contracts (except COTS); CDI definition |
| NIST SP 800-171 implementation | Self-assessment + 110-point SPRS score; POAM acceptable for deficiencies with timeline |
| Cyber incident reporting | **72 hours** to DoD CIO via DIBNet Portal; 90-day media preservation; forensics cooperation |
| NIST SP 800-171 14 families | AC / AT / AU / CM / IA / IR / MA / MP / PS / PE / RA / CA / SC / SI |
| SSP + POAM artifacts | System Security Plan describes system + boundary + implemented controls; POAM = remediation roadmap; SPRS score |
| CUI marking + handling | Per 32 CFR 2002 + category markings (CUI//SP-EXPT, CUI//SP-LEI); training; destruction per NIST SP 800-88 |

## Composition

```bash
openqms validate --module <vertical> --module defense-cui
# Common DoD aerospace contractor:
openqms validate --module aerospace --module aerospace-defense --module defense-cui --module cmmc
```

## When to use

DoD prime contractors + subcontractors handling CDI. Effectively required for any non-COTS DoD contract.

## When NOT to use

Non-DoD contractors. COTS-only DoD relationships (DFARS 7012 exempt).

## Standards licensing

PUBLIC.

## Forward work

- 32 CFR 2002 CUI Program standalone overlay (broader than DoD scope — applies to all federal agencies)
- Detailed per-family SSP template (NIST SP 800-171 14 families × ~110 controls)
- POAM workflow template
- SPRS-score calculation worksheet
