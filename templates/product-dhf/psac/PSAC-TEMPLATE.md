---
document_id: PSAC-XXX
title: "[Product Name] — Plan for Software Aspects of Certification"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Software Lead / Cert Engineer, Title]"
status: draft
approved_by: "[Cert Engineering / QA Lead + Certification Authority Designated Engineering Representative, Title]"
approval_date: YYYY-MM-DD
---

# PSAC-XXX: [Product Name] Plan for Software Aspects of Certification

Per DO-178C:2011 §4 + §11.1. The PSAC is the **primary planning document** submitted to and agreed with the certification authority (FAA / EASA / TCCA / etc.) at SOI (Stage of Involvement) #1. It establishes the software development lifecycle, processes, tools, standards, and Design Assurance Level (DAL) that will be followed and against which the certification credit will be claimed.

The PSAC is supplemented by four other top-level plans referenced from it (SDP / SVP / SCMP / SQAP) and the three top-level standards documents (SRS / SDS / SCS).

## 1. System overview

- **Product name + variant(s):** [name]
- **Software item(s) covered by this PSAC:** [enumerate]
- **System context:** [parent system; aircraft type; integration]
- **Linked system-level docs:** [ARP4754A SSP; FHA-XXX; SSP-XXX]
- **Certification basis:** [14 CFR Part 25.1309 / CS-25.1309 / etc. as applicable]
- **Certification authority:** [FAA / EASA / TCCA / etc.]
- **DER / DOA / Compliance Verification Engineer:** [name + reference]

## 2. Software overview

- **Software item identification:** [name + version + part number]
- **Hardware platform:** [target processor + OS / RTOS / bare metal]
- **Programming language(s) + compilers + tool versions:** [as configuration items]
- **Development methodology:** [waterfall / iterative / model-based / etc.]
- **Reused software:** [previously-certified, COTS, open source — DAL of reused components; reusable software components qualification]
- **Tool list:** [development + verification tools; qualified per DO-330 where applicable]

## 3. Certification considerations

### 3.1 Software level (DAL)

- **Assigned DAL:** [A / B / C / D / E]
- **DAL rationale:** [reference to FHA classification per ARP4761; failure condition classification]
- **Multi-version dissimilar software (MVDS) considerations** (if applicable): [as per AC 20-115 / AMC 20-115]

### 3.2 Means of compliance

[Per DO-178C Annex A Tables A-1 through A-10. For the assigned DAL, enumerate which objectives apply and the means of compliance for each. Independence requirements per the DAL table.]

### 3.3 Issue Papers / CRIs (if applicable)

[Non-standard interpretations or compliance issues raised with the certification authority. Each issue paper / Certification Review Item tracked through resolution.]

## 4. Software life cycle

### 4.1 Software development life cycle processes

[Per DO-178C §5. Reference the SDP for full detail; PSAC summarizes:]

- Software Planning Process
- Software Requirements Process
- Software Design Process
- Software Coding Process
- Integration Process
- Verification Process (reference SVP)
- Configuration Management Process (reference SCMP)
- Quality Assurance Process (reference SQAP)
- Certification Liaison Process

### 4.2 Transition criteria between processes

[Per DO-178C §4.3. Entry + exit criteria for each lifecycle process.]

## 5. Software life cycle data

### 5.1 Data produced

[Per DO-178C Section 11. Enumerate which lifecycle data items will be produced (PSAC, SDP, SVP, SCMP, SQAP, SAS; SRD, SDD, source code, executable object code; SVCP, SCI, problem reports; configuration index, etc.). For each, note Control Category 1 vs 2 per DO-178C §7.3.]

### 5.2 Data submitted to certification authority

[Subset of §5.1 explicitly submitted for review.]

### 5.3 Data available for review (not submitted)

[Subset of §5.1 retained by applicant; available on request.]

## 6. Software standards

- **Software Requirements Standard (SRS):** [reference]
- **Software Design Standard (SDS):** [reference]
- **Software Coding Standard (SCS):** [reference]
- **Linked artifacts:** [SRS / SDS / SCS controlled documents]

## 7. Tool qualification

| Tool | Purpose | DO-330 TQL | Qualification approach | Reference |
|---|---|---|---|---|
| | | TQL-1 / TQL-2 / TQL-3 / TQL-4 / TQL-5 | | |

[Per DO-330. Tools that automate verification activities or generate code/data that ends up in the airborne system require qualification.]

## 8. Configuration management

[Per DO-178C §7. Reference SCMP. Brief summary of:]

- Configuration identification
- Baselining
- Problem reporting
- Change control
- Configuration status accounting
- Release records
- Data control categories (CC1 / CC2)

## 9. Software quality assurance

[Per DO-178C §8. Reference SQAP. Brief summary of:]

- Software QA activities + records
- Audit + assessment cadence
- Software conformity review
- Records of audit results + corrective actions

## 10. Certification liaison process — Stages of Involvement (SOI)

| SOI | Topic | Planned date | Deliverables |
|---|---|---|---|
| SOI #1 | Planning Review | YYYY-MM-DD | PSAC + SDP + SVP + SCMP + SQAP + SRS + SDS + SCS |
| SOI #2 | Development Review | YYYY-MM-DD | Software requirements + design; verification approach for requirements + design |
| SOI #3 | Verification Review | YYYY-MM-DD | Verification results; test coverage; structural coverage |
| SOI #4 | Final Certification | YYYY-MM-DD | Software Accomplishment Summary (SAS) + Software Configuration Index (SCI) |

## 11. Additional considerations

- **Previously-developed software (PDS):** [if applicable]
- **Service experience credit:** [if applicable]
- **Parameter Data Items (PDI):** [if applicable]
- **Field-loadable software (FLS):** [if applicable]
- **Multi-version dissimilar software (MVDS):** [if applicable]
- **Use of formal methods supplement (DO-333):** [if applicable]
- **Use of model-based development supplement (DO-331):** [if applicable]
- **Use of object-oriented technology supplement (DO-332):** [if applicable]

## 12. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Software Lead | | | |
| Certification Engineering | | | |
| QA Lead | | | |
| DER / Compliance Verification Engineer | | | |
| Certification Authority concurrence (received) | | | |

## 13. References

- DO-178C:2011 / ED-12C — Software Considerations in Airborne Systems and Equipment Certification.
- DO-330 — Software Tool Qualification Considerations.
- DO-331 — Model-Based Development and Verification Supplement to DO-178C and DO-278A.
- DO-332 — Object-Oriented Technology and Related Techniques Supplement to DO-178C and DO-278A.
- DO-333 — Formal Methods Supplement to DO-178C and DO-278A.
- ARP4754A — Guidelines for Development of Civil Aircraft and Systems.
- FAA AC 20-115() — RTCA Inc Document DO-178() (current revision).
- EASA AMC 20-115() (current revision).
- Linked artifacts: SDP, SVP, SCMP, SQAP, SRS, SDS, SCS; FHA-XXX, SSP-XXX, TFC-XXX (type-cert pack index).

## 14. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
