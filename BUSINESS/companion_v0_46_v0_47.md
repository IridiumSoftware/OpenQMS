# Companion — v0.46.0 + v0.47.0 (HIPAA satellites + cross-overlay batch)

**Session date:** 2026-05-25 (paired with the v0.45.0 release-day arc)
**Engine version transitions:** 0.45.0 → 0.47.0 (2 releases)
**Why combined companion:** v0.46.0 was a small follow-up to the v0.45.0 HIPAA release (5 satellite templates + 1 new clause finishing the HIPAA story); v0.47.0 was a 5-cross-overlay batch. Combining into a single companion is proportionate to the per-release weight — neither warrants its own document but the combination is substantial enough to record.

## §1 Computational basis

Two sequential releases:

| Version | Date | Theme | Public commit | Spec entry |
|---|---|---|---|---|
| v0.46.0 | 2026-05-25 | HIPAA satellite templates + §164.509 clause + engine-version drift correction | `3c4461d` | (none — OQ-112 forward-work discharge; 1 new clause + 5 new templates added to existing OQ-112 module) |
| v0.47.0 | 2026-05-25 | Cross-overlay batch (5): connected-medical-device + cell-therapy-supply-chain + food-allergen-recall + defense-aerospace-cyber + digital-health-multi-region | `9b5fe43` | OQ-113 |

**Aggregate deliverables:**

- **1 NEW spec entry** (OQ-113)
- **5 new modules** (all cross-overlays at v0.47.0)
- **5 new templates** (all HIPAA satellites at v0.46.0)
- **1 new clause** added to existing hipaa module (HIPAA-164-509-reproductive-health-attestation at v0.46.0)
- **3 new registry standards** (FD&C §524B + FALCPA+FASTER Act + Cures Act; all PUBLIC; all v0.47.0)
- **Cross-overlay count:** 3 → 8 (+5 at v0.47.0)
- **Total module count:** 106 → 111 (+5 at v0.47.0)
- **Total template count:** 96 → 101 (+5 at v0.46.0)
- **Total registry standards:** ~126 → ~129 (+3 at v0.47.0)
- **Depth record:** 22-module healthcare ultimate composite (v0.45) → **24-module ultra composite** (v0.47)
- **Side fix:** engine version corrected from silently-stuck 0.43.0 to 0.46.0 at v0.46.0 release (root cause: parallel-batch edit failures in earlier release commits)

**Build commands** (replayable from clean checkout):

```bash
source .venv-engine/bin/activate

# v0.46.0 — HIPAA satellite templates
openqms validate --module hipaa                    # 15 clauses, 10 templates
openqms validate --module hipaa --module privacy   # most common pair

# v0.47.0 — cross-overlay validation
openqms validate --module medical-devices --module regulated-ai --module privacy --module iso-27001 --module hipaa --module connected-medical-device
openqms validate --module pharma --module atmp --module transport-hazmat --module cell-therapy-supply-chain
openqms validate --module food-safety --module recall-workflow --module privacy --module food-allergen-recall
openqms validate --module aerospace --module aerospace-defense --module defense-cui --module cmmc --module cmmc-level-2 --module defense-aerospace-cyber
openqms validate --module medical-devices --module privacy --module regulated-ai --module hipaa --module digital-health-multi-region

# 24-module ultra composite (v0.47 depth record)
openqms validate \
  --module medical-devices --module pharma --module combination-product \
  --module connected-medical-device --module digital-health-multi-region \
  --module pharma-sterile --module hipaa --module privacy \
  --module iso-27001 --module iso-27001-cloud --module iso-27001-privacy \
  --module regulated-ai --module iso-14001 --module iso-45001 \
  --module iso-50001 --module iso-37001 --module iso-22301 \
  --module iso-31000 --module integrated-management-system \
  --module soc-2 --module soc-2-type-ii \
  --module hitrust-csf --module hitrust-r2 --module iso-37301

# Repo-wide invariants (returns 111 modules / 828 clauses / 367 templates / 0 orphans)
openqms trace --all

# Test suite (116/116 pass) + linter (clean on 111 modules)
pytest engine/tests -q
python3 scripts/lint-module-yaml.py
```

## §2 Results

### v0.46.0 — HIPAA satellite templates + §164.509 clause

OQ-112 forward-work bucket discharged. 5 templates that complete the HIPAA story end-to-end, plus 1 new clause for the 2024 Reproductive Health Care Privacy Rule:

| Template | Section reference | Distinguishing feature |
|---|---|---|
| `HIPAA-AUTHORIZATION` | §164.508 | Required content + required statements + Compound-Authorization prohibition + psychotherapy-notes SEPARATE Authorization + cross-reference to §164.509 |
| `ACCOUNTING-OF-DISCLOSURES-LOG` | §164.528 | Exempted-disclosures catalog + temporary-suspension per §164.528(a)(2) + 60-day individual-request handling + first-accounting-free per 12-month |
| `RESTRICTION-REQUEST-LOG` | §164.522(a) + §164.522(b) | Permissive vs HITECH §13405(a) MANDATORY out-of-pocket restriction distinction (mandatory MUST be agreed by CE — billing-system segregation required) |
| `OCR-INVESTIGATION-RESPONSE` | §160 Subpart D + Resolution Agreement framework | Document-request response tracking + privileged-log discipline + CMP tier mapping per §160.404 HITECH 4-tier + 42 USC §1320d-6 criminal cross-reference + Wall of Shame public-listing risk |
| `REPRODUCTIVE-HEALTH-ATTESTATION` | §164.509 (HHS Final Rule 89 FR 32976) | Threshold determination + validity check + refusal handling + cross-state-line scenario (lawful provider state vs criminalised requestor state) |

New clause: `HIPAA-164-509-reproductive-health-attestation` — codifies the Final Rule effective 2026-12-23. Without this clause, the REPRODUCTIVE-HEALTH-ATTESTATION template would be orphaned (YAML linter caught this mid-release; added the clause + revalidated clean).

hipaa module evolution: **14 → 15 clauses, 5 → 10 templates**.

**Side fix — engine-version drift correction.** Mid-release discovery: `engine/pyproject.toml` + `engine/openqms/__init__.py` showed 0.43.0 despite v0.44.0 + v0.45.0 commits having shipped all other release content. Root cause: parallel-batch Edit calls in earlier release commits silently failed on the version-bump edits; all other content (modules + templates + spec + registry + dashboard + changelog + CI) went through. Corrected to 0.46.0 in this release + documented in changelog.

### v0.47.0 — Cross-overlay batch (5)

OQ-113 NEW `:tested`. Extends the cross-overlay shape (introduced at v0.44.0 OQ-111) to 5 additional vertical-intersection regulatory layers. Cross-overlay count: **3 → 8**.

#### connected-medical-device (medical-devices + regulated-ai + privacy + iso-27001 + hipaa)

7 clauses. The most-anticipated cross-overlay — SaMD-with-cloud-backend is the dominant new digital-health product category. Notable provisions:

- **FDA §524B cyber-device cybersecurity** per Sept 2023 Final Guidance — premarket submission requires (i) vulnerability monitoring plan + (ii) cybersecurity processes/procedures + (iii) SBOM per NTIA Minimum Elements + (iv) other FDA-deemed-necessary info. Applies to 510(k), De Novo, PMA, HDE, BLA, IDE.
- **EU MDR Annex I §17.2** + MDCG 2019-16 Cybersecurity Guidance + IEC 81001-5-1 (Health software safety + security activities)
- **FDA AI/ML SaMD Predetermined Change Control Plan (PCCP)** per Cures Act §3060(d) + April 2023 Final Guidance — pre-authorised algorithm modifications without new 510(k) per defined change scope + modification protocol + data management + training + V&V + impact assessment
- **NTIA Minimum Elements SBOM** — SPDX / CycloneDX / SWID machine-readable formats
- **ONC Cures Act EHR interoperability** — USCDI + FHIR APIs + information-blocking prohibition with 8 exceptions
- **Cross-overlay PHI data-flow coordination** — DPIA (GDPR Art 35) + HIPAA Risk Analysis (§164.308) + FDA Cybersecurity Risk Assessment share threat catalog + control framework

#### cell-therapy-supply-chain (pharma + atmp + transport-hazmat)

7 clauses. Vein-to-vein autologous CAR-T + manufacturer-to-patient allogeneic ATMP logistics. Notable provisions:

- **Chain of Identity (COI)** — autologous: same-patient through entire supply chain; allogeneic: donor + lot + recipient across batch-pool boundary; **30-year EU retention** (Annex 2A §11) + **indefinite US** (21 CFR 1271.290 + state law)
- **Chain of Custody (COC)** — documented handoffs across apheresis center → cryopreservation → packaging → transport → manufacturing → finished-product cryo → transport → infusion site → patient; per-handoff identity + condition + temperature continuous-monitoring + custodian acknowledgment
- **Cryogenic UN1977 shipping** — IATA PI 202 dry-shipper LN2 Dewar; 7-14 day vapor-shipper hold time; temperature continuous logging; gap in temperature data triggers product investigation
- **Time-Out-of-Storage (TOS) cumulative budget** — every minute above cryopreservation (≤ -150°C) counts toward CMC-stability-defined max; manufacturing TOS + transport TOS + clinical site TOS cumulative
- **21 CFR 1271 HCT/P** — Subpart A registration + C donor eligibility (RCDA + communicable disease testing + medical record) + D cGTP + F additional non-reproductive requirements
- **Autologous failure-mode escalation** per FDA CAR-T 2024 Guidance — no batch-pool backup; manufacturing failure = patient-specific product loss = retreatment from new apheresis OR clinical bridge
- **IATA Time and Temperature Sensitive Cargo (TTSC) + CEIV Pharma** carrier qualification

#### food-allergen-recall (food-safety + recall-workflow + privacy)

7 clauses. Undeclared allergens are the #1 cause of FDA Class I food recalls in the US. Notable provisions:

- **9 major allergens** per FALCPA (2004) + FASTER Act (2021 — sesame added effective 2023-01-01): milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, sesame
- **21 CFR 7 Class I default** for undeclared allergens — reasonable probability of serious adverse health consequences; triggers media notification + Reportable Food Registry + ≥98% recovery effectiveness expectation
- **FSMA §117.135(c)(2)** food allergen preventive control mandatory + §117.140 verification (visual + analytical with validated method)
- **Reportable Food Registry (RFR)** — 24-hour reporting per FSMA §211
- **Privacy-compliant consumer notification** — GDPR Article 6(1)(c) legal-obligation basis (recall = legal obligation) OR 6(1)(f) legitimate interests (consumer safety overrides privacy); CCPA §1798.145(a)(1) compliance-with-legal-obligation exception; data minimisation per GDPR Article 5

Critical adopter note: FASTER Act did NOT add sesame to GRAS exception list — sesame addition triggered massive industry reformulation OR explicit-declaration adjustment.

#### defense-aerospace-cyber (aerospace + aerospace-defense + defense-cui + cmmc + cmmc-level-2)

7 clauses. DoD aerospace prime contractors + sub-contractors. Notable provisions:

- **DFARS 252.204-7012 / 7019 / 7020 / 7021 stack** — Safeguarding CDI + Cyber Incident Reporting (72h DIBNet) + NIST SP 800-171 DoD Assessment + Basic Assessment Score (PIEE SPRS) + CMMC Requirements flow-down
- **MIL-STD-882E joint safety+cyber hazard tracking** per Tasks 102 + 200 + 300 — cybersecurity hazards explicitly in scope per §4.4; software safety + cyber-physical hazards + cybersecurity-induced safety hazards tracked in single Hazard Tracking System
- **ITAR USML Category VIII** controlled technical data — aircraft + parts + components + production equipment + associated software + technical data; foreign-person access pre-authorisation per 22 CFR §126.18
- **Airworthiness cybersecurity** per DO-326A Airworthiness Security Process Specification + DO-356A Airworthiness Security Methods + DO-355 Information Security for Continuing Airworthiness + ED-202A
- **Supply Chain Risk Management** per NIST SP 800-161 + DFARS 252.239-7018 + 252.204-7016 (FY19 NDAA §889 prohibition on Huawei/ZTE/Hytera/Hikvision/Dahua) + counterfeit-parts AS9120 / AS6081 / GIDEP alerting
- **DoDI 5000.90 platform cyber resilience** — Cybersecurity for Acquisition Programs; Resilience-by-Design + Continuous-Monitoring-Across-Lifecycle + Cyber-Survivability-Endorsement for high-pedigree programs

#### digital-health-multi-region (medical-devices + privacy + regulated-ai)

7 clauses. SaaS digital health operating across multiple jurisdictions. Notable provisions:

- **Per-jurisdiction scope determination** — FDA SaMD (IMDRF N12 + 21 CFR 820 + Pre-Cert if applicable); EU MDR Annex VIII Rule 11 (most SaMD = Class IIa minimum); UK MDR 2002 transitioning to MDR 2024 (UK Future Regulations Roadmap); Swiss MepV with Swissmedic; Canada MDR Class I-IV with Health Canada
- **Data residency + localisation** — GDPR Articles 44-49 + EU-US Data Privacy Framework 2023 + China PIPL (CIIO + significant data + cross-border CAC assessment) + Russia Federal Law 152-FZ + India DPDP Act 2023 sectoral healthcare rules
- **Multi-region consent framework** — GDPR Article 6 + 7 + 9 + HIPAA Authorization §164.508 + CMIA (California) + NY SHIELD Act + Illinois BIPA + PIPEDA + Quebec Law 25 + Ontario PHIPA
- **Multi-region AI/ML SaMD coordination** — EU AI Act Annex III high-risk; FDA AI/ML Action Plan + PCCP + September 2023 Cybersecurity Guidance; Canada AI Bill C-27 AIDA forthcoming; UK AI principles per March 2023 White Paper
- **Multi-stream breach notification** — HIPAA §164.404 / §164.408 / §164.406; GDPR Article 33 SA 72-hour + Article 34 subjects; US state AG breach laws; MDR §92 vigilance for cyber events affecting device safety performance; FDA §524B cyber incident reporting
- **ISO 13485 + MDSAP harmonisation** — Medical Device Single Audit Program covering US FDA + Health Canada + Brazil ANVISA + Australia TGA + Japan PMDA; single ISO 13485 + MDSAP audit reduces multi-region audit burden
- **Per-jurisdiction vigilance reporting** — FDA MDR (21 CFR 803) + EU MDR §92 + EUDAMED + UK MHRA Yellow Card + Health Canada Section 59-60 + Swissmedic Vigilance + PIDR / WHO Uppsala cross-reporting

All 5 cross-overlays reuse parent-overlay templates — no new templates required.

### 24-module ultra composite

```
medical-devices + pharma + combination-product +
connected-medical-device + digital-health-multi-region +
pharma-sterile + hipaa + privacy +
iso-27001 + iso-27001-cloud + iso-27001-privacy + regulated-ai +
iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301 + iso-31000 +
integrated-management-system + soc-2 + soc-2-type-ii +
hitrust-csf + hitrust-r2 + iso-37301
```

= 7 verticals/class + 2 cross-overlays + 1 IMS cross-overlay + 4 ISO 27001 family + 4 health/environment/safety/energy + 3 governance/compliance + 3 attestation (SOC 2 + HITRUST) — realistic shape for a digital-health platform operating multi-region with full compliance posture. Validates `invariant_holds: True`.

## §3 Verification

Per TCE evidence-type discipline:

| Item | Evidence | Status | Verification artifacts |
|---|---|---|---|
| OQ-112 v0.46 additions | example-tested (unchanged) | :tested (unchanged) | hipaa module validates standalone + composites; 15 clauses + 10 templates + 0 orphans per `openqms trace --module hipaa` |
| OQ-113 v0.47 (5 cross-overlays) | example-tested | :tested | All 5 modules validate standalone + 5 key composites validate (one per cross-overlay tested with required vertical combination); 24-module ultra composite validates |

**Honest framing:** all v0.46 + v0.47 additions are `example-tested` — the ceiling for module-coverage / template-existence claims per CLAUDE.md evidence-type rules. No upgrade to `:verified` is meaningfully available (regulatory completeness is not a mathematical property).

**Repo-wide invariant verification (post-v0.47.0):**

- 111 modules
- 828 clauses
- 367 templates
- 683 → 909 clause→template addresses (approximate; depends on count method)
- **0 orphaned clauses**
- **0 orphaned templates**

Per `openqms trace --all`. Enforced by CI gate (added at v0.39.0).

## §4 Spec impact

**Cumulative across v0.46 + v0.47:**

- Spec total: 96 → 97 (+1; OQ-113)
- Status counts (unchanged percentages): 6 `:verified` / 86 `:tested` / 5 `:argued` / 0 `:open`
- Cross-overlay count: 3 → 8 (+5; cross-overlay shape continues to compose cleanly)
- Cross-cutting overlay count: 25 (unchanged)
- Sub-overlay count: 26 (unchanged)
- Class overlay count: 44 (unchanged)
- Vertical count: 7 (unchanged)
- Total modules: 106 → 111 (+5)
- Registry standards: ~126 → ~129 (+3)
- Document templates: 96 → 101 (+5)
- hipaa module: 14→15 clauses, 5→10 templates
- Depth record: 22-module → 24-module ultra composite

## §5 What was deliberately NOT shipped

User-direction-driven scope-limits + remaining forward-work catalogued:

- **More verticals** — paused per repeated user direction (cosmetics / pesticides / nuclear / oil-and-gas / construction / textiles / mining / electrical-equipment)
- **Privacy regional + sector extensions** — UK GDPR specialist / US state-privacy umbrella / PIPEDA / LGPD / APPI / PIPL / COPPA / FERPA / GLBA / ePrivacy — still on bench
- **HIPAA forward work remaining (post-OQ-112 satellites discharge)**:
  - 42 CFR Part 2 (substance use disorder) overlay — narrower scope than HIPAA + additional consent requirements
  - ONC certified EHR technology adoption tracker
- **More cross-overlays** — automotive-supply-chain / clinical-trial-multi-region / banking-resilience / utility-cybersecurity / etc.
- **Engine adopter-features** — jurisdiction filtering / per-clause crosswalk export / module-coverage % reports

## §6 Lessons + observations

1. **YAML linter caught the §164.509 binding regression mid-release.** v0.46 template addresses referenced a clause not yet in the module's clause list; linter (added at v0.40.0) caught at pre-pytest gate; added the §164.509 clause + re-validated clean. Lint-before-validate gate prevents this class of bug from reaching commit. The same failure mode would have caused silent invariant breakage pre-v0.40.

2. **Engine-version drift caught at v0.46.** The v0.44 + v0.45 release commits had all their content shipped EXCEPT the engine version bumps, which silently failed in parallel-batch Edit calls. Caught at v0.46 by manual `grep` during commit prep. Pattern to watch: engine-version bumps in the same parallel block as other edits may fail silently. Mitigation: bump version + read-back-to-confirm before commit, OR isolate version bumps to their own Edit calls.

3. **Cross-overlay shape continues to compose cleanly at 8 instances.** No registration of new template subdirectories needed (cross-overlays reuse parent-overlay templates). Composition primitive (OQ-011) scales linearly with module count; 24-module composite validates in ~1s.

4. **All-PUBLIC standards stack continues to be the dominant adopter benefit.** Registry now ~129 standards; the recent additions (FD&C §524B + FALCPA + FASTER + Cures Act + GDPR + CCPA + HIPAA + HITECH) are all PUBLIC. Of the ~129 total, only ~10-12 are commercial (mostly ISO standards + IMDG + IATA DGR + USP). Open QMS can be adopted at zero standards-licensing cost for most non-ISO scopes.

5. **Cross-overlay is the natural home for intersection-specific regulation.** Each cross-overlay at v0.44 + v0.47 encodes regulatory requirements that emerge specifically at the intersection — combining-existing-overlays-ad-hoc misses the coordination layer. Examples: cell-therapy-supply-chain TOS budget + autologous failure-mode are not in pharma or atmp or transport-hazmat alone but at their intersection.

## §7 Acceptance + close-out

Both v0.46.0 + v0.47.0 shipped + pushed (`3c4461d` + `9b5fe43`). Engine version corrected. Repo-wide invariants holding. 116/116 pytest pass. All 8 bundle baselines clean. YAML linter clean on all 111 modules.

Per user direction "do document hygiene" — this companion + companion_index.md row added.

---

*Companion doc per TCE evidence-discipline; small-arc companion shape (2 releases, scope-balanced — v0.46 small + v0.47 substantial). Update `companion_index.md` with one row.*
