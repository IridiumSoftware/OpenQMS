# Companion — Phase 0 round-out (v0.2.1 + v0.2.2 + v0.3.0)

**Dates:** 2026-05-22
**Public commits:** `2fe3ef6` (P5) + `86bda4f` (P7) + `2625b98` (P6)
**Range:** `4a72a9f..2625b98`
**Spec deltas:** OQ-049 NEW `:tested`; OQ-062 `:open → :argued`; OQ-061 + OQ-068 + OQ-069 reframed (status unchanged); OQ-023 + OQ-038 notes updated.

## §1 Computational basis

The Phase 0 round-out closed the last three Phase 0 priorities from the v0.1.0 dashboard (P5, P6, P7) and shipped the workhorse templates the README had implicitly promised since the initial scaffold but hadn't yet delivered.

**v0.2.1 — P5: complaint intake + PHI/PII compartmentalization architecture**
- `.github/ISSUE_TEMPLATE/complaint.yml` — form-validated intake; required PHI-handling confirmation checkboxes; product / date received / source / severity / PHI-redacted description / regulatory reportability / CAPA linkage / PHI-bearing artifact reference fields.
- `docs/guide/complaints.md` — compartmentalization architecture: Pattern A (sibling private GitHub repo) vs Pattern B (external eQMS or encrypted document store). Workflow (intake → triage → investigation → CAPA dispatch → regulatory reporting → closure). Gotchas (email notifications carry content; closed issues retain content; cross-repo link discipline).
- `modules/medical-devices/module.yaml` — added ISO 13485 §8.2.2 + 21 CFR 820.198 clauses; bound to the new complaint template.

**v0.2.2 — P7: GPG signing enforcement guide**
- `docs/guide/gpg-signing.md` — runnable checklist for layering required-signed-commits enforcement on an Open QMS deployment. Five sections: pick signing scheme (GPG / SSH / S/MIME); per-individual key generation + GitHub registration; repository-level enforcement (`Settings → Branches → Require signed commits` + `gh api` equivalent); optional org-level defaults; CI belt-and-suspenders snippet that fails PRs containing unsigned commits + quarterly audit habit. Explicit limitations section (GitHub "Verified" certifies key→account but not account→person; web edits sign as GitHub; signature meaning is §11.50 / OQ-060 not §11.70).
- `scripts/setup.sh` not modified — enforcement requires admin permissions the standard `gh` CLI flow doesn't have.

**v0.3.0 — P6: product-dhf + product-sw template population**
- 8 new templates shipped, populating 8 of the 15 originally-empty `templates/` subdirectories:
  - `templates/product-dhf/risk-management/RISK-MANAGEMENT-FILE-TEMPLATE.md` — ISO 14971 RM file: plan, hazard analysis, risk control, residual risk evaluation, overall residual risk acceptability, risk-benefit analysis, RM report, production/post-production information.
  - `templates/product-dhf/verification/VERIFICATION-PROTOCOL-TEMPLATE.md` — Design verification per ISO 13485 §7.3.6 / 21 CFR 820.30(f).
  - `templates/product-dhf/validation/VALIDATION-PROTOCOL-TEMPLATE.md` — Design validation per ISO 13485 §7.3.7 / 21 CFR 820.30(g).
  - `templates/product-sw/requirements/SOFTWARE-REQUIREMENTS-TEMPLATE.md` — SRS per IEC 62304 §5.2 with risk-control requirements and traceability matrix.
  - `templates/product-sw/architecture/SOFTWARE-ARCHITECTURE-TEMPLATE.md` — SAD per IEC 62304 §5.3.
  - `templates/product-sw/soup-register/SOUP-REGISTER-TEMPLATE.md` — SOUP register per IEC 62304 §8.1.2.
  - `templates/product-sw/test/SOFTWARE-TEST-PROTOCOL-TEMPLATE.md` — Test protocol covering IEC 62304 §5.5 / §5.6 / §5.7.
  - `templates/product-sw/release/SOFTWARE-RELEASE-TEMPLATE.md` — Software release record per IEC 62304 §5.8.
- Module manifest extended with 14 new clauses (ISO 14971 §4-10; IEC 62304 §5.2, 5.3, 5.5, 5.6, 5.7, 5.8, 8.1.2) and 8 new template bindings. Standards list grows 2 → 4 (adds `ISO 14971:2019` and `IEC 62304:2006+A1:2015`).
- Validation harness passes on the expanded manifest: 6 → 20 clauses, 4 → 12 templates.

**Build / test:** unchanged from v0.2.0 baseline. `pip install -e './engine[dev]'` + `pytest engine/tests -v`. 15 tests, all green throughout the round-out.

## §2 Results

- **Templates: 3 → 11 document templates.** The Phase 0 baseline had 3 (quality-policy, SOP, design-input). After v0.3.0: 11.
- **Module clauses: 4 → 20.** The medical-devices module's machine-readable manifest grew from 4 clauses (v0.2.0) to 6 (v0.2.1) to 20 (v0.3.0). Validation harness green throughout.
- **PHI/PII architecture decision documented.** v0.2.1 captures the explicit two-pattern choice (sibling private repo vs external eQMS), upgrading OQ-062 from "no decision made" to "decision documented, adopter chooses per SOP."
- **GPG enforcement adopter-actionable.** v0.2.2 captures the §11.70 substrate enforcement path as a runnable checklist; OQ-023 stays `:argued` because the mechanism itself is unchanged, but adopters now have a documented path.
- **OQ-049 introduced as first complete-coverage module-tier entry.** ISO 14971's seven substantive clauses (§4-§10) are all in the manifest and all bound to the RM template — the first standard for which the medical-devices module hits full coverage.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-069 | Complaint issue template exists with form validation + required PHI-handling confirmation | example-tested | `.github/ISSUE_TEMPLATE/complaint.yml` shipped at v0.2.1; form validation enforced by GitHub form-spec at submission time. |
| OQ-062 | PHI/PII compartmentalization architecture is documented | manual | `docs/guide/complaints.md` documents Pattern A + Pattern B; intake template explicitly carries PHI-redaction discipline. Status `:argued` not `:tested` because the mechanism is procedural, not mechanically enforced. |
| OQ-023 | GPG signing enforcement is adopter-actionable | manual | `docs/guide/gpg-signing.md` ships a runnable checklist. Stays `:argued` — Open QMS itself can't enforce org-level GPG enforcement; adopters do per checklist. |
| OQ-049 | ISO 14971:2019 full coverage | example-tested | Module manifest includes ISO14971-4 through ISO14971-10 bound to RM template; validation harness passes. |
| OQ-068 | Template subdirectory population (partial at v0.3.0) | example-tested | 8 of original 15 empty subdirs populated; 7 remain placeholder-only (qms-* + design-outputs + technical-file). |

## §4 Spec impact

| S-ID | Before | After | Evidence type after | Notes |
|---|---|---|---|---|
| OQ-061 | `:tested` (gap framing) | `:tested` (claim reframed) | example-tested | Claim now describes post-fix state (PyYAML parsing). |
| OQ-062 | `:open` | `:argued` | manual | Architecture decision made; SOP-bound. |
| OQ-067 | `:open` | `:argued` | none | Broken script ref removed at v0.1.1; forward path documented. |
| OQ-068 | `:tested` (gap framing) | `:tested` (claim reframed) | example-tested | 8 of 15 originally-empty subdirs populated. |
| OQ-069 | `:tested` (gap framing) | `:tested` (claim reframed) | example-tested | Complaint template shipped. |
| OQ-023 | `:argued` | `:argued` | manual | Mechanism unchanged; documentation closes actionability gap. |
| OQ-038 | `:tested` | `:tested` | example-tested | Template count 3 → 11 (notes only). |
| OQ-049 | NEW | `:tested` | example-tested | First module-tier entry to reach full coverage. |

Status counts at end of v0.3.0: 20 `:tested` / 14 `:argued` / 6 `:open` (total 40 — pre-v0.6.0 reconciliation; actual total 46).
