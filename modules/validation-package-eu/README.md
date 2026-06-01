# Open QMS — validation-package-eu market overlay

The **EU market dial** for the P2 validation family. Refines the neutral [`validation-package`](../validation-package/) baseline with the EU framing:

- **ISO 13485 §7.5.6 / §7.6** — the device-QMS backbone (computerized systems under MDR Annex IX). *(headline)*
- **EU GMP Annex 11 (Computerised Systems)** — risk management (§1), validation + inventory + traceable URS (§4), data integrity (§5–9, §12), electronic signatures (§14).
- **EU GMP Annex 15 (Qualification and Validation)** — DQ/IQ/OQ/PQ qualification, VMP, change control, revalidation.
- **ICH Q9** — quality risk management as the basis for proportionate effort.

"CSA" is an FDA construct **not used in the EU**; this overlay frames the same risk-based spine in Annex 11/15 + ISO 13485 language. Classic **CSV / robust scripted = the Annex 15 DQ/IQ/OQ/PQ qualification path**.

## Compose it

```
openqms validate --module validation-package --module validation-package-eu
openqms validate --module pharma --module validation-package --module validation-package-eu
# US + EU product — compose both market overlays:
openqms validate --module validation-package --module validation-package-fda --module validation-package-eu
```

EU clauses bind to the baseline templates; Annex 15 qualification adds a `QUALIFICATION-PROTOCOL-TEMPLATE` (DQ/IQ/OQ/PQ), and Annex 11 data-integrity/e-sig bind to the shared `ELECTRONIC-RECORDS-CONTROLS-TEMPLATE` (which now carries both Part 11 and Annex 11 sections). See `BUSINESS/companion_p2_validation_package.md`.
