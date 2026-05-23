---
document_id: UEF-XXX
title: "[Product Name] — Usability Engineering File"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Usability / Human Factors Lead, Title]"
status: draft
approved_by: "[QA / Engineering Lead, Title]"
approval_date: YYYY-MM-DD
---

# UEF-XXX: [Product Name] Usability Engineering File

Per IEC 62366-1:2015+A1:2020. The Usability Engineering File (UEF) is the controlled-document compilation of every usability engineering activity for the device, from use-specification through summative evaluation. For SaMD and any device with user-interface aspects affecting safety, the UEF is a required component of the technical file.

## 1. Use specification (IEC 62366-1 §5.1)

- **Intended medical indication:** [as approved]
- **Intended patient population:** [demographics, condition, severity]
- **Intended part of body / type of tissue applied to / interacting with:** [as applicable]
- **Intended user profile:** [clinician role, training, expected experience]
- **Intended use environment:** [hospital ICU / outpatient / home / etc. — relevant operating conditions: lighting, noise, distraction level]
- **Operating principle of the device:** [brief]

## 2. User interface specification (IEC 62366-1 §5.2)

- **Identification of user interface characteristics related to safety:** [list of UI elements / interactions where errors could harm]
- **Identification of hazards and hazardous situations related to UI:** linked to RMF-XXX-001
- **Identification of known or foreseeable use errors:** [list with hazard mapping]

## 3. Identification of primary operating functions (IEC 62366-1 §5.3)

[The subset of UI functions that are critical to use safety. These get focused evaluation in formative and summative phases.]

| Function | Why primary (link to RMF hazard) |
|---|---|

## 4. Hazard-related use scenarios (IEC 62366-1 §5.5)

| Scenario # | User task | Reasonable user error | Hazardous situation (RMF link) | Severity if uncaught |
|---|---|---|---|---|

## 5. UI of primary operating functions (IEC 62366-1 §5.6)

[Detailed specification of the UI elements implementing each primary operating function: visual layout, interaction model, error-prevention design, error-recovery design, feedback mechanisms.]

## 6. Formative evaluation (IEC 62366-1 §5.8)

Iterative usability testing during design to identify use errors and refine the UI. Documented per round:

| Round | Date | Participants | Method | Findings | Design changes |
|---|---|---|---|---|---|

## 7. Summative evaluation (IEC 62366-1 §5.9)

Final validation that the UI is safe and effective for the intended users in the intended use environment.

- **Test plan:** [scope, participants by role, scenarios derived from §4, acceptance criteria]
- **Participants:** [n per user role; recruitment criteria; consent records]
- **Results:** [per scenario: completion rate, use-error rate, time to complete, satisfaction]
- **Disposition of any use errors observed:** linked CAPAs, design changes, or accepted residual risk

## 8. Conclusion

[Statement that the UI is acceptable for the intended use, intended users, and intended environment per the acceptability criteria. Sign-off by usability lead, QA, and clinical.]

## 9. Post-market usability feedback

[Process for collecting and acting on usability-related complaints or adverse events. Feeds back into the formative/summative cycle on the next revision.]

## 10. References

- IEC 62366-1:2015+A1:2020 — Application of usability engineering to medical devices.
- IEC TR 62366-2:2016 — Guidance (informative).
- FDA Guidance: Applying Human Factors and Usability Engineering to Medical Devices (2016).
- Linked artifacts: RMF-XXX-001; VAL-XXX-001; TFI-XXX.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
