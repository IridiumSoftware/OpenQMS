# Instance-level traceability (`trace-instances`)

Two layers of traceability ship in Open QMS:

| Layer | Proves | Command | Operates on |
|---|---|---|---|
| **Clause-level** (OQ-067) | every in-scope clause has ≥1 bound template | `openqms trace` | `modules/*/module.yaml` |
| **Instance-level** (P15) | the *living records* link up correctly | `openqms trace-instances` | your record markdown files |

This page covers the second — the **cross-record graph** the reviewer named ("connectedness is where modern systems win"): requirement ↔ hazard ↔ mitigation ↔ test ↔ CAPA ↔ complaint ↔ post-market finding.

> **Status:** P15.1a + **P15.1b** shipped — **Tier-1** (whole-record frontmatter) **and Tier-2** (in-body item tables) both walked. The GitHub-issue substrate (P15.2) is forthcoming. Full schema: `BUSINESS/companion_p15_trace_schema.md`.

## How records join the graph

Each record-producing markdown file declares three fields in its YAML frontmatter:

```yaml
record_kind: HAZ                      # controlled vocabulary
record_id:   HAZ-CARDIO-0007          # KIND-SCOPE-NNNN
trace_links:
  mitigated_by: [MIT-CARDIO-0011]     # typed, directed edge
```

- **IDs** are `KIND-SCOPE-NNNN` (e.g. `HAZ-CARDIO-0007`). SCOPE is required for product-bound kinds (REQ/URS/HAZ/MIT/TST/IQ/OQ/PQ/FUNC) and optional for process kinds (CAPA/CMPL/NCR/CHG/AUD/SUP/SYS/VREC/PMS).
- **Edges are typed and directed**, and the **inverse is materialized automatically** — declare `mitigated_by` on the hazard *or* `mitigates` on the mitigation; the graph records both either way. Relationships: `derived_from` · `mitigated_by` · `verified_by` · `validated_by` · `triggered_by` · `implements` · `part_of` · `assured_by` · `relates_to`.

## Two tiers

- **Tier-1 — whole-record docs.** One record per file (a CAPA, a complaint, an assurance record). Identity + links live in the **frontmatter** (above).
- **Tier-2 — item tables.** A *container* document holds many items as rows (a Risk Management File holds many hazards; an SRS holds many requirements). Each row is its own node, declared in a **trace table** — a markdown table with an `ID` column and a `Trace links` column:

  ```markdown
  | ID | Hazard | Severity | Trace links |
  |---|---|---|---|
  | HAZ-CARDIO-0007 | Over-infusion | Critical | mitigated_by:MIT-CARDIO-0011; verified_by:TST-CARDIO-0021 |
  ```

  The walker recognizes a trace table by those two columns; rows whose `ID` is a blank-template placeholder (`HAZ-[PRODUCT]-001`) are skipped. The two tiers compose into **one** graph — a Tier-2 mitigation can be `verified_by` a Tier-1 test record. (The shipped `RISK-MANAGEMENT-FILE-TEMPLATE` and `examples/trace-instances/RMF-CARDIO-0100.md` demonstrate this.)

## Running it

```bash
openqms trace-instances --path <your-records-dir> --policy trace-policy.yaml
```

It runs the **static lint** (ID grammar + vocabulary + scope) and the **runtime invariants**, prints a json/md report, and **exits 1** if any error-severity finding exists — so it's a CI gate. The shipped worked example lives at `examples/trace-instances/` and is checked in CI.

## The policy

Invariants are configurable (mirrors `deployment-policy.yaml`). See `trace-policy.example.yaml`:

```yaml
referential_integrity: error      # every linked target must resolve
require_scope: true               # SCOPE mandatory on product-bound kinds
no_cycles: [derived_from]
require:
  - { kind: HAZ,  edge: mitigated_by, min: 1, severity: error }
  - { kind: MIT,  edge: verified_by,  min: 1, severity: error }
  - { kind: CAPA, edge: triggered_by, min: 1, severity: error }
  - { kind: FUNC, edge: assured_by,   min: 1, severity: error }
```

## Honesty bound (OQ-080)

This proves links *exist and resolve* (every hazard has a mitigation, every CAPA has a trigger, every referenced ID is real) — it does **not** prove a mitigation actually mitigates. That remains QA judgment.
