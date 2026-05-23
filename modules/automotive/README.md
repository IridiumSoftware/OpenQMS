# Automotive — Open QMS vertical module

Vertical regulatory module for **road-vehicle automotive** (passenger cars, light commercial vehicles, heavy-duty trucks). The second non-medical vertical in Open QMS — built after the aerospace vertical to test whether the platform's composition discipline (OQ-011 compose primitive + OQ-014 registry + OQ-013 validation harness + OQ-015 regenerate) generalizes across substantively different regulated industries.

## Scope

This module covers:

- **QMS substrate** — ISO 9001:2015 + **IATF 16949:2016** (the automotive QMS, built on top of ISO 9001 with automotive-specific additions for process effectiveness, special characteristics, problem solving, and supplier control with Tier-N visibility).
- **Functional safety** — **ISO 26262:2018** (all 12 parts). Concept-phase (Item Definition, HARA, FSC), product development across system / hardware / software (Parts 4 / 5 / 6), supporting processes (Part 8 — config / change / tool qualification), ASIL-oriented analyses (Part 9 — ASIL decomposition, dependent-failure analysis). ASIL A through D.
- **Cybersecurity engineering** — **ISO/SAE 21434:2021**. CSMS at organizational level, project-dependent cybersecurity management, continuous activities (vulnerability + incident response), TARA with CAL assignment.
- **Type-approval cybersecurity regulations** — **UN R155** (CSMS + per-vehicle-type cybersecurity assessment) + **UN R156** (SUMS — software update management system). Mandatory for type approval in UNECE jurisdictions (EU, Japan, Korea, etc.) since July 2022; not mandatory in the US but increasingly flowed down by OEMs to suppliers.
- **Process maturity** — **Automotive SPICE 4.0** (VDA-required for German OEMs; widely adopted by Tier-1 suppliers globally). SWE process group + MAN + SUP.
- **Production approval** — **AIAG PPAP 4th Edition** (Production Part Approval Process — 18-element submission package; the automotive analog of the aerospace AS9102 First Article Inspection).

## Composition with overlays

The automotive module composes cleanly with:

- **`regulated-ai`** — increasingly relevant given modern vehicles' integration of ML-driven functions (ADAS, automated driving, predictive maintenance, in-cabin monitoring). ISO 23894 AI risk management is complementary to both ISO 26262 (functional safety) and ISO/SAE 21434 (cybersecurity) — three distinct risk-management disciplines that interact at the architectural level. Adopters with high-risk-AI scope under the EU AI Act should compose this overlay.
- **`iso-27001`** — organizational information security (orthogonal to product cybersecurity; covers IT systems, source code repositories, customer data, supplier portals). Recommended for any organization in scope of UN R155 since CSMS assessors increasingly expect an enterprise-wide IS posture.

## Composition with class overlays (forward work)

ASIL class overlays (ASIL-A / ASIL-B / ASIL-C / ASIL-D per ISO 26262) and CAL class overlays (CAL 1-4 per ISO/SAE 21434) are intentionally deferred to future overlays, mirroring the medical-devices / aerospace class overlay pattern. Each class overlay encodes the increasing-rigor activities mandated at each level:

- **ASIL-D** requires structural coverage at MC/DC level (Part 6), independent confirmation review with high independence requirements (Part 2 §6), and the most stringent hardware metrics (PMHF / SPFM / LFM per Part 5).
- **ASIL-A** requires statement coverage, recommended (not mandatory) confirmation review, looser hardware metrics.
- **QM (Quality Management)** — only ISO 9001 + IATF 16949 process discipline; no additional FuSa rigor.

## What is intentionally NOT in scope

- **Defense vehicles** — armored ground vehicles (GVSC standards), MIL-STD-882 system safety. Forward work as a separate `automotive-defense` overlay.
- **Off-highway / mobile machinery** — ISO 13849 + ISO 26262 motorcycle adaptation (Part 12). Separate verticals likely.
- **Rail** — EN 50128 / EN 50129. Separate vertical.
- **Aerospace** — see the `aerospace/` module.
- **Recall management** — NHTSA Part 573 in the US, RAPEX in EU. Cross-cutting workflow forward work; intersects with CAPA + management review (already in cross-cutting templates).

## Templates introduced by this module

Five new automotive-specific templates:

- **`templates/product-dhf/item-definition/ITEM-DEFINITION-TEMPLATE.md`** — ISO 26262 Part 3 §5 Item Definition. The first concept-phase deliverable; establishes the boundary of the "item" under FuSa analysis.
- **`templates/product-dhf/hara/HARA-TEMPLATE.md`** — ISO 26262 Part 3 §6 Hazard Analysis and Risk Assessment. Hazardous-event classification per S × E × C → ASIL determination → Safety Goals.
- **`templates/product-dhf/safety-concept/SAFETY-CONCEPT-TEMPLATE.md`** — combined Functional Safety Concept (Part 3 §7) + Technical Safety Concept (Part 4 §6) document. Includes optional Part C for Cybersecurity Concept (ISO/SAE 21434 §9) since the two concepts interact tightly.
- **`templates/product-dhf/tara/TARA-TEMPLATE.md`** — ISO/SAE 21434 §15 Threat Analysis and Risk Assessment. Cyber analog of HARA; drives CAL assignment + Cybersecurity Goals.
- **`templates/product-dhf/ppap/PPAP-TEMPLATE.md`** — AIAG PPAP 4th Ed. 18-element submission with Part Submission Warrant.

Cross-cutting templates already in Open QMS (quality-policy, SOP, audit, management-review, supplier, CAPA, NCR, RMF, verification, software test) cover the QMS surface — automotive QMS is structurally similar to medical-devices and aerospace QMS at the substrate level.

## Standards licensing

Open QMS references the automotive standards by clause number and normative summary only. It does NOT include or redistribute any of the following commercially-published copyrighted works:

- **IATF 16949:2016** — published by IATF; obtain via national member bodies (US: AIAG).
- **ISO 26262:2018** — published by ISO; obtain via national member bodies (US: ANSI; UK: BSI).
- **ISO/SAE 21434:2021** — co-published by ISO + SAE International.
- **Automotive SPICE 4.0** — published by VDA QMC.
- **AIAG PPAP 4th Edition** — published by AIAG.

**UN R155** and **UN R156** are public UNECE regulations and freely available at https://unece.org/transport/vehicle-regulations.

Adopters obtain their own licensed copies of the commercial standards. See repo-root `README.md` "Standards licensing — important" for the broader licensing posture.

## Forward work

- **ASIL class overlays** — ASIL-A through ASIL-D with progressively stringent process requirements per ISO 26262 Parts 2 / 4 / 5 / 6.
- **CAL class overlays** — CAL 1-4 per ISO/SAE 21434.
- **Automotive-defense overlay** — MIL-STD-882, ITAR / EAR procedural discipline.
- **Motorcycle adaptation** — ISO 26262 Part 12 (overlay vs. separate vertical decision pending an adopter motivating the choice).
- **Heavy commercial vehicles + buses** — same standards apply; specific operational situations differ in HARA.
- **NHTSA recall workflow** — Part 573 cross-cutting workflow (touches automotive + future verticals like consumer products / appliances).
