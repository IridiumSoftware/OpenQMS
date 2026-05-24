# HIPAA — Open QMS dedicated cross-cutting overlay

25th Open QMS cross-cutting overlay. **US healthcare-specific privacy + security regime** per 45 CFR Parts 160 + 164 + HITECH Act.

## Scope

US Covered Entities (CEs — health plans, healthcare clearinghouses, healthcare providers electronically transmitting HIPAA Transaction Rule data) + their Business Associates (BAs) + BAs' subcontractors.

## Why a dedicated overlay (vs subsumed in `privacy`)

The `privacy` overlay (GDPR + CCPA) doesn't map cleanly to HIPAA's structure:
- **CE/BA framework** — HIPAA's regulated-entity scope is structurally distinct from GDPR's controller/processor or CCPA's business/service-provider
- **4-rule architecture** — Privacy + Security + Breach Notification + Enforcement rules with distinct scope (Privacy Rule = all PHI; Security Rule = ePHI only)
- **OCR enforcement** — separate enforcement regime with 4-tier CMP structure + criminal penalties
- **BAA contractual framework** — §164.504(e) + §164.314 required content distinct from GDPR Article 28 DPA or CCPA §1798.140
- **HITECH-era extensions** — Security Rule + portions of Privacy Rule extended directly to BAs (was contract-only pre-HITECH)
- **Healthcare-specific provisions** — TPO permitted uses, de-identification Safe Harbor, Notice of Privacy Practices, accounting of disclosures, Authorization

## Standards covered

**2 PUBLIC standards:**
- **HIPAA** — 45 CFR Parts 160 + 164 (Privacy Rule §164.500-534 + Security Rule §164.302-318 + Breach Notification Rule §164.400-414 + Enforcement Rule §160 Subpart D + E)
- **HITECH** — Pub. L. 111-5 Title XIII + HITECH Final Rule 78 FR 5566 + Promoting Interoperability

13 clauses across the 4 rules + HITECH extensions.

## Templates introduced

4 new HIPAA-specific templates:

1. **`NPP-TEMPLATE.md`** — Notice of Privacy Practices per §164.520. Patient-facing notice covering uses + disclosures + individual rights + complaint channel + acknowledgment of receipt + revision tracking + posting requirements (physical premises + website for online-enabled CEs).

2. **`BAA-TEMPLATE.md`** — Business Associate Agreement per §164.504(e) + §164.314(a). Full required content: permitted/required uses + safeguards + reporting impermissible uses + breach 60-day notification + subcontractor flow-down + PHI return/destroy at termination + audit access.

3. **`HIPAA-RISK-ANALYSIS-TEMPLATE.md`** — Security Rule Risk Analysis per §164.308(a)(1)(ii)(A) — the foundational Security Rule artifact. System inventory + threat catalog + vulnerability assessment + likelihood×impact + control gap analysis + risk treatment + 6-year documentation retention.

4. **`HIPAA-BREACH-RISK-ASSESSMENT-TEMPLATE.md`** — 4-factor breach risk assessment per §164.402(2) presumption-rebuttal: (i) nature + extent of PHI; (ii) unauthorized recipient; (iii) actual acquisition/viewing; (iv) mitigation. Outcome drives §164.404 individual / §164.406 media (≥500) / §164.408 HHS notification decisions.

Plus 1 cross-cutting binding (SOP-TEMPLATE) for HIPAA operational SOPs (Privacy Officer + Security Officer designation + workforce training + sanctions + audit log review + incident response + BAA management + Authorization handling + de-identification methodology).

## Composition

Composes naturally with:

- **`hipaa + privacy`** — most adopters need BOTH (HIPAA for PHI; privacy for non-PHI employee + applicant + vendor data subject to GDPR/CCPA/state laws)
- **`medical-devices + hipaa`** — connected medical devices processing PHI
- **`pharma + hipaa`** — pharma adopters with clinical-trial PHI exposure (informed consent + IRB + recruitment)
- **`hipaa + hitrust-csf + hitrust-r2`** — HITRUST r2 provides validated multi-framework attestation including HIPAA + HITECH controls
- **`hipaa + soc-2 + soc-2-type-ii`** — common attestation pairing for healthcare-tech SaaS
- **`hipaa + iso-27001 + iso-27001-privacy`** — ISMS + PIMS + HIPAA legal-framework triad
- **`hipaa + iso-37301 + iso-37301-healthcare`** — compliance management substrate + healthcare sectoral profile + HIPAA-specific requirements

## When to use

- Health plans / health insurance issuers (commercial + Medicare Advantage + Medicaid managed care)
- Healthcare clearinghouses (claims + repricing + COB intermediaries)
- Healthcare providers transmitting HIPAA Transaction Rule data electronically (hospitals + physician practices + dental + behavioral health + long-term care)
- Business Associates: SaaS serving CEs; cloud hosting; analytics; revenue-cycle services; PHR vendors; e-prescribing; HIE infrastructure
- BA subcontractors (per HITECH §13404 extension)

## When NOT to use

- US healthcare adopters who only handle de-identified data per §164.514 Safe Harbor (not PHI; HIPAA doesn't apply to de-identified information)
- Non-US healthcare adopters not serving US patients (use jurisdictional analog — UK NHS Data Security and Protection Toolkit; EU EHDS regulation forthcoming)
- Pure consumer health tech outside HIPAA scope (use FTC Health Breach Notification Rule per 16 CFR Part 318 instead — covered by `privacy` overlay)
- Workforce-only PHI exposure (e.g., FSA / HSA admin) — HIPAA scope is narrow here; specific group health plan provisions in §164.504(f)

## Forward work

- HIPAA Privacy Rule final updates (2024 NPRM modifications + Reproductive Health Care Privacy Rule April 2024)
- HHS OCR Compliance Investigation response template
- Authorization template per §164.508 (form with required content)
- Accounting of Disclosures log template per §164.528
- Restriction Request log per §164.522(a)
- Reproductive Health Care Privacy Rule 2024 amendments (effective Dec 2024) attestation template
- ONC certified EHR technology adoption tracker
- 42 CFR Part 2 (substance use disorder) overlay — narrower scope than HIPAA + additional consent requirements
- Part 2 / HIPAA reconciliation post-CARES Act §3221 alignment (effective Feb 2024)
- Connected medical-devices cross-overlay (medical-devices + hipaa + privacy + iso-27001)
- 42 USC §1320d-6 criminal-penalties response template
