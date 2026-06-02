# Companion — P15 trace-link frontmatter schema (DRAFT)

**Status:** DRAFT design proposal · pre-implementation · not yet a spec entry
**Date:** 2026-05-31
**Addresses:** P15 (integration-architecture cross-record trace network) — and the shared dependency P2's new templates should adopt as they are authored.
**Maintainer:** Aaron Green

This document proposes the instance-level trace-link convention. It is the **shared dependency** flagged in the priority-stack discussion: lock the grammar now, apply it to P2's validation-package templates as they are written, and P15 never has to retrofit them. Nothing here is built yet; this is the schema we agree on before code.

---

## 1. What it has to do

Deliver the reviewer's vision — an enforced *instance-level* trace graph across living records:

> requirement ↔ hazard ↔ mitigation ↔ test ↔ CAPA ↔ complaint ↔ post-market-surveillance finding

This is one layer **below** the existing clause-level trace. To be precise about the two layers:

| Layer | Nodes | Edges | Enforced by | Status |
|---|---|---|---|---|
| **Clause-level** (shipped) | standard clauses ↔ templates | `addresses:` bindings | `openqms trace` + OQ-001 + OQ-067 zero-orphan in CI | `:tested` / `:verified` |
| **Instance-level** (P15) | individual records (this hazard, that test) | `trace_links` | `openqms trace-instances` (new) + instance zero-orphan | not built |

The clause layer proves *"every in-scope clause has ≥1 template."* The instance layer proves *"every hazard has ≥1 mitigation, every test cites ≥1 requirement, every CAPA cites ≥1 trigger, and every referenced ID resolves."* It does **not** prove a mitigation actually mitigates — that is QA judgment (the OQ-080 firewall holds).

---

## 2. The one decision that drives everything: granularity tier

Records come at two granularities, and the schema must be explicit about which it traces:

- **Whole-record documents** — one record per file/issue. A CAPA, a complaint, an NCR, a single validation protocol run. Natural ID home: **frontmatter** (or issue number+label).
- **Item-collection documents** — one file holds *many* trace items. A Risk Management File (`RMF-XXX-001`) contains many hazards; an SRS (`SRS-XXX-001`) contains many requirements. The reviewer's graph operates on the **items inside** (HAZ-0007, REQ-0012), not the containing file.

Tracing only at document granularity (RMF ↔ SRS) is too coarse to deliver P15. So the proposal is a **two-tier scheme**:

- **Tier 1 — document frontmatter** carries the record's identity and document-level links (used directly for whole-record docs).
- **Tier 2 — in-body item tables** carry per-item IDs and links inside item-collection docs, parsed by the walker.

Both tiers share one ID grammar and one relationship vocabulary (below), so the walker treats every node uniformly regardless of where its ID was declared.

> **RESOLVED (2026-05-31):** two-tier. Ship **Tier 1 first** (P15.1a); add Tier-2 in-body table parsing as P15.1b.

---

## 3. ID grammar

Build on the convention already in the wild (`RMF-XXX-001`, `SRS-XXX-001`): `KIND-SCOPE-NNNN`.

```
<KIND>-<SCOPE>-<NNNN>
```

- `KIND` — 2–5 uppercase letters from the controlled record-kind vocabulary (§4).
- `SCOPE` — product / system / project token, uppercase alnum (`CARDIO`, `PUMP2`). **RESOLVED (2026-05-31, refined): SCOPE mandatory for product-bound kinds** (`REQ` `URS` `HAZ` `MIT` `TST` `VMP` `IQ` `OQ` `PQ` — design + V&V items inherently tied to one product) and **optional for process-level kinds** (`CAPA` `CMPL` `NCR` `CHG` `AUD` `SUP` — which may span products or be process-only). A single-product adopter fork may force scope-less everywhere via `require_scope: false` in `trace-policy.yaml`; the multi-product default requires it for the product-bound set.
- `NNNN` — zero-padded sequence, unique within `KIND-SCOPE` (or within `KIND` when scope-less).

Regex (grammar accepts both forms; `require_scope` enforces which per kind): `^[A-Z]{2,5}-([A-Z0-9]+-)?\d{3,}$`

> **Provenance note (real-world grounding).** SCOPE in the ID is a *denormalization* of the authoritative product↔record mapping. In production QMS practice (per Aaron's deployment) document numbers are deliberately **product-agnostic**, typed by document *class* — `QAP` (protocols), `DWI` (detailed work instructions), `DWF` (work forms), `PLN` (quality plans), `QTP` (test protocols), `QTR` (test reports), `WI` (manufacturing work instructions; travelers are WI appendices). Product association lives in the **DHF register**, referenced from the **Device Master Record** (the top-level product doc pointing to BOMs, Mfg/Packaging WIs, QTRs; BOM itself out of scope). P15 keeps SCOPE in *item* IDs for walkability, but the DHF index (`TECHNICAL-FILE-INDEX-TEMPLATE`) stays the product authority — a forward invariant (P15.2+) can assert a node's SCOPE matches its source document's DHF-register product assignment.

Issue-sourced records (P15.2) use `KIND-<issue-number>` (e.g., `CAPA-123`), derived from label + GitHub issue number — no SCOPE, because the issue number is globally unique in the repo.

---

## 4. Record-kind vocabulary (controlled)

| KIND | Record | Today's surface |
|---|---|---|
| `REQ` | Requirement / design input | `SRS-*`, `design-input.yml` |
| `URS` | User requirement (computerized system) | P2 — new |
| `HAZ` | Hazard / risk item | RMF item table |
| `MIT` | Risk control / mitigation | RMF item table |
| `TST` | Verification or validation test | `VERIFICATION-PROTOCOL`, `VALIDATION-PROTOCOL`, software test protocol |
| `VMP` | Validation Master Plan (governs IQ/OQ/PQ; `implemented_by` them) | v0.71.0 — new |
| `IQ` `OQ` `PQ` | Installation / Operational / Performance qualification | P2 — new |
| `SYS` | Computerized system (validation inventory entry) | P2 — new |
| `FUNC` | Feature / function / operation (CSA risk-determination unit) | P2 — new |
| `VREC` | Assurance record (CSA evidence) | P2 — new |
| `CAPA` | Corrective/preventive action | `capa.yml` |
| `CMPL` | Complaint | `complaint.yml` |
| `NCR` | Nonconformance | `nonconformance.yml` |
| `CHG` | Change request / control | `change-request.yml`, `CHANGE-CONTROL` |
| `PMS` | Post-market-surveillance finding | (forward) |
| `AUD` | Audit finding | (forward) |
| `SUP` | Supplier evaluation | `supplier-evaluation.yml` |

The vocabulary is **extensible**: a fork adds a KIND by registering it (mirrors the standards registry pattern). Unknown KIND → linter error, not silent acceptance.

---

## 5. Relationship vocabulary (directed, with inverse)

Edges are **directed and typed**. Store each edge **once** on either endpoint; the walker materializes the inverse — no double-maintenance.

| Forward | Inverse | Canonical pair |
|---|---|---|
| `derived_from` | `derives` | REQ derived_from URS; design-output derived_from REQ |
| `mitigated_by` | `mitigates` | HAZ mitigated_by MIT |
| `verified_by` | `verifies` | REQ / MIT verified_by TST |
| `validated_by` | `validates` | URS validated_by PQ |
| `triggered_by` | `triggers` | CAPA triggered_by CMPL / NCR / PMS / AUD |
| `implements` | `implemented_by` | IQ / OQ / PQ implements VMP |
| `part_of` | `comprises` | FUNC part_of SYS (structural containment; added 2026-05-31 per P2) |
| `assured_by` | `assures` | FUNC assured_by VREC (CSA assurance evidence; added 2026-05-31 per P2) |
| `relates_to` | `relates_to` | generic, symmetric — escape hatch |

> **RESOLVED (2026-05-31):** keep typed edges — they are what make the zero-orphan invariants meaningful. (Rejected alternative: a single untyped `linked: [ids]`, which cannot express "every HAZ needs a *mitigation* specifically".)

---

## 6. Tier 1 — document frontmatter

Additive to the existing template frontmatter (`template_schema.py` is permissive on extras, so this is non-breaking). Three new fields — `record_kind`, `record_id`, `trace_links`:

```yaml
---
document_id: DWF-0117              # UNCHANGED — document-control ID (Detailed Work Form),
                                  #   per the company numbering SOP; product-agnostic
record_kind: CAPA                 # NEW — trace taxonomy (§4)
record_id:   CAPA-CARDIO-0034     # NEW — trace-graph node ID (kind-typed, product-scoped)
version: "1.0"
owner: "[Quality Manager]"
status: open
opened_date: YYYY-MM-DD
trace_links:                      # NEW — map of relationship -> [target record IDs]
  triggered_by: [NCR-CARDIO-0009]
  relates_to:   [CMPL-CARDIO-0003]
---
```

- `document_id` — **unchanged**; the company's document-control identifier, typed by document *class* (QAP/DWI/DWF/PLN/QTP/QTR/WI) and governed by the existing numbering SOP. The trace layer never touches it.
- **RESOLVED #4 (2026-05-31): `record_id` is always a separate field — never folded into `document_id`.** The two are orthogonal taxonomies: a `QTP` *document* contains many `TST` *items*; one document ≠ one trace node. The walker records `source_document = document_id` automatically (for Tier-2 items, the containing file's `document_id`), so provenance is captured with no hand-entered field.
- `record_kind` is **required** on trace-participating templates (controlled vocabulary §4).
- `trace_links` keys must be in the relationship vocabulary (§5); values are lists of well-formed record IDs.

## 7. Tier 2 — in-body item tables (item-collection docs)

Inside an RMF, SRS, etc., items live in a **trace table** with a fixed leading `ID` column and trailing `Trace links` column. Example (RMF hazard table):

```markdown
| ID | Hazard | Severity | Trace links |
|---|---|---|---|
| HAZ-CARDIO-0007 | Over-infusion | Critical | mitigated_by:MIT-CARDIO-0011,MIT-CARDIO-0012; verified_by:TST-CARDIO-0021 |
```

Compact cell grammar: `rel:ID,ID; rel:ID` — same vocabularies as Tier 1, just serialized into one cell. The walker recognizes a trace table by the presence of an `ID` column whose values match the ID grammar.

## 8. Issue-record mapping (P15.2)

Issue forms get a structured field instead of free text. The `nonconformance.yml` "create linked CAPA issue" checkbox becomes an input:

```yaml
  - type: input
    id: trace-links
    attributes:
      label: Trace links
      description: "rel:ID syntax, e.g. triggered_by:NCR-CARDIO-0009"
      placeholder: "triggered_by:NCR-CARDIO-0009; relates_to:CMPL-CARDIO-0003"
```

A `gh`-backed export (the verify-deployment pattern) snapshots open issues → the same node/edge JSON the markdown walker emits, so both substrates feed one graph. Deferred to P15.2.

---

## 9. Invariants + `trace-policy.yaml`

Invariants are **configurable** (mirrors `deployment-policy.yaml` from verify-deployment / P11), because not every adopter wants every rule and severity varies:

```yaml
# trace-policy.yaml
referential_integrity: error    # every referenced ID must resolve (instance analog of OQ-067)
no_cycles: [derived_from]        # acyclic on these edge types
require:
  - { kind: HAZ,  edge: mitigated_by, min: 1, severity: error }
  - { kind: MIT,  edge: verified_by,  min: 1, severity: error }
  - { kind: REQ,  edge: verified_by,  min: 1, severity: warning }   # requirements coverage
  - { kind: CAPA, edge: triggered_by, min: 1, severity: error }
```

## 10. Engine surface

```
openqms trace-instances [--scope CARDIO] [--policy trace-policy.yaml] [--format json|md]
```

Walks markdown records (Tier 1 + Tier 2) in P15.1; adds the issue-export source in P15.2. Emits forward + reverse maps + invariant findings + orphan list — a deliberate mirror of `openqms trace` so the mental model carries over.

## 11. Composition with what exists

- `record_kind`, `record_id`, `trace_links` are **additive** frontmatter fields — `template_schema.py` already ignores extras, so no existing template breaks.
- New `scripts/lint-trace-links.py` (parallel to `lint-template-frontmatter.py` + `lint-module-yaml.py`) validates ID grammar + vocabulary + cell syntax — a pre-pytest CI gate.
- The walker enforces the policy invariants (the runtime check), the linter enforces syntax (the static check). Same split as module-YAML today.

## 12. Phasing

| Phase | Scope | Deliverable |
|---|---|---|
| **P15.1a** | Tier-1 frontmatter only, markdown | schema + linter + `trace-instances` walker over whole-record docs + policy + tests + docs |
| **P15.1b** | Tier-2 in-body item tables | table parser + RMF/SRS migrated to ID+links columns |
| **P15.2** | GitHub-issue substrate | structured issue-form fields + `gh` export → unified graph |

P15.1a is the contained, demo-able slice that proves the differentiator without the ~20–40-template migration or the API dependency.

---

## 13. Decisions

**All resolved 2026-05-31:**
1. ✅ **Granularity** — two-tier. Tier-1 first (P15.1a), Tier-2 tables next (P15.1b). (§2)
2. ✅ **Edge vocabulary** — typed, directed edges with auto-materialized inverse. (§5)
3. ✅ **SCOPE token** — mandatory for product-bound kinds, optional for process-level kinds (refined from "blanket mandatory" once real product-agnostic doc-numbering surfaced); `require_scope: false` opt-out for single-product forks. (§3)
4. ✅ **record_id vs document_id** — **always separate.** `document_id` stays the company's product-agnostic document-control ID (QAP/DWI/QTP/...); `record_id` is the kind-typed, product-scoped trace node; `source_document` auto-derived. (§6)
5. ✅ **Apply-to-P2-now** — yes. P2's URS/IQ/OQ/PQ templates carry §6 frontmatter as authored; the URS→IQ→OQ→PQ chain (`derived_from` / `validated_by`) is the first clean exercise of the grammar.

**Schema is settled.** Next: build order is P2 (CSV-framed, pending Aaron's CSA-vs-CSV research) → P15.1a → P15.1b → P15.2.
