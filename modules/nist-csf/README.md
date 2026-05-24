# nist-csf — Open QMS cross-cutting overlay

NIST Cybersecurity Framework v2.0 (Feb 2024) overlay. Composes with any vertical.

## Scope

General-purpose cybersecurity framework widely adopted across US public + private sector. v2.0 (Feb 2024) added the GOVERN function and expanded scope beyond critical infrastructure.

## Standards covered

PUBLIC license (NIST):

- NIST CSF v2.0

7 clauses across the 6 functions + profiles/tiers:

| Function | Code | Topic |
|---|---|---|
| **Govern (NEW in v2.0)** | GV | Org context + risk strategy + roles + policies + C-SCRM + oversight |
| Identify | ID | Asset management + business environment + risk assessment |
| Protect | PR | Identity + auth + access + awareness + data + platform security |
| Detect | DE | Continuous monitoring + adverse event analysis |
| Respond | RS | Incident management + analysis + communication + mitigation |
| Recover | RC | Recovery plan execution + communication + lessons learned |
| Profiles + Tiers | | Current vs. Target Profile gap analysis; Tier 1-4 maturity (Partial / Risk Informed / Repeatable / Adaptive) |

## Composition

```bash
openqms validate --module <vertical> --module nist-csf
# Common: with ISO 27001 for ISMS + CSF for risk-management framework
openqms validate --module manufacturing --module nist-csf --module iso-27001
```

## When to use

Any organization seeking a general-purpose cybersecurity risk-management framework. US federal contractors increasingly required to demonstrate NIST CSF alignment.

## When NOT to use

Organizations with specific framework mandates (HIPAA = HITRUST CSF or HIPAA Security Rule direct; payment = PCI DSS; DoD = CMMC) may not need NIST CSF in addition — though NIST CSF cross-references most major frameworks.

## Standards licensing

PUBLIC.

## Forward work

- NIST SP 800-53 detailed control catalog overlay (much more granular than CSF; ~1000 controls)
- NIST Privacy Framework v1.0 sibling overlay
- NIST CSF Quick Start Guide workflow template
