# Connected Medical Device — Open QMS cross-overlay

**Cross-overlay.** Binds across medical-devices + regulated-ai + privacy + iso-27001 + hipaa to encode the regulatory framework for SaMD-with-cloud-backend / connected medical devices.

## Scope

Medical devices with cloud connectivity, telemetry, remote-monitoring, AI/ML inference, OTA firmware updates, clinician dashboards, patient apps. Increasing FDA + EU MDR scrutiny.

## Standards covered

7 clauses across FD&C §524B (cyber-device cybersecurity per Sept 2023 FDA Final Guidance) + EU MDR Annex I §17.2 + MDCG 2019-16 + FDA AI/ML SaMD Action Plan with Predetermined Change Control Plan + Postmarket Cybersecurity Management + NTIA SBOM minimum elements + Cures Act ONC Interoperability + cross-overlay PHI data-flow coordination.

## Composition

Most natural: `medical-devices + regulated-ai + privacy + iso-27001 + hipaa + connected-medical-device`. Add `samd` class overlay for SaMD-specific scope. Add `mdr-class-iii` or `fda-class-iii` for high-risk implantable connected device.

May also compose with `iso-27001-cloud` (cloud infrastructure security) + `iso-27001-privacy` (PIMS) + `hitrust-csf + hitrust-r2` (multi-framework attestation).

## When to use

- SaMD with cloud backend
- Implantable devices with telemetry (CIEDs / CGMs / neurostimulators)
- Diagnostic imaging with AI/ML inference
- Remote-monitoring platforms
- Patient-facing connected device apps
- Hospital-network-connected device fleets

## Forward work

- SBOM lifecycle management template per NTIA minimum elements
- FDA Premarket Cybersecurity submission template (5 required content sections)
- CVD coordinated disclosure policy template
- AI/ML PCCP template (Description of Modifications + Modification Protocol with 5 sub-protocols)
- ONC Cures Act information-blocking exception evaluation worksheet
