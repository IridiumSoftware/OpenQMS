# US State Privacy Matrix

**Template for:** state-by-state US privacy law applicability + obligation tracker. Single matrix capturing where the organisation is in scope + what state-specific obligations apply.
**Update cadence:** per state-law effective date + per material business-scope change (new state customer base + revenue thresholds crossed).

---

## 1. Organisation scope (annual review)

| Field | Value |
|---|---|
| Annual gross revenue (most recent FY) | |
| Consumers (residents) processed per state (most recent year — best estimate) | |
| % of revenue derived from sale of personal data | |
| Online consumer advertising service revenue (for FDBR) | |
| US consumer-app-store operation (for FDBR) | |
| Smart speaker / virtual assistant operation (for FDBR) | |
| Children's data processed (under 13 / under 16 / under 18) | |

## 2. Per-state applicability + key obligations

| State (effective date) | Threshold met? | Cure period | UOOM (GPC) mandatory? | Sensitive data scope | Penalty cap | Response deadline | DPA required? |
|---|---|---|---|---|---|---|---|
| **California CCPA/CPRA** (2020-01-01) | ☐ ≥$25M rev / 100k consumers / 50% sale revenue | None (CPPA + AG) | ✓ Mandatory per CPPA §7025 | SPI per §1798.140(ae) | $2.5k-$7.5k (CPRA $7.5k+ for minors) | 45+45 | ✓ Risk Assessment (CPPA regs) — handled by `privacy` overlay |
| **Virginia VCDPA** (2023-01-01) | ☐ ≥100k OR 25k+50% sale | 30 days (PERSISTENT) | ☐ Optional | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child / precise geolocation | $7.5k | 45+45 | ✓ |
| **Colorado CPA** (2023-07-01) | ☐ ≥100k OR 25k+sale revenue | 60 days (sunset 2025) | **✓ Mandatory** | Race / religion / health / sex life / citizenship / genetic+biometric / child + Mental health | $20k per violation | 45+45 | ✓ |
| **Connecticut CTDPA** (2023-07-01) | ☐ ≥100k OR 25k+25% sale | 60 days (sunset 2024) | **✓ Mandatory** | Race / religion / health / sex orient / citizenship / genetic+biometric / child / precise geolocation | $5k | 45+45 | ✓ |
| **Utah UCPA** (2023-12-31) | ☐ ≥$25M rev + 100k OR 25k+50% sale | 30 days (PERSISTENT) | ☐ Optional | Race / religion / health / sex orient / citizenship / genetic+biometric | $7.5k | 45+45 | ☐ Not required |
| **Texas TDPSA** (2024-07-01) | ☐ Not small-business (>$25M; >50% of revenue) OR processing | 30 days (PERSISTENT) | **✓ Mandatory** | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child / precise geolocation | $7.5k | 45+45 | ✓ |
| **Oregon OCPA** (2024-07-01) | ☐ ≥100k OR 25k+25% sale | 30 days (sunset 2026) | **✓ Mandatory** | + non-binary status + transgender status + national origin + status as victim of crime | $7.5k | 45+45 | ✓ |
| **Montana MCDPA** (2024-10-01) | ☐ ≥50k (lower than most) OR 25k+25% sale | 60 days (sunset 2026) | **✓ Mandatory** | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child | $7.5k | 45+45 | ✓ |
| **Iowa ICDPA** (2025-01-01) | ☐ ≥100k OR 25k+50% sale | 90 days (PERSISTENT) | ☐ Optional | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child | $7.5k | 90 days | ☐ Not required |
| **Delaware DPDPA** (2025-01-01) | ☐ ≥35k (lowest) OR 10k+20% sale | 60 days (sunset 2025) | **✓ Mandatory** | + Pregnancy / transgender / non-binary + status / immigration / past adjudicated juvenile delinquency | $10k | 45+45 | ✓ |
| **New Hampshire NHPA** (2025-01-01) | ☐ ≥35k OR 10k+25% sale | 60 days (sunset 2026) | ☐ Optional | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child | $10k | 45+45 | ✓ |
| **New Jersey NJDPA** (2025-01-15) | ☐ ≥100k OR 25k+revenue from sale | 18 months (sunset) | **✓ Mandatory** | Racial/ethnic + religious + health + sex orient + citizenship + genetic+biometric + child + financial info + precise geolocation | $10k-$20k | 45+45 | ✓ |
| **Tennessee TIPA** (2025-07-01) | ☐ ≥$25M revenue + 175k OR 25k+50% sale (high thresholds) | 60 days (PERSISTENT) | ☐ Optional | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child | $7.5k + $15k willful | 60 days | ✓ |
| **Minnesota MCDPA** (2025-07-31) | ☐ ≥100k OR 25k+25% sale | 30 days (sunset 2026) | **✓ Mandatory** | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child / precise geolocation | $7.5k | 45+45 | ✓ |
| **Maryland MODPA** (2025-10-01) — **STRICTER** | ☐ ≥35k OR 10k+20% sale | 60 days (sunset 2027) | **✓ Mandatory** | + Consumer health data (analog to Washington MHMDA broad scope) | **$10k + $25k subsequent** | 45+45 | ✓ **with DATA-MINIMIZATION standard** |
| **Indiana INCDPA** (2026-01-01) | ☐ ≥100k OR 25k+50% sale | 30 days (PERSISTENT) | ☐ Optional | Race / religion / mental+physical / sex orient / citizenship / genetic+biometric / child | $7.5k | 45+45 | ✓ |
| **Florida FDBR** (2024-07-01) — **NARROW** | ☐ >$1B revenue + (>50% rev from ads OR consumer app store + ≥250k apps OR smart speaker with virtual assistant) | 45 days | ☐ Not specified | + Sale of sensitive data specific opt-out | $50k per violation (high) | 45+45 | ✓ |

## 3. Operational programme summary

| Item | Status |
|---|---|
| Privacy Officer / DPO designated | |
| State-by-state privacy notices published | |
| Consumer-rights request channel operational (web form + email + toll-free + mail) | |
| Identity verification per state's standards | |
| Consumer-request log + 45/60/90-day response tracking | |
| UOOM (GPC) honoring implemented + tested per browser | |
| Sale + targeted-advertising opt-out + back-end propagation | |
| Sensitive data consent capture (per Maryland MODPA strict necessity check) | |
| Data Protection Assessments documented for required states | |
| Annual training cadence | |
| DPA contracts with all processors (including sub-processor flow-down) | |
| State AG complaint response procedure | |

## 4. Special-attention scenarios

| Scenario | State-specific impact |
|---|---|
| Maryland MODPA — data minimization scrutiny | Sensitive data processing limited to "strictly necessary"; cannot rely on broad consent; document specific necessity |
| Maryland MODPA — sale of sensitive data | Absolute prohibition; review revenue model + data flow |
| Maryland MODPA — targeted advertising to under-18 | Absolute prohibition; age verification + ad-targeting suppression for known/likely minors |
| Florida FDBR — applicability gating | Verify revenue/operations thresholds; most adopters OUT |
| Oregon OCPA — protected-class expansion | Non-binary / transgender / national origin / crime-victim status as sensitive data — broader than other states |
| Delaware DPDPA — lowest thresholds | Many smaller operators in scope; pregnancy + transgender + immigration + juvenile-delinquency sensitive data scope |
| Texas TDPSA — small-business definition | "Small business" exemption per SBA definition + 50% revenue test; many tech startups OUT |
| New Jersey NJDPA — financial info sensitive | Financial info + precise geolocation explicitly sensitive — different from VCDPA template |
| Maryland MODPA + Washington MHMDA (parallel) | Both apply broad "consumer health data" scope; coordinate compliance posture |

## 5. Cure period management (where applicable)

| Field | Value |
|---|---|
| AG inquiry received? | ☐ Yes — state: , date: |
| Cure period start | |
| Cure period deadline | |
| Cure activities documented + evidence preserved | |
| AG notified of cure | ☐ Yes (date) |
| AG closure received | ☐ Yes (date) |
| Enforcement action despite cure attempt | ☐ Yes — see §6 |

## 6. AG enforcement response

| Field | Value |
|---|---|
| State AG investigation reference | |
| Outside counsel engaged | |
| Internal incident link | |
| Settlement + consent decree status | |
| Civil penalty assessed (per state cap) | |
| Compliance monitor period (if applicable) | |
| Cross-state coordination (multi-state investigation common) | |

## 7. Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Privacy Officer / DPO | | | |
| US privacy counsel | | | |
| Compliance Officer | | | |
| Annual review approver | | | |

---

**Trace evidence.** This matrix addresses USP-scope-thresholds-by-state + USP-sensitive-data-divergence + USP-Universal-Opt-Out-Mechanism-UOOM + USP-cure-period-AG-enforcement + USP-Maryland-MODPA-stricter + USP-FDBR-narrow-scope per `modules/us-state-privacy/module.yaml`. State law citations + effective dates in `registry/standards.yaml` `US State Privacy Laws` entry. Maintain annually + per state-law amendment.
