# Open QMS — finance vertical (SOX / ICFR)

The **eighth vertical**: the *QMS-of-financial-reporting* — **Internal Control over Financial Reporting (ICFR)** for US public companies. Spine:

- **Sarbanes-Oxley Act** — §302 (quarterly disclosure-controls certification) + §404(a) (annual management ICFR assessment) + §404(b) (auditor attestation).
- **SEC Exchange Act** — Rules 13a-15 / 15d-15 (maintain DC&P + ICFR; disclose material changes).
- **COSO Internal Control — Integrated Framework (2013)** — the 5 components / 17 principles management assesses ICFR against.
- **PCAOB AS 2201** — the integrated audit: top-down risk-based scoping, risk-control matrix, design + operating-effectiveness testing, deficiency evaluation, ITGC.

## Why a vertical

ICFR is a **control framework you build, bind to evidence, and test** — the same shape Open QMS already implements for quality systems. SOX §404 is literally *design → operate → test controls → evaluate deficiencies*, which maps onto the engine's clause → template → instance-trace model.

## Composes with the existing financial overlays

This is the *control-framework* spine; the operational side is already covered by cross-cutting overlays that compose with it:

```
openqms validate --module finance
openqms validate --module finance --module iso-27001            # ITGC / infosec
openqms validate --module finance --module iso-37301-financial-services --module soc-2
openqms validate --module finance --module dora --module nist-csf   # resilience + cyber
```

## Templates

`templates/qms-finance/` — ICFR Risk-Control Matrix · Entity-Level Controls assessment (COSO 5 components / 17 principles) · ITGC register · Control Test Plan & Results · SOX Certification (§302 + §404) · Control Deficiency Log (authored as a P15 Tier-2 trace table — each deficiency is an `NCR`-kind node that `triggers` a remediation `CAPA`).

## Honesty bound (OQ-080)

Ships the ICFR control-framework scaffold + evidence bindings + the testing/deficiency lifecycle. It does **not** assert that any specific control actually mitigates its risk, nor substitute for the external auditor's §404(b) attestation — those remain management judgment + independent audit.

## Forward overlays (not in v1)

EU market (CSRD / ESEF + EU audit reform), broker-dealer (SEC + FINRA), AML/BSA program, banking prudential (Basel III) — each a future class/market overlay or sibling vertical.
