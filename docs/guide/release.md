# Release Management

## Release gate workflow

When you push a tag matching `v*` or `release-*`, the `release-gate.yml` workflow runs:

1. **Checks required documents exist** (quality policy, quality manual)
2. **Checks for open blocking issues** (labels: `release-blocker`, `capa-open`, `ncr-open`)
3. **Checks document statuses** (warns on draft documents)
4. **Creates a GitHub Release** if all checks pass

## How to release

**As of v0.55.0, release tags MUST be GPG-signed** (compliance-architecture forward work P7). The unsigned-tag pattern below is retained only as a transitional pattern for adopter forks that have not yet adopted GPG signing.

```bash
# Sign the release tag with GPG (required for project upstream)
git tag -s v1.0.0 -m "v1.0.0 — <release theme>"
git push origin v1.0.0

# The release gate + release-artifact workflows run automatically
# release-artifact.yml verifies the tag signature via `git tag -v`
# and aborts artifact archival on verification failure.
```

### Verifying a release tag locally

Adopters can verify any released tag against the project's published signing key:

```bash
# Fetch the project release-signing public key (one-time)
gpg --keyserver hkps://keys.openpgp.org --recv-keys <PROJECT-RELEASE-KEY-FINGERPRINT>

# Verify a specific tag
git tag -v v1.0.0
# Expected: "Good signature from ..." matching the project's release-signing identity
```

For adopter forks operating in regulated scope: publish your own release-signing public key per the identity-mapping SOP (`templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md`), and replace this section with your fork's verification instructions.

### Release-artifact archival

In addition to the release-gate, the `release-artifact.yml` workflow runs on every `v*` / `release-*` tag push and captures a ZIP containing:

- `trace.json` — repo-wide forward + reverse traceability maps (`openqms trace --all`)
- `coverage.json` — per-module + aggregate clause-coverage metrics (`openqms coverage --all`)
- `signatures.json` — Part 11-style audit trail (`openqms signatures export`)
- `pytest-results.txt` — full pytest log for the release commit
- `lint-output.txt` — YAML linter output
- `module-count.txt` — per-shape module count snapshot
- `tag-signature.txt` — `git tag -v` signature verification output

The artifact is attached to the GitHub Release and retained 90 days by default. Adopters operating in regulated scope should mirror artifacts to org-controlled long-term storage per their records retention schedule (typical pattern: monthly `gh release download` cron job to an encrypted S3 bucket; see `templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md` §2 for the 3-2-1 instantiation).

## Blocking conditions

A release is blocked if:
- Required documents are missing from the repository
- Any issue has the `release-blocker`, `capa-open`, or `ncr-open` label

## Customization

Edit the `required_files` array in `.github/workflows/release-gate.yml` to define which documents must exist for a release.

Edit the `blockingLabels` array to change which issue labels block releases.
