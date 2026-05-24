# soc-2 — Open QMS cross-cutting overlay

AICPA SOC 2 Trust Services Criteria overlay. Composes with any vertical.

## Scope

US service-organization examination framework. Distinct from ISO 27001 (substantive control overlap but different assurance + attestation model — SOC 2 is CPA-firm-issued attestation under SSAE 18; ISO 27001 is certification body audit + cert).

## Standards covered

Commercial license (AICPA):

- AICPA Trust Services Criteria (TSC) 2017 — revised 2022

7 clauses:

| TSC | Required/Optional | Specifics |
|---|---|---|
| Common Criteria (CC1-CC9) | Required | Control environment + communication + risk + monitoring + control activities + logical/physical access + system operations + change management |
| **Security** | Mandatory | Foundational TSC for any SOC 2 |
| Availability | Optional | Capacity monitoring + DR + BC (composes with iso-22301) |
| Processing Integrity | Optional | System completeness + validity + accuracy + timeliness |
| Confidentiality | Optional | Designated-confidential information protection (composes with iso-27001) |
| Privacy | Optional | Personal information collection/use/retention/disclosure (GDPR + CCPA + sectoral) |
| Type I vs. Type II | Examination type | Type II (period of 6-12 months operating-effectiveness) is the standard ongoing-customer expectation |

## Composition

```bash
openqms validate --module <vertical> --module soc-2
openqms validate --module <vertical> --module soc-2 --module iso-27001  # often combined
```

## When to use

US service organizations (SaaS, cloud services, payment processors, BPO) where customer contracts require SOC 2 attestation. Increasingly required for B2B technology vendors.

## When NOT to use

Non-service-organizations OR organizations exclusively certifying under ISO 27001 (different frameworks; some adopters maintain both — SOC 2 for US customers, ISO 27001 for international).

## Standards licensing

AICPA TSC commercial.

## Forward work

- SOC 1 (ICFR) overlay for service organizations where customer financial reporting is affected
- SOC 3 (general-use SOC 2 report) workflow
- Type I vs. Type II evidence-collection workflow templates
