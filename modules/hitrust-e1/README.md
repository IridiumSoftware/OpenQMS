# HITRUST e1 Essentials — Open QMS sub-overlay

Sub-overlay on the `hitrust-csf` cross-cutting overlay. **HITRUST e1 (Essentials) 1-year assessment** — 44 controls covering cyber-hygiene baseline.

## Composition

`hitrust-csf + hitrust-e1`. Mutually exclusive with hitrust-i1 / hitrust-r2.

## When to use

- Startups / small healthcare-tech needing rapid HIPAA-aligned attestation at lower cost than i1/r2
- Sub-contractors to i1/r2-assessed primes needing flow-down attestation
- Lower-risk vendors whose customers accept e1 in vendor-management programs

## When NOT to use

- Material PHI processing / large covered entities → `hitrust-i1` minimum, typically `hitrust-r2`
- Enterprise-customer procurement gating on i1 or r2 (most common enterprise reality)
