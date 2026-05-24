# ISO/IEC 27017:2015 Cloud Services — Open QMS sub-overlay

Sub-overlay on the `iso-27001` cross-cutting overlay. **Code of practice for information security controls based on ISO/IEC 27002 for cloud services** per ISO/IEC 27017:2015.

## Scope

Applies to BOTH cloud service providers (CSPs) AND cloud service customers (CSCs). Extends ISO/IEC 27002 controls with 37 cloud-specific guidance items + 7 new cloud-specific controls (CLD.6.3.1, CLD.8.1.5, CLD.9.5.1, CLD.9.5.2, CLD.12.1.5, CLD.12.4.5, CLD.13.1.4).

## Standards covered

6 clauses across cloud shared-responsibility model + 4 cloud-specific control areas + customer-side supplementary responsibilities.

## Composition

`iso-27001 + iso-27001-cloud`. Often paired with `iso-27001 + iso-27001-cloud + iso-27001-privacy` for cloud services processing personal data.

## When to use

- Cloud service provider seeking 27017 attestation alongside 27001
- Cloud service customer adopting due-diligence framework for CSP selection + ongoing CSP management
- SaaS company with material cloud-infrastructure footprint
- Customer-of-CSP for whom shared-responsibility-model documentation is required by regulator or enterprise customer

## When NOT to use

- Pure on-premises infrastructure with no cloud component
- Adopters using cloud only for non-sensitive workloads (cost may not justify; verify customer/regulator expectations)

## Standards licensing

ISO/IEC 27017:2015 commercial. ISO/IEC 27001:2022 commercial (already required by parent overlay).
