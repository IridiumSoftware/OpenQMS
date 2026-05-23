---
document_id: STP-XXX-001
title: "[Software Item Name] — Software Test Protocol"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Test Lead, Title]"
status: draft
approved_by: "[Software / QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# STP-XXX-001: [Software Item Name] Software Test Protocol

Per IEC 62304 §5.5 (unit verification), §5.6 (integration testing), §5.7 (system testing).

## 1. Purpose and scope

[State which software item and which test phases this protocol covers. Reference the SRS and SAD that define the requirements and architecture being exercised.]

- **Software item:** [name + version]
- **Software safety class:** [A / B / C]
- **Test phases covered:** [Unit / Integration / System / Regression — check applicable]
- **Linked SRS:** SRS-XXX-001
- **Linked SAD:** SAD-XXX-001

## 2. Test strategy

- **Unit testing:** [tooling, coverage criteria, sample-execution methodology. For Class B/C software per IEC 62304 §5.5.5, document the criteria for accepting unit test results.]
- **Integration testing:** [scope of integration — which software items / SOUP items are exercised together. Per IEC 62304 §5.6.3, documents the integration test pass/fail criteria.]
- **System testing:** [end-to-end against the SRS. Per §5.7.3, every functional and non-functional requirement maps to ≥1 system test case.]
- **Regression strategy:** [how previously-passing tests are re-run on change.]

## 3. Test environment

- **Hardware-in-the-loop or simulator:** [bench setup, calibrated instruments, simulated patient signals.]
- **Software dependencies:** [OS version, runtime, SOUP versions per SOUP-XXX-001.]
- **Test data:** [datasets, signal corpora, simulated patient profiles — controlled per the org's record-retention SOP.]

## 4. Per-requirement test cases

| Test ID | Phase | Requirement (SRS) | Preconditions | Steps | Expected result | Acceptance criterion | Result | Pass / Fail |
|---|---|---|---|---|---|---|---|---|
| TC-001 | System | FR-001 (battery %) | Battery at known charge X | Power on; navigate to status screen; record displayed % | % matches X ± 2% | ±2% accuracy | [actual] | [Pass/Fail] |
| TC-012 | System | FR-002 (thermal shutoff) | Battery heated to 60.5°C in test chamber | Operate device; observe behavior within 1 s | Device halts; logs thermal event; visual alarm | Halt within 1s; event logged | [actual] | [Pass/Fail] |

## 5. Test execution log

| Date | Tester | Build under test | Test cases run | Results summary |
|---|---|---|---|---|
| YYYY-MM-DD | [name] | [SW version + HW rev] | TC-001..TC-100 | [pass count / fail count] |

## 6. Defects and deviations

[Each failed test gets a problem report — issue ID, severity, root cause, fix evidence (linked PR), re-test result. Aligns with IEC 62304 §9.]

## 7. Conclusion

[Statement that every in-scope requirement has at least one passing test case OR documented disposition for failures. Sign-off by test lead and quality.]

## 8. References

- IEC 62304:2006+A1:2015 §5.5, §5.6, §5.7, §9.
- 21 CFR 820.30(f) — Design verification (software portion).
- Linked artifacts: SRS-XXX-001; SAD-XXX-001; SOUP-XXX-001; VP-XXX-001.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
