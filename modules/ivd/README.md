# IVD (In Vitro Diagnostic) overlay

Cross-cutting overlay adding IVD-specific requirements. IVDs in the EU are governed by **IVDR (Regulation 2017/746)**, not MDR. In the US, IVDs are regulated under 21 CFR 820 (QSR) plus the IVD-specific 21 CFR 809 labeling regulation.

Use via:

```bash
openqms resolve --module medical-devices --module ivd ...
```

## What this overlay adds

- **EU IVDR 2017/746** — full IVD-specific regulatory framework: Article 5 (placing on market), Annex I (IVD GSPRs analogous to MDR Annex I), Annex II (technical documentation), Annex IX (conformity assessment with NB involvement for Class B/C/D), Annex XIII (performance evaluation: scientific validity + analytical performance + clinical performance), Article 56 (PSUR cadence: annual for Class D, biennial for Class C, as-needed for A/B).
- **21 CFR 809** — FDA IVD-specific labeling requirements (intended use, indications, specimen type, equipment, performance characteristics).
- **ISO 15189:2022** — medical laboratory quality and competence requirements; composes with ISO 13485 for IVD manufacturers who also operate testing labs (e.g. laboratory-developed test makers).

## Composition with medical-devices

This overlay is shipped as a cross-cutting overlay rather than a complete standalone vertical, for pragmatic reuse of the shared QMS baseline (ISO 13485, 21 CFR 820, Part 11, ISO 14971, IEC 62304). When composed with `medical-devices`:

- **The medical-devices module's MDR-specific clauses (MDR-Art10(9), MDR-AnnexI, MDR-AnnexII, MDR-AnnexIX, MDR-AnnexXIV-A, MDR-AnnexXIV-B) are NOT APPLICABLE to IVD products** in the EU and should be declared NA per the adopter's IVD-scope SOP.
- The IVD module's IVDR-Annex-* clauses replace them functionally.

A future enhancement could ship a `medical-devices-ivd` standalone vertical that excludes MDR clauses entirely; for v0.1, the overlay-with-NA-MDR pattern is what we ship.

## IVD classification (IVDR Annex VIII)

The IVD classification rules (IVDR Annex VIII) differ from MDR — IVDR uses Class A (low individual + low public health risk) through D (high individual + high public health risk). Examples: glucose meters typically Class B; HIV diagnostics Class D; specimen-receptacle products Class A.

Class-specific overlays for IVDR (e.g. `ivdr-class-c`, `ivdr-class-d`) remain forward work analogous to the existing MDR class overlays.

## CLIA scope note

The 42 CFR 493 (CLIA — Clinical Laboratory Improvement Amendments) regulations govern US laboratory operations (especially for laboratory-developed tests / LDTs). CLIA is NOT covered by this overlay — it applies to the laboratory operating the test, not to the IVD product manufacturer. ISO 15189:2022 partially overlaps the CLIA scope and can serve as the QMS substrate for an in-house lab operation.
