# 21 CFR Part 11 §11.50 — signature meaning

GPG-signed commits cryptographically bind committer identity to content (§11.70 signature/record linking). They do **not** natively encode the **meaning** of the signature — approved? reviewed? authorized? released? — which §11.50 specifically requires the signature manifestation to display:

> §11.50 Signature manifestations.
> (a) Signed electronic records shall contain information associated with the signing that clearly indicates all of the following: (1) The printed name of the signer; (2) The date and time when the signature was executed; and (3) The meaning (such as review, approval, responsibility, or authorship) associated with the signature.

Open QMS bridges the gap with a **commit-trailer convention** plus a parser, audit-trail exporter, and CI gate. The pair (GPG + trailers) satisfies §11.70 (cryptographic identity binding) AND §11.50 (meaning manifestation).

This is the OQ-060 prototype. Production deployment requires the adopting organization to (a) define its controlled vocabulary of signature meanings in an SOP, (b) configure the shipped CI workflow against its controlled-document paths, and (c) maintain the HR-to-GitHub identity mapping that turns `signer_email` into an attested individual (see `gpg-signing.md`).

## The trailer convention

Every commit that constitutes a signature under §11.50 carries a trailer block at the end of the commit message. Three trailers, one required:

```
Approve quality policy v2.1

(body of the commit message — context, references, etc.)

Signature-Meaning: approved
Signature-Role: QA-Lead
Signature-Justification: Reviewed against ISO 13485 §4.2.4 / 21 CFR 820.40 requirements; meets all clauses.

Signed-off-by: Aaron Green <aaron@example.com>
```

| Trailer | Required? | Purpose |
|---|---|---|
| `Signature-Meaning` | **yes** | The meaning per §11.50(a)(3). Adopters define their controlled vocabulary in their signature-handling SOP — common values: `approved`, `reviewed`, `authorized`, `released`, `verified`, `validated`. |
| `Signature-Role` | no, recommended | The role of the signer (e.g. `QA-Lead`, `Engineering-Manager`). Adopters map roles to GitHub identities via CODEOWNERS or a sibling file. |
| `Signature-Justification` | no, recommended for high-risk approvals | Free-form rationale. Useful for audit reconstruction. |

`Signature-Meaning` is the load-bearing trailer. Commits without it are not §11.50 signatures (they may still be valuable engineering commits, but they don't appear in the audit-trail export).

## The verification model

Three layers, each with a different mechanism:

1. **GPG signing** (substrate, OQ-023) — every commit is GPG-signed by an HR-attested identity. Repository-level "Require signed commits" branch protection enforces this. See `gpg-signing.md`.
2. **Trailer parser** (engine) — `openqms signatures verify --commit <sha>` extracts the trailers and verifies the GPG status. CI gate on controlled-path PRs fails any commit lacking `Signature-Meaning`.
3. **Audit trail export** (engine) — `openqms signatures export --since <ref>` walks `git log`, emits Part 11 §11.50-format JSON records for every commit declaring `Signature-Meaning`. Suitable for inspection responses.

## CLI

### Verify a single commit

```bash
openqms signatures verify --commit abc123
openqms signatures verify                    # defaults to HEAD
openqms signatures verify --require-gpg      # fails if commit isn't GPG-verified
```

Exit code: 0 on pass, 1 on missing trailer / not GPG-verified (when `--require-gpg`), 2 on error.

### Export the audit trail

```bash
openqms signatures export --since main~50 --output audit.json
openqms signatures export --path qms-policy --path qms-sops --output audit.json
openqms signatures export --require-gpg --output audit.json   # exits 1 if any record is not GPG-verified
```

Each record carries the §11.50 minimums (printed name, datetime, meaning) plus the role, justification, the §11.70 cryptographic-binding fields (GPG verified, key id), and a pointer to the underlying Git commit.

## CI integration

`.github/workflows/signature-check.yml` ships in OpenQMS and gates PRs touching `qms-policy/` and `qms-sops/`. In the OpenQMS repository itself those paths don't exist, so the workflow is dormant. In adopter forks that populate controlled-document paths, it activates automatically.

The workflow runs `openqms signatures verify --commit <PR-head>` and fails the PR if the head commit lacks `Signature-Meaning`. Adopters can extend the workflow to require GPG verification (`--require-gpg`) once their org-level signed-commits enforcement is in place.

## Limitations

- **The trailer convention is a discipline, not a security boundary.** A determined actor with commit access can write any trailer. The cryptographic identity binding (§11.70) is what makes the signature non-repudiable; the trailer just declares what the signer was attesting to. Audit-trail integrity depends on the combination.
- **HR-to-GitHub identity mapping is procedural.** Open QMS records the Git author email and (when available) the GPG key id. Translating those into an attested individual is the adopter's user-master-list discipline (see `gpg-signing.md` §2).
- **Controlled vocabulary is the adopter's responsibility.** OpenQMS does not enforce that `Signature-Meaning` values come from a fixed list — that would require shipping a one-size-fits-all SOP. Adopters define their vocabulary; future OpenQMS work may add an optional `qms-signatures.yml` schema to validate trailers against an org-defined list.
- **Trailer parsing is lenient.** The engine matches `Signature-*: value` lines anywhere in the message, not strictly in the trailer block per the Git spec. This is robust to common commit-message styles; strict-trailer-block parsing is a future enhancement.
- **Web edits sign as GitHub.** If your branch protection allows web edits of controlled paths, the resulting commits are GPG-signed by GitHub itself, not by the editor. This breaks the §11.70 binding to the editor's identity. Disable web editing of controlled paths via branch protection.

## See also

- `docs/guide/gpg-signing.md` — the §11.70 substrate.
- `docs/regulatory/medical-devices.md` — overall Part 11 gap context.
- `docs/regulatory/overview.md` — full GitHub-as-QMS gap analysis.
