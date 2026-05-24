# Combination Product — Open QMS cross-overlay

**New module shape — cross-overlay.** Binds ACROSS medical-devices AND pharma verticals to encode combination-product regulatory obligations under FDA 21 CFR Part 4 + EU MDR Article 117.

## Scope

Products that consist of two or more regulated components (drug + device + biologic) physically/chemically combined OR cross-labeled OR co-packaged. Examples: drug-eluting stents; pre-filled auto-injectors; insulin pumps with dose calc software; transdermal patches with reservoir; CAR-T cells with delivery system.

## Standards covered

6 clauses across two regulatory regimes (both PUBLIC):
- 21 CFR Part 4 (US FDA — PMOA + streamlined CGMP + cross-application registration + postmarket coordination + cross-applied QSR provisions)
- EU MDR 2017/745 Article 117 (drug-device with integral device — Notified Body opinion on device part)

## Composition

`medical-devices + pharma + combination-product`. Both verticals required — combination-product makes no sense without both. Often also composes with `medical-devices + samd` (if combination product includes software) + `pharma + pharma-sterile` (if drug component is parenteral) + `privacy` (if connected device + patient data).

## Module shape

This is a **cross-overlay** — a new module shape introduced at v0.44.0:
- Cross-cutting overlays apply to ANY single vertical
- Cross-overlays bind ACROSS specific vertical combinations + coordinate cross-QMS requirements

Distinct from class overlays (within-vertical rigor delta) and sub-overlays (within-cross-cutting tier delta).

## Key adopter decisions

1. **PMOA determination** — drug / device / biologic as primary mode of action; file RFD if uncertain
2. **Streamlined approach** — full Parts 211 + 820 OR drug-led streamlined OR device-led streamlined per §4.4
3. **Article 117 lead** — for EU drug-device combinations, NB selected to issue opinion on device part
4. **Lead adverse-event reporter** — single sponsor reporter coordinating MDR + ADE streams

## When to use

- Drug-device combinations (auto-injectors, prefilled syringes, drug-coated stents, drug-eluting balloons)
- Drug-biologic combinations (cell therapies with carrier matrix)
- Device-biologic combinations (collagen scaffolds with growth factors)
- Cross-labeled separately-packaged products (e.g., infusion pump + drug specifically labeled for that pump)

## When NOT to use

- Pure drug product without integral device → `pharma` alone
- Pure medical device without integral drug/biologic → `medical-devices` alone
- Co-administration without physical/chemical combination + no cross-labeling → separate `pharma` + `medical-devices` QMSes

## Forward work

- FDA Combination Products Inter-Center Consult Request workflow template
- Article 117 NB submission package template
- Streamlined CGMP gap analysis worksheet (drug-led vs device-led decision)
- Cross-application registration submission tracker
- Combination product PSUR + MDR-PSUR coordination workflow
