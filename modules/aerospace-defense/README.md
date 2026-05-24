# aerospace-defense — Open QMS class overlay

Class overlay on the **aerospace** vertical. Adds defense-specific requirements: MIL-STD-882E System Safety Program + ITAR + EAR controlled-technology handling.

## Scope

Military aircraft + defense variants of civilian platforms + Department of Defense acquisition programs.

## Standards covered

All PUBLIC license (US federal regs + DoD standards):

- MIL-STD-882E System Safety (May 2012; Change 1 2018)
- ITAR (22 CFR Parts 120-130) — US State Department / DDTC
- EAR (15 CFR Parts 730-774) — US Commerce / BIS

6 clauses:

| Element | Specifics |
|---|---|
| MIL-STD-882E SSPP | System Safety Program Plan across system lifecycle; PHA / SHA / SSHA / HHA / O&SHA; Risk Assessment Codes Severity × Probability |
| MIL-STD-882E hazard tracking | Hazard Tracking Database; risk acceptance authority levels (PM → CAE → Component Head) |
| ITAR USML categorization | Defense articles + services per 21 USML categories; brokering + technical data per §120.10 |
| ITAR Technology Control Plan | DDTC registration; export licensing; **deemed export** of technical data to foreign-persons within US |
| EAR EAR99 vs. CCL | Dual-use items on CCL; ECCN classification; EAR99 = subject-but-not-listed; end-use + end-user + destination drive licensing |
| EAR deemed export | Release of EAR-controlled tech/source to foreign-person within US = deemed export to person's citizenship country |

## Standards-licensing scope-boundary

The cited regulations are PUBLIC, BUT the controlled technical data referenced by ITAR + EAR is heavily restricted. **Open QMS handles the procedural framework only — actual controlled data must be handled per the adopter's separate Technology Control Plan + DCSA / DDTC / BIS oversight.** Do NOT commit ITAR-restricted technical data to a public Git repository.

## Composition

```bash
openqms validate --module aerospace --module aerospace-defense
```

## When to use

DoD acquisition programs; military aircraft manufacturers; defense-platform variants; companies handling USML-listed defense articles or CCL-listed dual-use technologies.

## When NOT to use

Civil-only aerospace manufacturers (aerospace vertical alone). Verify USML/CCL applicability before assuming non-applicability — many seemingly-commercial aerospace components are subject to EAR (commercial aircraft engine components per ECCN 9A991 etc.).

## Standards licensing

PUBLIC license for the regulations; ADOPTER-RESTRICTED for controlled data handled under them.

## Forward work

- CMMC (Cybersecurity Maturity Model Certification) overlay for DoD contractors
- DFARS 252.204-7012 + NIST SP 800-171 controlled-unclassified-information overlay
- FAR / DFARS clause flow-down checklist template
