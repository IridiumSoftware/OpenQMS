# Business Associate Agreement (BAA)

**Template for:** HIPAA §164.504(e) + §164.314(a) Business Associate Agreement.
**Scope:** Required between Covered Entity (or upstream Business Associate) and any Business Associate per §160.103 definition. Subcontractor BAAs required for any subcontractor of a BA that creates / receives / maintains / transmits PHI on behalf of the BA.
**Form:** Standalone OR as schedule/addendum to underlying services agreement.

---

## 1. Parties

| Field | Covered Entity / Upstream BA | Business Associate |
|---|---|---|
| Legal entity name | | |
| Registered address | | |
| Privacy Officer / Security Officer + contact | | |
| Authorized signatory + title | | |

## 2. Definitions

Terms used herein have the same meaning as in HIPAA Rules (45 CFR Parts 160 + 164), including:
- **PHI** — Protected Health Information per §160.103
- **ePHI** — electronic PHI subject to Security Rule
- **Breach** — per §164.402, with the 4-factor presumption-rebuttal analysis
- **Designated Record Set** — per §164.501
- **Required By Law** — per §164.103
- **Secretary** — Secretary of HHS or designee

## 3. Permitted + required uses + disclosures by BA

### 3.1 Permitted uses

BA may use + disclose PHI:
- (a) To perform the Services specified in the underlying agreement attached as Annex A;
- (b) For the proper management + administration of BA OR to carry out BA's legal responsibilities per §164.504(e)(4) — limited to:
  - As required by law, OR
  - Reasonable assurances from any recipient that PHI will remain confidential + used/disclosed only as required by law or for purpose for which disclosed AND recipient will notify BA of any known breach
- (c) To provide data aggregation services relating to healthcare operations of CE per §164.504(e)(2)(i)(B)
- (d) To de-identify PHI per §164.514 (Safe Harbor 18-identifier removal OR Expert Determination)

### 3.2 Prohibited uses

BA shall NOT:
- Use or disclose PHI other than as permitted by this BAA or required by law
- Sell PHI per HITECH §13405(d) (limited exceptions)
- Use PHI for marketing communications (limited TPO exceptions)
- Use psychotherapy notes without specific Authorization
- Use PHI for fundraising on behalf of CE without specific authorization

## 4. BA obligations

### 4.1 Safeguards (§164.314(a)(2)(i)(A))

BA shall implement appropriate administrative + physical + technical safeguards to prevent use/disclosure of PHI other than as permitted by this BAA. BA shall comply with applicable Security Rule provisions (§164.302-318) with respect to ePHI.

### 4.2 Reporting (§164.314(a)(2)(i)(B) + §164.410)

BA shall report to CE:
- Use/disclosure not permitted by this BAA — within [N] days of discovery
- Security incident — within [N] days of discovery (definitional debate; recommend including unsuccessful security incidents in aggregate periodic report, successful incidents individually)
- **Breach** of unsecured PHI — without unreasonable delay AND no later than **60 calendar days** from discovery per §164.410(b); include all §164.410(c) required content + sufficient detail for CE to perform §164.404 individual notification within 60 days from CE's discovery (clock starts at BA's discovery for purposes of BA notification to CE, but at CE's discovery for purposes of CE's notification to individuals)

### 4.3 Sub-contractor management (§164.314(a)(2)(iii) + §164.504(e)(1)(ii))

BA shall ensure that any subcontractor that creates / receives / maintains / transmits PHI on behalf of BA agrees in writing to the same restrictions + conditions that apply to BA with respect to such information. Sub-BAAs flow down all material terms of this BAA.

### 4.4 Individual access (§164.524 via §164.504(e)(2)(ii)(E))

If BA maintains PHI in a Designated Record Set on behalf of CE, BA shall make such PHI available to CE within [N] days of CE's request to enable CE to meet §164.524 access obligations.

### 4.5 Amendment (§164.526 via §164.504(e)(2)(ii)(F))

If BA maintains PHI in a Designated Record Set on behalf of CE, BA shall make amendments to PHI as directed by CE within [N] days of CE's request to enable CE to meet §164.526 amendment obligations.

### 4.6 Accounting of Disclosures (§164.528 via §164.504(e)(2)(ii)(G))

BA shall document accountable disclosures + provide information to CE on request within [N] days to enable CE to meet §164.528 accounting obligations.

### 4.7 Internal practices, books + records (§164.504(e)(2)(ii)(H))

BA shall make internal practices, books + records relating to use/disclosure of PHI available to the Secretary for purposes of determining CE's HIPAA compliance.

### 4.8 Mitigation (§164.530(f) flow-down recommended)

BA shall mitigate, to the extent practicable, any harmful effect known to BA of a use/disclosure of PHI by BA in violation of this BAA.

### 4.9 Minimum necessary (§164.502(b))

BA shall request, use, and disclose only the minimum amount of PHI necessary to accomplish the intended purpose.

## 5. CE obligations

### 5.1 Notice of restrictions

CE shall notify BA of any limitation in CE's NPP (per §164.520) to the extent it may affect BA's use/disclosure of PHI.

### 5.2 Notice of changes in individual permissions

CE shall notify BA of any changes in, or revocation of, Authorization by an individual to the extent it may affect BA's use/disclosure.

### 5.3 Permissible requests

CE shall not request BA to use or disclose PHI in any manner not permitted by HIPAA if done by CE itself (except for §3.1(b)-(c) data-aggregation + management-and-administration exceptions).

## 6. Term + termination (§164.504(e)(2)(ii)(I))

### 6.1 Term

Effective on signature; continues until termination of underlying agreement OR termination per §6.2.

### 6.2 Termination for material breach

CE may terminate this BAA + underlying agreement upon BA's material breach if:
- BA does not cure the breach within [N] days of notice, OR
- Cure is not feasible

### 6.3 Effect of termination — return / destroy PHI (§164.504(e)(2)(ii)(J))

At termination, BA shall:
- Return OR destroy all PHI received from CE or created/received by BA on behalf of CE, including subcontractor copies, OR
- If return/destruction is INFEASIBLE, extend protections of this BAA to PHI and limit further uses/disclosures to those that make return/destruction infeasible

Certification of destruction or written infeasibility determination provided within [N] days of termination.

## 7. HIPAA-relevant operational provisions

| Topic | Specification |
|---|---|
| BA contact for individual access/amendment/accounting requests routed via CE | [name + email + phone] |
| BA contact for breach notification | [24-hour contact] |
| Security incident aggregate reporting cadence | [quarterly recommended] |
| BA Risk Analysis evidence available to CE | ☐ Yes — SOC 2 Type II / HITRUST r2 / ISO 27001 attestation acceptable in lieu of direct audit |
| Encryption at rest + in transit (per HHS Guidance for "secured" PHI status) | ☐ AES-256 at rest ☐ TLS 1.2+ in transit |
| Audit log retention | [≥6 years per §164.316(b)(2)(i)] |
| PHI in non-US locations? | ☐ No ☐ Yes — list jurisdictions + safeguards |

## 8. Sub-BA acknowledgment + flow-down

| Sub-BA legal name | Services | Sub-BAA executed (date) | Sub-BA Security attestation reference |
|---|---|---|---|
| | | | |

## 9. Liability

Each party retains liability for its own HIPAA violations. BA acknowledges HITECH §13404 extends Security Rule + certain Privacy Rule provisions directly to BAs, exposing BA to direct OCR enforcement + Civil Monetary Penalties per §160.404 + criminal penalties per 42 USC §1320d-6.

[Liability cap + indemnification per underlying agreement, with HIPAA-specific carve-outs per organizational policy. Common: cap exclusion for HIPAA fines + breach-notification costs + statutory damages.]

## 10. Governing law + dispute resolution

Per underlying agreement; HIPAA federal law preempts state law to the extent of any conflict (§160.203).

## 11. Severability + integration

If any provision deemed invalid, remainder remains in effect. This BAA + Annex A constitute the entire agreement between parties with respect to BA HIPAA obligations.

## 12. Annexes

| Annex | Content |
|---|---|
| A | Services description + scope of PHI processed |
| B | Sub-BA list authorised at signature |
| C | Technical + Organisational Safeguards summary (or reference to SOC 2 / HITRUST / ISO 27001 attestation) |

## 13. Signatures

| Party | Name + title | Signature | Date |
|---|---|---|---|
| Covered Entity / Upstream BA | | | |
| Business Associate | | | |

---

**Trace evidence.** This BAA addresses HIPAA-164-314-organizational-requirements-BAA + HIPAA-160-103-CE-BA-scope + HIPAA-164-400-414-breach-notification per `modules/hipaa/module.yaml`. HHS Model BAA available at hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/.
