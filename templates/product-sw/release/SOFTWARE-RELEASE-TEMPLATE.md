---
document_id: SRR-XXX-001
title: "[Software Item Name] — Software Release Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Release Manager, Title]"
status: draft
approved_by: "[Software / QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# SRR-XXX-001: [Software Item Name] Software Release Record

Per IEC 62304 §5.8 (Software release).

## 1. Release identification

- **Software item:** [name]
- **Release version:** [e.g. 2.4.0]
- **Git tag / commit hash:** [refs/tags/v2.4.0 — capture full SHA]
- **Release date:** YYYY-MM-DD
- **Release scope:** [new release / patch / hotfix; bullet list of intended changes]

## 2. Release approval checklist

Per IEC 62304 §5.8.1–§5.8.8. The release-gate CI workflow (`.github/workflows/release-gate.yml`) automates several of these; manual confirmation here is the human attestation.

- [ ] **§5.8.1** All software-development activities (per the plan) are complete OR documented disposition exists for any incomplete activities.
- [ ] **§5.8.2** All known residual anomalies are documented in §4 below and each has an impact evaluation.
- [ ] **§5.8.3** Each documented residual anomaly has been evaluated against the safety class and the risk management file (RMF-XXX-001).
- [ ] **§5.8.4** Version identification is fully recorded (this document + Git tag).
- [ ] **§5.8.5** Released software CAN be reproduced from the configuration items recorded (Git tag + SOUP-XXX-001 + build environment specification).
- [ ] **§5.8.6** Software has been archived along with documentation per the retention SOP.
- [ ] **§5.8.7** Release process is documented and was followed (this document is the evidence).
- [ ] **§5.8.8** Activities or tasks not completed are explicitly listed in §5 below.

## 3. Risk assessment summary

[Confirm that the RMF (RMF-XXX-001) has been reviewed in light of this release's changes; that risk control measures are intact; that overall residual risk acceptability per ISO 14971 §8 still holds.]

- **RMF version reviewed:** [RMF-XXX-001 v1.X]
- **New hazards identified in this release?** [Yes/No — if yes, RMF must be updated before release.]
- **Residual risk evaluation unchanged?** [Yes/No]

## 4. Known anomalies / open issues

| Anomaly ID | Description | Severity | Workaround | Impact on risk | Disposition |
|---|---|---|---|---|---|
| ANOM-001 | [Brief description] | [Low/Med/High] | [if any] | [reference RMF if relevant] | [Defer to next release / accept] |

## 5. Incomplete activities (if any)

[Per IEC 62304 §5.8.8 — list any planned activities that were not completed for this release, with justification and the plan for completion in a subsequent release.]

## 6. Release artifacts archived

[List of artifacts captured as part of this release — Git tag, built binaries, build logs, SOUP register snapshot, configuration files, test reports.]

| Artifact | Location | Hash |
|---|---|---|

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Software Lead | | | |
| Quality Lead | | | |
| Risk Manager | | | |
| Release Authority | | | |

## 8. References

- IEC 62304:2006+A1:2015 §5.8 — Software release.
- ISO 14971:2019 §8, §9, §10.
- Linked artifacts: SRS-XXX-001; SAD-XXX-001; STP-XXX-001; SOUP-XXX-001; RMF-XXX-001; VP-XXX-001; VAL-XXX-001.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
