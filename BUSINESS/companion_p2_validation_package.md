# Companion — P2 validation-package overlay (DRAFT)

**Status:** DRAFT design proposal · pre-implementation · not yet a spec entry
**Date:** 2026-05-31
**Addresses:** P2 (the highest-value remaining adopter deliverable) — a risk-based computerized-system validation overlay for production / quality-management-system software.
**Maintainer:** Aaron Green
**Depends on:** the trace-link schema in `companion_p15_trace_schema.md` (P2 templates are authored trace-ready — schema decision #5).

This is the design we agree on before any templates are authored. Grounded in the **final FDA CSA guidance** (`~/Desktop/CSA.pdf`, issued 2026-02-03 — see the `fda-csa-guidance` memory).

---

## 1. The reframe (corrects an earlier draft framing)

It is **not "CSV vs CSA."** FDA's **Computer Software Assurance (CSA)** guidance is final (2026-02-03), supersedes **Section 6 of the General Principles of Software Validation** for production/QMS software, and is bound to **QMSR** (21 CFR Part 820 → ISO 13485:2016, effective 2026-02-02; validation obligations at ISO 13485 §4.1.6, §7.5.6, §7.6). CSA is the **overarching risk-based framework**; **classic CSV (robust scripted IQ/OQ/PQ) is its highest assurance tier**, applied to high-process-risk functions.

So the optionality the adopter wants — heavy validation for critical functions, lighter assurance for non-critical — is **native to CSA's risk-based determination**, not a fork between two methodologies.

**CSA Table 1 — the four assurance tiers** (the rigor dial):

| Tier | Test plan | Record depth | ≈ traditional |
|---|---|---|---|
| **Scripted — Robust** | objectives + step-by-step cases + expected results + independent review | detailed report + per-case results | **classic CSV / IQ-OQ-PQ** |
| **Scripted — Limited** | limited step-by-step cases + identify unscripted applied | summary + per-case results | lighter CSV |
| **Unscripted — Scenario / Error-guessing** | features / failure-modes, no test plan | summary + issues | — |
| **Unscripted — Exploratory** | high-level objectives w/ pass-fail, no step-by-step | summary + issues | — |

Tier is selected by the **risk-based analysis**, NOT rigidly: the guidance states unscripted testing can suit high-risk functions and scripted automation can suit low-risk ones (§V.A.4). Open QMS must not hard-code high→scripted.

---

## 2. Architecture — two orthogonal dials

P2 is **one baseline overlay + two dials**. It is NOT a `validation-csv` / `validation-csa` split (CSA lets a single system mix tiers per function — the worked examples do exactly this).

```
validation-package                 ← baseline, market-NEUTRAL spine (GAMP 5 2nd ed.)
   │                                  system inventory · VMP · Assurance Determination ·
   │                                  tier-aware Assurance Record · vendor-leverage · traceability
   ├── validation-package-fda       ← MARKET dial (US): CSA framework + 21 CFR Part 11 + Part 820/QMSR
   └── validation-package-eu        ← MARKET dial (EU): EU GMP Annex 11 + Annex 15 + ISO 13485 §7.5.6/7.6
```

- **Dial 1 — rigor (per function):** assurance tier, an *output of the determination*. Lives in data (a field on each function row), not in module composition.
- **Dial 2 — market (per fork/bundle):** which regulatory overlay you compose. Composes via the existing `compose` primitive + bundles, exactly like every other Open QMS overlay.

A critical-device fork bundles `medical-devices + validation-package + validation-package-fda`; its high-process-risk systems land on robust scripted. A pharma fork bundles `validation-package + validation-package-eu`. A US+EU product bundles both market overlays (clause sets union; no conflict — they cite different predicate rules over the same risk-based spine).

---

## 3. Module + template layout

```
modules/validation-package/module.yaml            # baseline clauses (GAMP 5 + ISO 13485 §4.1.6/7.5.6/7.6 + 29119-1)
modules/validation-package-fda/module.yaml         # CSA + Part 11 + Part 820 clauses
modules/validation-package-eu/module.yaml          # Annex 11 + Annex 15 clauses

templates/qms-validation/
  SYSTEM-INVENTORY-TEMPLATE.md                      # the computerized-system register (SYS)
  ASSURANCE-DETERMINATION-TEMPLATE.md               # the per-function risk decision (FDA 5-column)  ← the human judgment
  ASSURANCE-RECORD-TEMPLATE.md                      # tier-aware evidence record (Table 1 fields)
  VENDOR-LEVERAGE-ASSESSMENT-TEMPLATE.md            # §V.A.5 — reuses supplier-evaluation pattern
  URS-TEMPLATE.md                                   # user requirements (URS)
  IQ-PROTOCOL-TEMPLATE.md / OQ- / PQ-               # robust-scripted-tier instances (IQ/OQ/PQ)
```

VMP already exists (`templates/product-pharma/validation/VALIDATION-MASTER-PLAN-TEMPLATE.md`) — generalize it into `qms-validation/` or cross-reference. Change Assessment already exists (`product-pharma/change-control/CHANGE-CONTROL-TEMPLATE.md`) — reuse for §V.A.3 software changes.

---

## 4. The Assurance Determination — the human risk decision (FDA's own format)

FDA gives the artifact shape: the Appendix A example tables are a **5-column determination**. Open QMS adds an `ID` and a P15 `Trace links` column, making the determination a **P15 Tier-2 item table** — so P2 is the first real exercise of the instance-trace schema:

| ID | Feature / Function / Operation | Intended Use | Risk-Based Analysis | Assurance Tier | Trace links |
|---|---|---|---|---|---|
| `FUNC-CARDIO-0012` | Product-containment trigger | directly | **high process risk** — failure ⇒ correction not initiated ⇒ foreseeable safety compromise | scripted-robust | `part_of:SYS-CARDIO-0003; assured_by:VREC-CARDIO-0044; validates:URS-CARDIO-0007` |
| `FUNC-CARDIO-0013` | NC initiation workflow | directly | not-high — containment controls exist downstream | unscripted-exploratory | `part_of:SYS-CARDIO-0003; assured_by:VREC-CARDIO-0045` |

- **Intended Use** is the §V.A.1 classification: `directly` / `support` / `not` part of production-or-QMS. (`not` ⇒ ISO 13485 §4.1.6/7.5.6/7.6 don't apply — e.g. email, accounting, generic infrastructure.)
- **Risk-Based Analysis** is the §V.A.2 call: `high-process-risk` (failure foreseeably compromises safety) vs `not-high`, with rationale. **This is the documented human judgment — Open QMS records it, never makes it (OQ-080).**
- **Assurance Tier** is the §V.A.4 output (Table 1 tier).

## 5. The tier-aware Assurance Record (§V.A.6 + Table 1)

One template; required sections gate on the declared tier. Field set lifted directly from the guidance:

- **Always:** intended use · risk-based-analysis result · description of testing performed · issues found (deviations/defects/failures) · conclusion of acceptability (+ resolution / risk justification of issues) · who performed + date · review/approval signature *when appropriate*.
- **+ Scripted-robust:** detailed test protocol + expected results + result for each test case + detailed report + independent review/approval.
- **+ Scripted-limited:** limited test cases + note unscripted methods applied.
- **Unscripted:** summary of features/failure-modes tested (no per-case protocol).

Digital records preferred (§V.A.6): system logs, audit trails, automated traceability over paper/screenshots — aligns with Open QMS's git-native evidence model + the OQ-067 trace tooling.

---

## 6. Market overlays — clause crosswalks

**`validation-package` (baseline, neutral):**
- **GAMP 5 (2nd ed.)** — risk-based lifecycle + software categories (1 infrastructure / 3 non-configured COTS / 4 configured / 5 custom); the market-neutral bridge.
- **ISO 13485 §4.1.6** (validation of QMS software application), **§7.5.6** (validation of production/service software), **§7.6** (M&M software).
- **IEC/IEEE/ISO 29119-1:2022** — testing taxonomy (scripted / unscripted / scenario / error-guessing / exploratory), cited by CSA.

**`validation-package-fda` (US):**
- **FDA CSA guidance** (2026-02-03) — intended-use classification, high-process-risk determination, Table 1 tiers, vendor leverage §V.A.5, record §V.A.6.
- **21 CFR Part 11** — e-records/e-sigs; the §V.B mapping (a Part-820-required record kept electronically is a Part-11 record; enforcement discretion does *not* extend to ISO 13485 §4.1.6/7.5.6/7.6 validation).
- **21 CFR Part 820 (QMSR)** — predicate rule via ISO 13485:2016.
- Note: supersedes GPSV §6.

**`validation-package-eu` (EU):**
- **EU GMP Annex 11** (Computerised Systems) + **Annex 15** (Qualification & Validation — DQ/IQ/OQ/PQ definitions); Eudralex Vol 4.
- **ISO 13485 §7.5.6/7.6** shared device backbone (for EU device QMS computerized systems under MDR Annex IX).
- Risk management per **Annex 11 §1 + ICH Q9**. Note: "CSA" is an FDA term not used in EU; the EU overlay frames the same risk-based spine in Annex 11/15 language.

**Registry additions needed:** GAMP 5 2nd ed. (commercial, ISPE) · IEC/IEEE/ISO 29119-1:2022 (commercial) · FDA CSA guidance (public) · FDA GPSV (public) · EU GMP Annex 11 (public) · EU GMP Annex 15 (public) · ICH Q9 (public). 21 CFR Part 11 / Part 820 / ISO 13485 already registered.

---

## 7. Trace-link integration (P15 dependency)

New record kinds to add to the P15 §4 vocabulary: `SYS` (computerized system), `FUNC` (feature/function/operation — the determination unit), `VREC` (assurance record). `URS` / `IQ` / `OQ` / `PQ` / `TST` already in §4.

**Two new edges P2 surfaces — proposed amendments to P15 §5 vocabulary:**

| Forward | Inverse | Pair |
|---|---|---|
| `part_of` | `comprises` | FUNC part_of SYS |
| `assured_by` | `assures` | FUNC assured_by VREC |

(`validated_by` / `verified_by` / `derived_from` / `implements` already cover URS↔PQ, FUNC↔TST, IQ/OQ/PQ↔URS, IQ/OQ/PQ↔VMP.) These two additions are the honest consequence of P2 informing the schema — fold them back into `companion_p15_trace_schema.md` §5.

All P2 templates carry the §6 frontmatter (`record_kind` + `record_id` + `trace_links`) as authored. The Assurance Determination is a Tier-2 trace table (§4 above).

---

## 8. Verifiable backbone — `validation-policy.yaml`

Mirrors `deployment-policy.yaml` (P11) and `trace-policy.yaml` (P15). Adopter-configurable; checks the *substrate*, never the judgment:

```yaml
# validation-policy.yaml
require:
  - { rule: every SYS in inventory has >=1 FUNC determination,           severity: error }
  - { rule: every FUNC.intended_use in [directly, support, not],         severity: error }
  - { rule: every FUNC has >=1 assured_by VREC (unless intended_use=not), severity: error }
  - { rule: every VREC carries the V.A.6 required fields,                 severity: error }
  - { rule: high-process-risk FUNC uses a scripted tier,                  severity: warning }  # NOT error — CSA §V.A.4 says mapping is not rigid
```

The last rule is a **warning, not a gate** — encoding it as an error would contradict the guidance's "not exclusive" statement and overstep the adopter's judgment.

## 9. OQ-080 firewall

P2 ships the *framework + determination template + tier-aware record + policy check*. It records the risk decision and proves the artifact set matches the declared tier. It does **not** decide whether a function is high process risk, nor prove that a validated system is fit for use — those remain adopter QA judgment (and, where required, third-party assessment). The guidance itself: *"Manufacturers are responsible for determining the appropriate assurance activities."*

---

## 10. Phasing

| Phase | Scope |
|---|---|
| **P2.1** | Baseline `validation-package` module + System Inventory + Assurance Determination + tier-aware Assurance Record + VMP generalization + trace frontmatter + tests + guide |
| **P2.2** | `validation-package-fda` overlay (CSA + Part 11 + Part 820 crosswalks) + registry standards + composite validate + Part 11 §V.B mapping doc |
| **P2.3** | `validation-package-eu` overlay (Annex 11/15 + ISO 13485) + US+EU composite + IQ/OQ/PQ robust-tier protocol templates |
| **P2.4** | Dogfooding worked example: Open QMS's own CAPA/complaint/NCR GitHub-Issue workflow validated as a "not-high-process-risk" system (ties to P15 instance-trace) |

## 11. Decisions (resolved 2026-05-31)

1. ✅ **Determination artifact name** — **"Assurance Determination"** (mirrors FDA's column language).
2. ✅ **Tier vocabulary surface** — **expose all four** Table 1 tiers (scripted-robust / scripted-limited / unscripted-scenario / unscripted-exploratory); they map to distinct record-field sets.
3. ✅ **EU overlay headline** — **ISO 13485 §7.5.6/7.6 backbone + Annex 11/15 cited** (Open QMS's center of gravity is devices; pharma/GMP adopters get Annex 11/15 in the same overlay).
4. ✅ **GAMP 5 licensing** — **cite, don't reproduce.** Baseline references GAMP 5 (2nd ed.) by clause/concept but ships no copyrighted ISPE text — consistent with the OQ-070/071 standards-licensing posture.
