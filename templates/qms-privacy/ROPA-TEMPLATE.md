# Records of Processing Activities (ROPA)

**Template for:** GDPR Article 30 Records of Processing Activities — required record per controller + per processor (when acting as processor). One row per processing activity.
**Article 30(5) exemption:** Limited — only applies to organisations <250 employees AND processing is occasional AND not high-risk AND not Article 9 special category / Article 10 criminal-conviction data. Most orgs in scope.
**Maintained centrally:** Updated on every new processing purpose / new lawful basis / new recipient / new transfer / new retention period / new technical+organisational measure. Reviewed annually as part of GDPR compliance review.

---

## Part A — Controller ROPA (Article 30(1))

One entry per processing activity. Required fields per Article 30(1)(a)-(g).

### Entry [N] — [processing activity name]

| Field | Value |
|---|---|
| **Activity ID** | [internal stable ID] |
| **Activity name** | |
| **Status** | ☐ Active ☐ Suspended ☐ Retired (since: ) |
| **Owner (business)** | |
| **Owner (technical)** | |
| **Date created** | |
| **Last updated** | |
| **Next review** | |

#### (1)(a) Controller + DPO contacts

| Role | Identity + contact |
|---|---|
| Controller (legal entity) | |
| Joint controllers (if any; Article 26 arrangement reference) | |
| Controller's EU representative (if non-EU; Article 27) | |
| DPO (if designated; Article 37) | |

#### (1)(b) Purposes of processing

| Purpose | Lawful basis (Article 6) | If 6(1)(f) legitimate interests reference | If Article 9 SPI — condition |
|---|---|---|---|
| | | | |

#### (1)(c) Categories of data subjects + personal data

| Category of data subject | Categories of personal data | Special category (Art 9)? |
|---|---|---|
| | | ☐ |

#### (1)(d) Categories of recipients

| Category | Examples | Personal data shared | Business purpose |
|---|---|---|---|
| Internal departments | | | |
| Affiliates | | | |
| Service providers (processors) | | | |
| Joint controllers | | | |
| Third parties (sale/share recipients per CCPA) | | | |
| Government / regulators / law enforcement | | | |

#### (1)(e) Third-country transfers + safeguards

| Destination | Recipient | Data categories | Safeguard | Adequacy? |
|---|---|---|---|---|
| | | | ☐ SCCs ☐ BCRs ☐ Adequacy ☐ Art 49 derogation | |

If applicable: documentation of suitable safeguards per Article 46(2)(d)/(f) (e.g., link to BCRs approval; SCC contract reference; certification reference; UK IDTA reference); Transfer Impact Assessment per Schrems II.

#### (1)(f) Retention schedule

| Data category | Retention period | Trigger for deletion | Disposal method |
|---|---|---|---|
| | | | |

Reference: [link to org records-retention SOP].

#### (1)(g) Article 32 technical + organisational security measures

| Measure category | Implementation |
|---|---|
| Encryption at rest | |
| Encryption in transit | |
| Pseudonymisation | |
| Access controls (RBAC / ABAC / least privilege) | |
| Authentication (MFA / SSO) | |
| Logging + monitoring | |
| Backup + restoration | |
| Vulnerability management | |
| Incident response | |
| Vendor security assessment | |
| Personnel training | |
| Physical security | |
| Reference: ISO 27001 SoA + control mapping | |

#### Supplementary metadata (not required by Article 30 but recommended for audit-readiness)

| Field | Value |
|---|---|
| DPIA required? | ☐ N/A ☐ Yes — DPIA ref: ; date: |
| Data subject notice (Article 13/14) provided? | ☐ Yes — privacy policy section ref: |
| Cross-references to CCPA notice at collection sections | |
| Linked DPAs (Article 28) | |
| Linked sub-processor list | |
| Linked information-security risk assessment | |
| Linked records-retention SOP entry | |
| ADMT involved? (CCPA + GDPR Art 22 cross-reference) | |

---

## Part B — Processor ROPA (Article 30(2))

One entry per processing activity carried out on behalf of a controller. Required fields per Article 30(2)(a)-(d).

### Entry [N] — [activity name on behalf of [controller]]

| Field | Value |
|---|---|
| **Activity ID** | |
| **Activity name** | |
| **Status** | ☐ Active ☐ Suspended ☐ Retired |

#### (2)(a) Processor + controller contacts

| Role | Identity + contact |
|---|---|
| Processor (legal entity — this org) | |
| Processor's EU representative (if non-EU; Article 27) | |
| Processor's DPO (if designated) | |
| Controller(s) on whose behalf processing carried out | |
| Controller's EU representative + DPO contacts | |

#### (2)(b) Categories of processing carried out on behalf of each controller

| Controller | Categories of processing | Categories of data subjects | Categories of personal data | Special category? |
|---|---|---|---|---|
| | | | | ☐ |

#### (2)(c) Third-country transfers + safeguards

Same structure as Part A (1)(e).

#### (2)(d) General description of Article 32 technical + organisational security measures

Same structure as Part A (1)(g).

#### Supplementary metadata

| Field | Value |
|---|---|
| Linked DPA (Article 28) | |
| Sub-processors used (with controller authorisation per §6.4 DPA) | |
| Linked breach notification SLA to controller (24h target) | |

---

## Maintenance discipline

| Event | ROPA action |
|---|---|
| New processing purpose introduced | Add entry; capture lawful basis + Article 9 condition if SPI; cross-check privacy policy update + DPIA threshold |
| Existing purpose modified | Edit entry; capture last-updated; cross-check privacy policy update |
| Processing activity retired | Mark Retired with date; preserve historical row; cross-check deletion of underlying data per retention schedule |
| New recipient added | Edit entry; cross-check DPA (Article 28) in place; cross-check transfer safeguard if international |
| Retention period change | Edit entry; cross-check disposal procedure + records-retention SOP |
| Article 32 measure change | Edit entry; cross-check ISO 27001 SoA + risk assessment |
| Annual review | Walk every entry; refresh owner + dates; verify accuracy with business owner |
| Supervisory authority request (Article 30(4)) | Provide complete ROPA on request — typically within 14 days |

## Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| ROPA custodian | | | |
| DPO (review) | | | |
| Legal (annual review) | | | |

---

**Trace evidence.** This ROPA addresses GDPR-Art-30-ROPA + GDPR-Art-5-principles + GDPR-Art-32-security per `modules/privacy/module.yaml`. Article 30(5) exemption rarely applies in practice — assume in scope unless small + occasional + non-high-risk + non-special-category processing is confirmed. EDPB Guidelines 07/2019 on processor records (Article 30(2)) clarify processor-side scope.
