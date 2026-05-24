# Companion — Overlay modules (v0.11.0 + v0.12.0)

**Dates:** 2026-05-23
**Public commits:** `54e93de` + `edfc2f0` (v0.11.0) + `f0d48f7` + `361f4ff` + `3e231d5` + `093c35f` (v0.12.0)
**Range:** `aa51574..093c35f`
**Spec deltas:** 9 NEW module-tier entries (OQ-050 through OQ-058) — all `:tested`. Spec total grows 46 → 50 → 55.

## §1 Computational basis

Two release cycles delivered nine overlay modules spanning two orthogonal dimensions:

- **Device category overlays** — what kind of device: SaMD (software-only), implantable, IVD.
- **Risk-class overlays** — what regulatory class under which jurisdiction: EU MDR Class IIa / IIb / III; FDA Class II (510(k)) / III (PMA).

Plus a **cross-cutting AI overlay** that composes with any vertical regulatory module — medical-devices today; future fintech / employment / automotive AI verticals later.

### v0.11.0 — first 4 overlay modules

**Files new:**

- `modules/samd/` — Software as a Medical Device. 3 clauses: IMDRF SaMD risk categorization framework (Class I-IV on State-of-Healthcare-Situation × Significance-of-Information axes), IEC 82304-1 health software product safety, SaMD cybersecurity. Binds to new SAMD-INTENDED-USE-TEMPLATE + existing SOFTWARE-REQUIREMENTS-TEMPLATE + existing RISK-MANAGEMENT-FILE-TEMPLATE.
- `modules/implantable/` — Implantable medical devices. 3 clauses: MDR Annex I §23.4 (implant card), Article 32 (SSCP), ISO 14708-1 (active implantable general requirements). Binds to new IMPLANT-CARD-TEMPLATE + new SSCP-TEMPLATE + existing VERIFICATION-PROTOCOL-TEMPLATE.
- `modules/mdr-class-iii/` — EU MDR Class III risk class. 4 clauses: MDR Article 32 (SSCP, shared with implantable), Article 54 (expert panel consultation), Annex X (type-examination), Article 84 (PSUR annual cadence). Binds to SSCP-TEMPLATE + new EXPERT-PANEL-CONSULTATION-TEMPLATE + existing technical-file index + existing PMCF template.
- `modules/fda-class-iii/` — FDA Class III / PMA path. 4 clauses: 21 CFR 814 Subpart B (PMA application), §814.39 (PMA supplements), §814.84 (PMA annual report), 21 CFR 803 (FDA Medical Device Reporting — not to be confused with EU MDR). Binds to new PMA-SUBMISSION-TEMPLATE + existing change-request + complaint + management-review templates.

- 5 new templates: SAMD-INTENDED-USE, IMPLANT-CARD, SSCP, EXPERT-PANEL-CONSULTATION, PMA-SUBMISSION.
- 5 new standards in registry: IEC 82304-1:2016, ISO 14708-1:2014, 21 CFR 814, 21 CFR 803, IMDRF SaMD N12.
- `bundles/example-samd.yaml` updated to include `samd` overlay + IEC 82304-1 + IMDRF SaMD N12 standards.

### v0.12.0 — 5 more overlay modules in three phases

**Phase A (commit `f0d48f7`):** Additional class overlays.

- `modules/mdr-class-iib/` — EU MDR Class IIb. 3 clauses: Article 54 expert panel (active drug-delivery subset), Annex IX Class IIb conformity, Article 84 biennial PSUR. MDR-Art54 declared identically across iib + iii overlays → silent dedup.
- `modules/mdr-class-iia/` — EU MDR Class IIa. 2 clauses: Annex XI production quality assurance, Article 83 as-needed PMS.
- `modules/fda-class-ii/` — FDA Class II (510(k)). 3 clauses: 21 CFR 807 Subpart E Premarket Notification, Special Controls, 21 CFR 860 Subpart D De Novo. Ships 510K-SUBMISSION-TEMPLATE.
- Registry additions: 21 CFR 807, 21 CFR 860.

**Phase B (commit `361f4ff`):** IVD overlay.

- `modules/ivd/` — In Vitro Diagnostic. 8 clauses: EU IVDR Article 5 + Annex I (IVD GSPRs) + Annex II + Annex IX + Annex XIII (performance evaluation: scientific validity + analytical performance + clinical performance) + Article 56 (PSUR cadence per class A/B/C/D); 21 CFR 809 (FDA IVD labeling); ISO 15189:2022 (medical lab quality).
- 2 new templates: IVDR-GSPR-CHECKLIST (analogous to MDR GSPR but IVD-specific), PERFORMANCE-EVALUATION-REPORT (IVD equivalent of CER).
- Registry additions: EU IVDR 2017/746, 21 CFR 809, ISO 15189:2022.
- Pragmatic shipping decision: cross-cutting overlay (not standalone vertical). Adopters compose with medical-devices for the shared QMS baseline; declare medical-devices MDR-specific clauses (MDR-Art10(9), MDR-AnnexI, MDR-AnnexII, MDR-AnnexIX, MDR-AnnexXIV-A, MDR-AnnexXIV-B) as NA per IVD scope SOP. Future `medical-devices-ivd` standalone vertical excluding MDR clauses entirely remains forward work.

**Phase C (commit `3e231d5`):** Regulated-AI cross-cutting overlay.

- `modules/regulated-ai/` — composes with ANY vertical. 13 clauses:
  - NIST AI RMF 1.0 four functions: Govern, Map, Measure, Manage.
  - EU AI Act Chapter III §2 (high-risk AI requirements): Articles 9, 10, 11, 12, 13, 14, 15.
  - ISO/IEC 42001:2023 AIMS (consolidated).
  - ISO/IEC 23894:2023 AI risk management guidance.
- 2 new templates: AI-SYSTEM-CARD (Mitchell et al. 2019 Model Card extended with EU AI Act + IMDRF SaMD), AI-IMPACT-ASSESSMENT (Article 9 + Article 14 + Article 27 + NIST AI RMF Govern/Map/Measure/Manage).
- Existing template bindings extended: RMF → ISO 23894; quality-policy → ISO 42001 AIMS; SAD → EU AI Act Art 15; STP → EU AI Act Art 10; TFI → EU AI Act Art 12.
- Registry addition: ISO/IEC 23894:2023.

**Files modified:**

- Registry: 6 new standards added across the cycle (5 at v0.11.0; 6 at v0.12.0 but ISO 23894 was the only truly net-new addition since others were already registered as roadmap entries at v0.5.0).
- `engine/openqms/{__init__,pyproject.toml}` — 0.10.0 → 0.11.0 → 0.12.0.

**Test environment:** unchanged. Test count remains 97 throughout (overlay shipping is content not engine code). Each overlay validates standalone; the full 7-module mega-composite (`medical-devices + ivd + samd + regulated-ai + mdr-class-iii + fda-class-iii + iso-27001`) validates cleanly.

## §2 Results

- **9 new module-tier entries.** OQ-050 (SaMD), OQ-051 (implantable), OQ-052 (MDR III), OQ-053 (FDA III), OQ-054 (MDR IIb), OQ-055 (MDR IIa), OQ-056 (FDA II), OQ-057 (IVD), OQ-058 (regulated-AI). All `:tested`.
- **Two orthogonal dimensions covered.** Device category (SaMD / implantable / IVD) × risk class (FDA II/III, MDR IIa/IIb/III). Adopters compose per their specific device profile.
- **Composition primitive validated at scale.** The 7-module mega-composite resolves cleanly. Demonstrates: AI overlay composes with any vertical; IVD overlay composes alongside medical-devices; class overlays stack; dedup-by-content-equality (OQ-011) handles MDR-Art54 + MDR-Art32 across multiple overlays without conflict.
- **Templates: 18 → 26 (v0.11.0) → 31 (v0.12.0).** 5 added in v0.11.0 (device-class overlay templates); 5 added in v0.12.0 across phases (510K, IVDR-GSPR, PERFORMANCE-EVALUATION, AI-SYSTEM-CARD, AI-IMPACT-ASSESSMENT).
- **Registry: 21 → 26 standards** (v0.11.0 added 5; v0.12.0 effectively added 4 net new since ISO 23894 was the only true new addition).
- **Honest scope notes carried throughout:**
  - **Class I (FDA + MDR) overlays not shipped.** Their "additions" over baseline medical-devices are subtractions (exemptions from §820.30 design controls for Class I; reduced 510(k) for Class II) which don't fit the union-based compose primitive. Adopters use medical-devices directly with applicability notes.
  - **IVDR class overlays** (ivdr-class-c, ivdr-class-d) remain forward work analogous to MDR class overlays.
  - **`medical-devices-ivd` standalone vertical** that excludes MDR clauses entirely remains forward work.
  - **CLIA (42 CFR 493)** deferred — applies to labs operating tests, not IVD manufacturers; ISO 15189:2022 partially overlaps.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-050 | SaMD overlay shipped | example-tested | Module validates standalone + in composite; example-samd bundle exercises it via the `samd` module list entry. |
| OQ-051 | Implantable overlay shipped | example-tested | Module validates standalone + in composite (with mdr-class-iii). MDR-Art32 declared identically in both overlays → silent dedup. |
| OQ-052 | EU MDR Class III overlay shipped | example-tested | Module validates standalone + in composite. Article 54 + Article 32 + Annex X + Article 84 clauses bound to existing + new templates. |
| OQ-053 | FDA Class III overlay shipped | example-tested | Module validates standalone + in composite. PMA + supplements + annual report + FDA MDR bound to new PMA template + existing issue templates + management-review. |
| OQ-054 | EU MDR Class IIb overlay shipped | example-tested | Module validates standalone + in composite. MDR-Art54 + Annex IX IIb + Article 84 biennial PSUR. |
| OQ-055 | EU MDR Class IIa overlay shipped | example-tested | Module validates standalone + in composite. Annex XI PQA + Article 83 as-needed PMS. |
| OQ-056 | FDA Class II overlay shipped | example-tested | Module validates standalone + in composite. 510(k) + Special Controls + De Novo. |
| OQ-057 | IVD overlay shipped (IVDR + 21 CFR 809 + ISO 15189) | example-tested | Module validates standalone + composite with medical-devices. 8 clauses; 2 new templates (IVDR-GSPR + PERFORMANCE-EVALUATION). |
| OQ-058 | Regulated-AI overlay shipped (NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894) | example-tested | Module validates standalone. 7-module mega-composite (with medical-devices + ivd + samd + mdr-iii + fda-iii + iso-27001) validates — demonstrates AI overlay composes with any vertical combination. |

## §4 Spec impact

| S-ID | Before | After | Evidence type after |
|---|---|---|---|
| OQ-050 | NEW (v0.11.0) | `:tested` | example-tested |
| OQ-051 | NEW (v0.11.0) | `:tested` | example-tested |
| OQ-052 | NEW (v0.11.0) | `:tested` | example-tested |
| OQ-053 | NEW (v0.11.0) | `:tested` | example-tested |
| OQ-054 | NEW (v0.12.0) | `:tested` | example-tested |
| OQ-055 | NEW (v0.12.0) | `:tested` | example-tested |
| OQ-056 | NEW (v0.12.0) | `:tested` | example-tested |
| OQ-057 | NEW (v0.12.0) | `:tested` | example-tested |
| OQ-058 | NEW (v0.12.0) | `:tested` | example-tested |
| OQ-038 | `:tested` (template count notes) | `:tested` | example-tested |

Status counts at end of v0.12.0: 47 `:tested` · 8 `:argued` · 0 `:open` · total 55.

**Module-tier coverage now spans 19 entries:**
- 10 medical-devices coverage (OQ-040..OQ-049)
- 4 v0.11.0 device-class overlays (OQ-050..OQ-053)
- 5 v0.12.0 overlays (OQ-054..OQ-058)

OpenQMS is now a comprehensively populated regulated-industry QMS generator covering medical-devices + IVD + AI across both EU (MDR / IVDR / AI Act) and US (FDA QSR / PMA / 510(k) / MDR) regulatory frameworks. The composition primitive demonstrates end-to-end usability at scale (7-module mega-composite resolves cleanly). Per-vertical extension is now a pattern — add a new vertical module (financial-services, automotive, food-safety, etc.) and the existing overlays (regulated-ai, iso-27001) compose with it.
