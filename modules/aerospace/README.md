# Aerospace vertical module

Vertical regulatory module for civil aviation (commercial aerospace). Analogous to the medical-devices vertical: ships a substantive seed covering the core QMS + certification + software + hardware + system + safety standards for commercial aircraft, engines, propellers, and avionics development.

## What this module covers

| Domain | Standards |
|---|---|
| QMS substrate | AS9100D + ISO 9001:2015 |
| Certification | 14 CFR Part 21 (FAA) + EASA Part 21 |
| Software | DO-178C:2011 (RTCA / EUROCAE ED-12C) |
| Hardware | DO-254:2000 (RTCA / EUROCAE ED-80) |
| System development | ARP4754A:2010 (SAE) |
| Safety assessment | ARP4761:1996 (SAE) — FHA + PASA + PSSA + SSA + CCA |
| Production gate | AS9102 Rev C — First Article Inspection |

27 clauses across these standards. Bindings to existing cross-cutting templates (quality-policy, SOP, audit, management-review, supplier templates, CAPA, NCR, risk management, verification, software test) plus 5 new aerospace-specific templates (PSAC, FHA, System Safety Plan, FAI Report, Type Certificate Pack Index).

## Composition with overlays

```bash
# Civil aircraft + AI-driven avionics (Class IIa-equivalent rigor; SaMD-AI analog)
openqms resolve \
  --product AvionicsAI \
  --jurisdiction FAA --jurisdiction EASA \
  --standard "AS9100D" --standard "ISO 9001:2015" \
  --standard "14 CFR Part 21" --standard "EASA Part 21" \
  --standard "DO-178C:2011" --standard "DO-254:2000" \
  --standard "ARP4754A:2010" --standard "ARP4761:1996" \
  --standard "AS9102 Rev C" \
  --standard "NIST AI RMF 1.0" --standard "EU AI Act" \
  --module aerospace --module regulated-ai \
  --output traceability_matrix.json
```

The `regulated-ai` overlay composes naturally with `aerospace`: NIST AI RMF + EU AI Act + ISO 42001 add to the safety-assurance toolkit. ISO 23894 (AI risk management) composes with ARP4761's safety assessment process.

## Forward — class overlays

Design Assurance Levels (DAL A through E per DO-178C / DO-254) are the aerospace analog of medical-device risk classes. Class overlays (`aerospace-dal-a`, `aerospace-dal-b`, `aerospace-dal-c`) are forward work and would add:

- DAL-A: independence requirements per Annex A Tables A-3 through A-7; formal methods consideration; structural coverage including MC/DC; common-mode analysis depth.
- DAL-B: independence for selected verification objectives; structural coverage including decision coverage.
- DAL-C: less stringent verification; structural coverage at statement level.

Most avionics safety-critical software is DAL-A or DAL-B; flight management systems, fly-by-wire, engine control are typically DAL-A.

## Forward — defense scope

This vertical covers civil aviation. Defense aerospace (military aircraft, missiles, satellites for defense) is governed by additional standards:

- **MIL-STD-882** — System Safety (DoD analog of ARP4761)
- **MIL-STD-498** — Software Development and Documentation (older; partially superseded by DO-178C)
- **MIL-HDBK-516** — Airworthiness Certification Criteria
- **ITAR** (International Traffic in Arms Regulations) — defense article controls
- **EAR** (Export Administration Regulations) — dual-use technology controls

A future `aerospace-defense` overlay would compose with `aerospace` to add the defense-specific clauses. The civil + defense duality is analogous to medical-devices' FDA + EU MDR duality.

## Standards licensing

AS9100D, DO-178C, DO-254, ARP4754A, ARP4761, AS9102 are all commercially-published copyrighted works sold by SAE International / RTCA. ISO 9001:2015 is sold by ISO or national member bodies (ANSI in the US, BSI in the UK, etc.). 14 CFR Part 21 and EASA Part 21 are public regulations.

Adopters must obtain their own licensed copies of all commercially-published standards. The Apache-2.0 license on Open QMS does not extend to the standards it references. See repo-root `README.md` "Standards licensing — important" section.

## Naming / numbering notes

- **AS9100D §9.3** vs **AS9100 Rev C §5.6**: Rev D adopted ISO 9001:2015's clause numbering, placing management review under §9.3 (Performance evaluation). The clause ID `AS9100D-5.6` in this manifest is a legacy-friendly alias for the §9.3 content; updating to `AS9100D-9.3` is forward work that would require a registry migration step.
- **DO-178C / ED-12C** and **DO-254 / ED-80**: RTCA (US) and EUROCAE (EU) publish equivalent standards under different document numbers. The registry uses the RTCA "DO-" form as canonical; EUROCAE "ED-" forms are aliases.
- **ARP4754A** and **ARP4761**: both are SAE Aerospace Recommended Practices (ARPs), not standards in the strict sense, but are referenced as the de facto requirements by certification authorities (FAA AC 20-174 explicitly references ARP4754A; EASA CRI references both).
