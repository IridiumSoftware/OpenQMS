# Verify deployment — adopter-side configuration check

**Audience:** adopter IT/Security + Quality Manager responsible for the GitHub-fork that hosts the QMS. Closes compliance-architecture forward-work P11 at v0.62.0 (OQ-126).

**What this is:** an `openqms` subcommand + shell wrapper that queries your GitHub fork's actual configuration (branch protection + CODEOWNERS + signed commits + required status checks) and compares against a declared `deployment-policy.yaml`. Exits 1 if any policy item isn't satisfied.

**Why this exists:** the reviewer's deepest substantive point — *"the 'immutability' and approval model are not intrinsic properties of the repo. They are deployment controls."* Open QMS can't enforce branch protection in your fork — that's your org's GitHub admin scope. But Open QMS CAN ship the verifier you run to confirm your declared policy is actually in force.

---

## Quick start

1. Copy the example policy:

   ```bash
   cp deployment-policy.example.yaml deployment-policy.yaml
   ```

2. Edit `deployment-policy.yaml`:
   - Set `repo.owner` + `repo.name` to your fork
   - Adjust `required_status_checks.contexts` to your actual CI check names
   - Add `codeowners.required_paths` for any custom paths

3. Authenticate `gh` if you haven't:

   ```bash
   gh auth login
   ```

4. Run the verifier:

   ```bash
   openqms verify-deployment --policy deployment-policy.yaml
   ```

   or via the shell wrapper:

   ```bash
   ./scripts/verify-deployment.sh
   ```

5. Output:

   ```
   verify-deployment: PASS — all declared policy items match actual configuration
   ```

   or

   ```
   verify-deployment: 2 error(s), 0 warning(s)
     [error] branch_protection: require_signed_commits: declared true, actual false (require_signed_commits is the §11.100 unique-attribution anchor)
     [error] codeowners: required path 'modules/' has no CODEOWNERS entry
   ```

---

## What it checks

| Category | What |
|---|---|
| **Branch protection** | `required_approving_review_count` + `require_code_owner_reviews` + `dismiss_stale_reviews` + `enforce_admins` + `required_linear_history` |
| **Signed commits** | `require_signed_commits` enabled (the §11.100 unique-attribution anchor) |
| **Status checks** | `strict: true` + every declared context appears in actual required-checks list |
| **Force push / deletion** | `allow_force_pushes` and `allow_deletions` are NOT enabled (preserves OQ-022 immutability + audit-trail recoverability) |
| **CODEOWNERS** | File exists at `.github/CODEOWNERS` / `CODEOWNERS` / `docs/CODEOWNERS` + every declared required path is covered |

---

## What it does NOT check (intentional gaps)

- **Org-level 2FA enforcement** — requires org-admin API access; left for adopter to verify via GitHub org settings UI
- **GPG key registration per individual** — already covered by the `IDENTITY-MAPPING-SOP-TEMPLATE.md` discipline (OQ-120 P12); the verifier can't tell *which* signatures are valid without per-individual key fingerprints
- **Audit log retention** — varies by GitHub plan (Free has none, Team/Enterprise have configurable retention); flag in your adopter SOP
- **External service integrations** (Slack, JIRA, etc.) — out of QMS scope
- **Repository-secret presence + rotation cadence** — out of substrate scope

---

## CI integration

Adopters can run `openqms verify-deployment` as a periodic CI job (weekly cron). Example workflow snippet:

```yaml
name: Deployment policy verification
on:
  schedule:
    - cron: '0 12 * * 1'   # Mondays at noon UTC
  workflow_dispatch:        # manual trigger

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - uses: astral-sh/setup-uv@v3
        with: { version: '0.11.7' }
      - run: |
          cd engine && uv sync --frozen
          cd engine && uv pip install -e '.'
      - run: openqms verify-deployment --policy deployment-policy.yaml
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

A failing weekly verify is a meaningful signal — it means an admin
changed configuration without going through the policy-update workflow.

---

## Policy schema

See [`deployment-policy.example.yaml`](../../deployment-policy.example.yaml) for the full annotated example. All branch-protection fields are optional; declare only what your adopter policy actually requires. Missing fields mean "no check run."

---

## Linkage to other Open QMS controls

- **OQ-020 + OQ-021** PR + required-reviewers / branch-protection — the controls the verifier checks for
- **OQ-022** force-push-disabled immutability — verifier catches the `allow_force_pushes` regression
- **OQ-023** GPG-signed commits — verifier catches the `require_signed_commits` regression
- **OQ-060** §11.50 signature-meaning — depends on signed commits being enforced
- **OQ-126** this subcommand
- **`templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md`** (OQ-120 P12) — the SOP that runs the per-individual identity-mapping discipline this verifier complements
- **`docs/guide/document-routing.md`** (OQ-121 P3) — CODEOWNERS-based review-chain reference

---

## Adopter checklist

- [ ] Copied + customized `deployment-policy.yaml`
- [ ] Authenticated `gh` CLI with sufficient repo-read scope
- [ ] Ran `openqms verify-deployment --policy deployment-policy.yaml` locally; got PASS
- [ ] Scheduled weekly CI cron to re-verify
- [ ] Failing-verify-handling SOP documented (who fixes; how fast)
