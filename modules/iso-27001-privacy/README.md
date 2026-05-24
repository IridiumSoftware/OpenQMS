# ISO/IEC 27701:2019 PIMS — Open QMS sub-overlay

Sub-overlay on the `iso-27001` cross-cutting overlay. **Privacy Information Management System (PIMS) extension** per ISO/IEC 27701:2019.

## Scope

Extension to ISO/IEC 27001 (ISMS) + ISO/IEC 27002 (controls). Adds requirements for PII controllers + PII processors. Internationally recognised certification analog to a privacy management system.

## Standards covered

5 clauses across PIMS scope extension + Annex A controller controls (31) + Annex B processor controls (18) + certification extension model + GDPR/CCPA mapping.

## Composition

`iso-27001 + iso-27001-privacy`. **Strong complement to the `privacy` cross-cutting overlay** (GDPR + CCPA) — privacy encodes legal-framework obligations; iso-27001-privacy encodes the certifiable management-system to operationalise them.

Typical compositions:
- `iso-27001 + iso-27001-privacy + privacy` (most natural — ISMS + PIMS + legal framework)
- `iso-27001 + iso-27001-privacy + iso-27001-cloud` (cloud SaaS processing PII)
- `iso-27001 + iso-27001-privacy + hitrust-csf + privacy` (healthcare SaaS — HITRUST internal mapping reinforced)

## Certification path

PIMS certification is an **EXTENSION** to ISO/IEC 27001 certification, NOT standalone:
1. Hold valid ISO/IEC 27001 certification
2. Expand ISMS scope to include PII processing as PIMS scope
3. Pursue combined ISMS + PIMS audit
4. Certifying body issues combined certificate

## When to use

- Adopters with ISO/IEC 27001 certification + processing material PII
- GDPR adopters seeking certification-based compliance demonstration
- B2B providers where enterprise customers require PIMS certification
- Multi-jurisdiction privacy operators wanting single ISMS+PIMS framework

## When NOT to use

- No existing 27001 certification (pursue 27001 first; PIMS extension impossible standalone)
- Very limited PII processing where 27001 alone + privacy overlay sufficient

## Standards licensing

ISO/IEC 27701:2019 commercial. ISO/IEC 27001:2022 commercial.
