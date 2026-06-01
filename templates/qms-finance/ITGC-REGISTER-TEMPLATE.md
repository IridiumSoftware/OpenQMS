---
document_id: FIN-ITGC-001
title: "IT General Controls (ITGC) Register"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[IT SOX Lead, Title]"
status: draft
approved_by: "[CIO / CFO, Title]"
approval_date: YYYY-MM-DD
---

# FIN-ITGC-001: IT General Controls Register

ITGCs support the continued effective operation of automated controls and the reliability of information produced by the entity (IPE) relied on for ICFR (PCAOB AS 2201). Scoped to financially-relevant systems (the ERP, sub-ledgers, consolidation, and reporting tools behind the [Control Matrix](ICFR-CONTROL-MATRIX-TEMPLATE.md)). Compose with the **iso-27001** overlay for the broader infosec control set.

## In-scope systems

[List the financially-relevant applications + supporting databases / OS / network in scope, with the significant accounts each touches.]

## ITGC domains

| Domain | Control objective | Control ID | Description | Frequency | Owner | Test ref |
|---|---|---|---|---|---|---|
| Logical access & security | Access is appropriate, authorized, and periodically reviewed; SoD enforced | ITGC-AC-01 | [provisioning approval + quarterly access review + privileged-access logging] | quarterly | [IT Sec] | [FIN-TEST ref] |
| Change management | Changes are authorized, tested, and approved before production | ITGC-CM-01 | [change ticket → test → approval → segregated migration] | per change | [App Owner] | [FIN-TEST ref] |
| Computer operations | Jobs, backups, and incidents are monitored and resolved | ITGC-OP-01 | [batch-job monitoring + backup verification + incident SLA] | daily | [IT Ops] | [FIN-TEST ref] |
| Program development (SDLC) | New systems/major changes are validated before go-live | ITGC-PD-01 | [SDLC gate + UAT sign-off + data-migration validation] | per project | [PMO] | [FIN-TEST ref] |
