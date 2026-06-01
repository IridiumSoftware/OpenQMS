# Finance vertical — SOX / ICFR

The **8th vertical**: Internal Control over Financial Reporting (ICFR) for US public companies — the *QMS-of-financial-reporting*. It's the control-framework spine; the operational-finance side (resilience, infosec, compliance management) is already covered by cross-cutting overlays that compose with it.

## The spine

| Standard | Role |
|---|---|
| **Sarbanes-Oxley §302** | Quarterly disclosure-controls certification (CEO/CFO) |
| **Sarbanes-Oxley §404(a)** | Annual management ICFR assessment against a suitable framework |
| **Sarbanes-Oxley §404(b)** | External-auditor attestation (accelerated filers) |
| **SEC Exchange Act 13a-15 / 15d-15** | Maintain DC&P + ICFR; disclose material ICFR changes |
| **COSO IC-IF (2013)** | The 5 components / 17 principles ICFR is assessed against |
| **PCAOB AS 2201** | Integrated audit: top-down scoping, RCM, design+operating testing, deficiency evaluation, ITGC |

## Why a vertical (not just an overlay)

ICFR is a **control framework you build, bind to evidence, and test** — `design → operate → test → evaluate deficiencies` — the same shape Open QMS already implements for quality systems. That's why it earns vertical status rather than being folded into the compliance overlays.

## How to use it

```bash
openqms validate --module finance                                            # the ICFR spine alone
openqms validate --module finance --module iso-27001                          # + ITGC / infosec
openqms validate --module finance --module iso-37301-financial-services --module soc-2
openqms validate --module finance --module dora --module nist-csf --module iso-22301   # + resilience
```

The six `templates/qms-finance/` templates walk the §404 lifecycle: **ICFR Risk-Control Matrix** (top-down scoping → accounts × assertions × controls) → **Entity-Level Controls** (COSO 5/17) + **ITGC Register** → **Control Test Plan & Results** (design + operating effectiveness) → **Control Deficiency Log** → **SOX Certification** (§302 + §404).

## Instance traceability (P15)

The **Control Deficiency Log** is authored as a P15 Tier-2 trace table: each deficiency is an `NCR`-kind node that `triggers` a remediation `CAPA`, so `openqms trace-instances` walks deficiency → remediation across the same graph as the rest of your records — no new vocabulary needed.

## Honesty bound (OQ-080)

Ships the ICFR control-framework scaffold + evidence bindings + the testing/deficiency lifecycle. It does **not** assert any specific control actually mitigates its risk, nor substitute for the §404(b) auditor attestation — those remain management judgment + independent audit.

## Forward (not in v1)

EU market (CSRD / ESEF), broker-dealer (SEC + FINRA), AML/BSA, banking prudential (Basel III) — future class/market overlays or sibling verticals.
