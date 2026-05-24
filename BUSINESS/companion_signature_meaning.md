# Companion — Part 11 §11.50 signature-meaning prototype (v0.7.0)

**Date:** 2026-05-23
**Public commit:** `0b06381` (`3cfec2c..0b06381`)
**Spec delta:** OQ-060 `:open → :tested`.

## §1 Computational basis

GPG-signed commits satisfy 21 CFR Part 11 §11.70 (cryptographic identity binding to content). §11.50 separately requires the signature to display its **meaning** (approved / reviewed / authorized / released / etc.) — GPG alone doesn't encode this. The v0.7.0 prototype bridges the gap with a controlled-vocabulary commit-trailer convention plus parser, audit-trail exporter, CLI, dormant CI gate, and comprehensive guide.

**Files new:**

- `engine/openqms/signatures.py`
  - `SignatureTrailer` frozen dataclass: `meaning`, `role`, `justification`, `signer_name`, `signer_email`, `signed_at`, `commit_sha`, `gpg_verified`, `gpg_signer_key_id`.
  - `parse_signature_trailers(message: str) -> dict[str, str]` — lenient regex extraction of `Signature-*:` lines from anywhere in the commit message body. Strict trailer-block parsing per the Git spec is overkill for this prototype; in practice adopters write the trailers in the canonical block at the bottom of the message.
  - `signature_from_commit_data()` — builds a `SignatureTrailer` from commit metadata; returns `None` if no `Signature-Meaning` declared. Decodes all 9 `git log %G?` GPG status codes; only `G` (good) and `U` (good/unknown-validity) set `gpg_verified=True`.
  - `extract_signatures_from_repo(repo_root, since_ref=None, paths=None)` — walks `git log` with NUL-separated `%x00` fields + `0x1e` record separator, parses each commit, returns the list of signatures matching `Signature-Meaning`.
  - `export_audit_trail(signatures)` — emits Part 11 §11.50-format JSON records: name, email, datetime, meaning, role, justification, git_commit pointer, GPG verification state with key id.

- `engine/openqms/cli.py` — new `openqms signatures verify|export` subcommand.
  - `verify --commit <sha>` (default HEAD) — checks the commit has the required trailer; `--require-gpg` upgrades unverified signatures to errors.
  - `export --since <ref> --path <p>… --output <path>` — emits the JSON audit trail; `--require-gpg` fails on any unverified record.

- `docs/guide/signature-meaning.md` — verbatim §11.50 text; why GPG alone is necessary but not sufficient; trailer convention with examples (`Signature-Meaning:` required, `Signature-Role:` + `Signature-Justification:` optional); CLI surface; CI configuration; honest limitations (trailer is discipline not security boundary; HR-to-identity mapping is procedural; controlled vocabulary is adopter's responsibility; parsing is lenient; web edits sign as GitHub).

- `.github/workflows/signature-check.yml` — gates PRs touching controlled-document paths (`qms-policy/`, `qms-sops/`, `qms-forms/`, `qms-training/`, `product-*/`). Runs `openqms signatures verify` against every commit in the PR's range. Dormant in OpenQMS itself (no controlled documents at those paths today); active in adopter forks. `--require-gpg` is commented out — adopters uncomment after their org has GPG enforcement in place per `gpg-signing.md`.

- `engine/tests/test_signatures.py` — 23 tests:
  - Parser (4): basic, empty body, justification field, ignores non-Signature trailers.
  - `signature_from_commit_data` + parametric over 9 GPG codes (2 + 9 = 11).
  - `export_audit_trail` (2): full Part 11 fields, missing optional fields.
  - tmp-git-repo integration (2): mix of signed/unsigned, path filter respected.
  - CLI subprocess (4): export, verify pass, verify fail on missing trailer, `--require-gpg` fail on unsigned.

**Files modified:**

- `engine/openqms/{__init__,pyproject.toml}` — 0.6.0 → 0.7.0.
- `.github/workflows/engine-tests.yml` — adds `openqms signatures export` as a smoke check.
- `engine/README.md` + top-level `README.md` — document the signatures subcommand, the trailer convention, the §11.70 vs §11.50 gap.

**Test environment:** Python 3.14.4 on Darwin; tmp-repo tests use `GIT_AUTHOR_*` env vars + `commit.gpgsign=false` so they work without keyrings. Test count: 74 → 97 (+23).

## §2 Results

- **Trailer convention defined.** `Signature-Meaning: <value>` is the required §11.50 manifestation; `Signature-Role:` and `Signature-Justification:` are recommended. Adopters define the controlled vocabulary in their signature-handling SOP.
- **Engine implements the round-trip.** Parser extracts trailers; constructor builds typed records with GPG verification state; extractor walks a real git log; exporter emits Part 11-format JSON. End-to-end verified via tmp-repo subprocess tests.
- **CI gate ships dormant.** OpenQMS itself has no documents at the controlled paths, so the workflow is no-op in this repo. In an adopter fork that populates `qms-policy/` etc., the workflow activates automatically.
- **Bridges the §11.70 / §11.50 gap.** GPG-signing (OQ-023, v0.2.2) gives §11.70; trailers (OQ-060, v0.7.0) give §11.50. The pair satisfies both.

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-060 | Part 11 §11.50 signature-meaning prototype shipped | example-tested | 23 tests in `test_signatures.py`: parser handles standard cases + ignores non-Signature trailers; GPG status decoder parametric over all 9 codes; export produces full Part 11 fields; tmp-repo integration tests assert end-to-end extraction; CLI subprocess tests exercise the full surface. |

## §4 Spec impact

| S-ID | Before | After | Evidence type after |
|---|---|---|---|
| OQ-060 | `:open` | `:tested` | example-tested |

Status counts at end of v0.7.0: 29 `:tested` / 15 `:argued` / 2 `:open` (total 46).

**Honest scope notes for future iteration:**

- **Trailer parsing is lenient.** Matches `Signature-*:` lines anywhere in the body, not strictly in the trailer block. Strict-trailer-block parsing per `git interpret-trailers --parse` is a future enhancement.
- **Controlled vocabulary is adopter's.** No `qms-signatures.yml` schema yet to validate `Signature-Meaning` values against an org-defined list. Future enhancement.
- **HR-to-GitHub identity mapping is procedural.** Open QMS records the Git author email and GPG key ID; mapping to an attested individual is the adopter's user-master-list discipline (see OQ-023 / `gpg-signing.md` §2).
- **Web edits sign as GitHub.** If adopter allows web edits on controlled paths, the resulting commits are GPG-signed by GitHub, not the editor. Breaks §11.70 binding to the editor's identity. Documented in the guide; mitigation is to disable web editing via branch protection.

This is the cleanest first-place to test the OpenQMS × Open Honest Foundation collaboration hypothesis (Honest Framework's decision-table / single-writer discipline applied to compliance artifacts rather than runtime code). The OQ-060 prototype is small, formally specifiable, and the absence of a good solution is what makes most regulated-industry teams reach for proprietary eQMS platforms.
