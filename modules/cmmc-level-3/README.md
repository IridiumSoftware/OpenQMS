# CMMC Level 3 — Open QMS sub-overlay

Sub-overlay on the `cmmc` cross-cutting overlay. **CMMC Level 3 — Expert** per 32 CFR Part 170 §170.14(c)(3) — additional 24 NIST SP 800-172 enhanced requirements targeting APT protection.

## Scope

DoD contractors handling CUI designated as **national-security-critical** where unauthorised disclosure consequences would be catastrophic. DoD CIO + AOAP designates contracts requiring Level 3.

## Assessment regime

**DIBCAC (Defense Industrial Base Cybersecurity Assessment Center)** — DCMA-organisation-conducted; NOT C3PAO-delegable. Most rigorous CMMC regime.

| Item | Detail |
|---|---|
| Assessor | DIBCAC (DCMA) |
| Cadence | Every 3 years + interim risk monitoring |
| POAM allowance | NONE — all 134 requirements MET |
| Threat intel integration | NSA + DC3 cyber threat feeds |

## Standards covered

5 clauses across NIST SP 800-172 enhanced requirements + DIBCAC assessment regime + no-POAM constraint + additional protections.

## Composition

`defense-cui + cmmc + cmmc-level-2 + cmmc-level-3`. Level 3 is ADDITIVE to Level 2 — adopters must satisfy all 110 Level 2 requirements PLUS the 24 enhanced requirements. Compose both sub-overlays.

## When to use

- DoD contract designated national-security-critical
- Handling CUI where unauthorised disclosure consequences would be catastrophic
- DoD-CIO-designated supply chain elements requiring APT-resistant protection

## When NOT to use

- General CUI without national-security designation → cmmc-level-2 sufficient
- FCI-only → cmmc-level-1
