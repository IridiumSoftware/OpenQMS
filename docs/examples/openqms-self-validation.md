# Worked example — Open QMS validates its own QMS workflow

A dogfood of the [`validation-package`](../guide/validation-package.md) framework: Open QMS applies its own risk-based computerized-system validation to the **GitHub-hosted QMS** it ships. It mirrors **FDA CSA Appendix A, Example 1 (Nonconformance Management System)** — and reaches the same honest conclusion: this is **not high process risk**, so assurance is light and largely *leveraged*.

> This example validates the *project's* tooling. It does **not** certify that tooling for any adopter — each adopter validates their **own** deployment (see [`verify-deployment`](../guide/verify-deployment.md)). OQ-080 firewall.

## 1. The system (inventory)

`SYS-OPENQMS-001` — the GitHub-hosted QMS: **Issue Forms** (`.github/ISSUE_TEMPLATE/` — `capa.yml`, `complaint.yml`, `nonconformance.yml`, …) for records; **GitHub Actions** (`doc-control.yml`, `training-trigger.yml`, `engine-tests.yml`, `signature-check.yml`) for automated QMS processes; **Git** for record storage + audit trail; the **`openqms` engine** for scaffold generation + traceability.

- **Intended use:** *directly* part of the QMS — it creates and maintains quality records (ISO 13485 §4.2.5).
- **GAMP category:** 3–4 (configured COTS — GitHub — plus category-5 custom code in the `openqms` engine).

## 2. Risk-based analysis

**Not high process risk.** The functions are CAPA routing, complaint logging/tracking, nonconformance tracking, automated change control, and automated logging — exactly the activities FDA CSA §V.A.2 lists as *not high process risk*. Failure would not foreseeably compromise device safety: records are human-reviewed, and the engine makes **no** automated acceptance decision about any product. So assurance is **commensurate with process risk** (the lighter end).

## 3. Assurance determination (CSA 5-column · P15 Tier-2 trace table)

| ID | Feature / function | Intended use | Risk-based analysis | Assurance tier | Trace links |
|---|---|---|---|---|---|
| `FUNC-OPENQMS-001` | Record intake (CAPA / complaint / NC issue forms) | directly | not high — human-reviewed records, no product decision | unscripted-exploratory + vendor leverage | `part_of:SYS-OPENQMS-001; assured_by:VREC-OPENQMS-001` |
| `FUNC-OPENQMS-002` | CAPA routing + lifecycle labels | directly | not high — CSA-named not-high example | unscripted-scenario + vendor leverage | `part_of:SYS-OPENQMS-001; assured_by:VREC-OPENQMS-001` |
| `FUNC-OPENQMS-003` | Audit trail (git history + Signature-Meaning trailers) | directly | not high — append-only history; integrity leveraged from Git/GitHub | vendor leverage + monitoring | `part_of:SYS-OPENQMS-001; assured_by:VREC-OPENQMS-002` |
| `FUNC-OPENQMS-004` | Doc-control gate (`doc-control.yml`) | directly | not high — CI gate; human approval still required | **scripted-limited** (`test_doc_control.py`) | `part_of:SYS-OPENQMS-001; assured_by:VREC-OPENQMS-003` |
| `FUNC-OPENQMS-005` | Traceability zero-orphan invariant (`openqms trace --all`) | directly | not high — assurance check, not a product decision | **scripted-limited** (`test_trace.py` + CI invariant) | `part_of:SYS-OPENQMS-001; assured_by:VREC-OPENQMS-003` |

**Note the mix:** the GitHub-hosted record-keeping functions take *unscripted + leveraged* assurance, while the **engine's own automation** (doc-control, trace) is covered by *scripted* tests — one system, tiers mixed per function, exactly as CSA intends.

## 4. Vendor leverage (CSA §V.A.5)

- **GitHub** (the platform vendor): SOC 2 / ISO 27001 certifications cover availability, access control, and data integrity of Issues/Actions/Git — leveraged rather than re-tested.
- **Open QMS's own CI as continuous assurance + monitoring:** the engine test suite (**265 tests**), `lint-module-yaml` + `lint-template-frontmatter` gates, the `coverage --all` 100% and `trace --all` zero-orphan invariants, and `signatures export` run on every push — ongoing objective evidence that the system maintains a validated state.

## 5. Assurance record (summary)

`VREC-OPENQMS-001..003` —

- **Intended use / risk result:** as §§1–2 (directly used in QMS; not high process risk).
- **Assurance activities:** vendor-certification review (GitHub); the CI suite as scripted-limited evidence for the engine gates; exploratory use for the issue-form workflows.
- **Issues found:** tracked as repository issues; none open that affect intended use.
- **Conclusion:** acceptable for intended use; validated state maintained by the CI invariants on every push.
- **Who / when:** git commit history (author + timestamp); Signature-Meaning trailers where applied.

## 6. Part 11 / Annex 11 applicability

Records required under Part 820 (e.g., CAPA, NC, complaint records) that are maintained electronically here are **Part 11 electronic records**; Git's commit history + the [Signature-Meaning convention](../guide/signature-meaning.md) provide the audit trail and signature manifestation. The EU equivalent is GMP Annex 11 §§5–9/§12 (data integrity) + §14 (e-signatures) — see `ELECTRONIC-RECORDS-CONTROLS-TEMPLATE`.

## 7. Forward (P15 instance-trace)

The `SYS-` / `FUNC-` / `VREC-` IDs above are written to the P15 trace grammar; once `openqms trace-instances` ships (P15.1), this example becomes a live, walkable instance-trace — Open QMS's own validation graph, checked in CI alongside the clause-level one.
