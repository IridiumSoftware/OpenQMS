# CMMC Level 2 — Open QMS sub-overlay

Sub-overlay on the `cmmc` cross-cutting overlay. **CMMC Level 2 — Advanced** per 32 CFR Part 170 §170.14(c)(2) aligned with NIST SP 800-171 Rev 3.

## Scope

DoD contractors processing **Controlled Unclassified Information (CUI)** per 32 CFR Part 2002 NARA CUI Registry.

## Standards covered

6 clauses spanning the 110 NIST SP 800-171 requirements across 14 control families + CMMC-specific assessment + SPRS scoring + DFARS 7012 incident reporting.

## Assessment regime — BIFURCATED

| Acquisition type | Assessment | Cadence |
|---|---|---|
| Non-prioritized | Self-assessment per §170.16 | Annual + senior official affirmation |
| Prioritized (DoD-designated national-security-critical) | C3PAO per §170.17 | Every 3 years + interim self-assessment |

## Composition

`defense-cui + cmmc + cmmc-level-2`. defense-cui provides the NIST SP 800-171 baseline + SPRS scoring + 72h DIBNet incident reporting; cmmc adds CMMC 2.0 certification regime; cmmc-level-2 adds the Level-2-specific POAM + self-vs-C3PAO bifurcation.

## POAM allowance

- Up to **5% of requirements** may be conditionally certified with Plans of Action + Milestones
- "Conditional CMMC Status Level 2" valid 180 days from assessment + 1 close-out assessment for full status
- Highest-weight requirements (per §170.24 SPRS weights) NOT POAM-eligible — must be MET at assessment

## When to use

- DoD contractor handling CUI
- Pre-contract for CUI-bearing solicitations
- Sub-contractor receiving Level 2 flow-down from prime

## When NOT to use

- FCI-only → use cmmc-level-1
- National-security-critical CUI requiring Advanced controls → use cmmc-level-3
- Non-DoD federal contracts (CMMC is DoD-specific)
