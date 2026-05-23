# GPG signing enforcement

Required-signed-commits is the strongest mechanism GitHub gives you for binding committer identity to controlled content. This is one piece of the Part 11 §11.70 signature/record-linking story (the *meaning* of the signature is a separate, larger gap — see `regulatory/overview.md`).

`scripts/setup.sh` configures branch protection and required reviews at the **repository** level, but it does **not** enforce commit signing — that decision lives at the **organization** level and requires admin permissions you may not have via the standard `gh` CLI flow. This guide is a runnable checklist.

## What you're enforcing

Three layered checks:

1. **Every commit on `main` is cryptographically signed by its author** (GPG, S/MIME, or SSH-signed). GitHub displays a green "Verified" badge; unsigned commits cannot be merged.
2. **The signing key is registered against a verified GitHub identity** that maps to an HR-attested individual. The Git author is not enough on its own — anyone can set `user.email` to any string.
3. **The branch protection rule for `main` requires verified signatures** so the second mechanism enforces the first at merge time.

Together these turn `git log --show-signature` into an audit-trail with cryptographic identity binding. They do **not** cover signature meaning (see OQ-060 in the spec).

## Checklist

### 1. Pick a signing scheme

GitHub accepts **GPG**, **S/MIME**, and **SSH** signatures. For a QMS context, the practical comparison:

- **GPG.** Mature; broad tooling support; key management is the team's job. Web-of-trust is irrelevant here; you only need GitHub to verify the key.
- **SSH.** Reuses the SSH keys engineers already have. Simpler key management. Requires Git ≥ 2.34 and `git config gpg.format ssh`.
- **S/MIME.** Tied to organizational certificate authority. Rare in software-engineering contexts; usually only chosen when your IT department already runs S/MIME for email.

For most teams, **SSH-signed commits** are the lowest-friction path. The remainder of this guide assumes GPG (more common in regulated-industry literature); commands for SSH are noted inline.

### 2. Generate / register keys per individual

For each contributor, the **individual** generates a key and registers it against their GitHub account. The key is private to the individual; the public key is added to GitHub via `Settings → SSH and GPG keys`.

```bash
# GPG
gpg --full-generate-key  # 4096-bit RSA, no expiry or 1y, real name + GitHub-verified email
gpg --armor --export <key-id>      # copy output, paste into github.com/settings/keys

# SSH
ssh-keygen -t ed25519 -C 'youremail@org.com'
cat ~/.ssh/id_ed25519.pub          # paste into github.com/settings/keys → SSH (Signing Key)
```

Then configure local Git to sign by default:

```bash
# GPG
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# SSH
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

**Identity proofing.** The GitHub account itself must map to an HR-attested individual. Document this mapping (your "user master list" in QMS terms) and update it as personnel change. Without this, the signature binds to a GitHub handle but not to a real person — auditors will flag the gap.

### 3. Enforce at the repository level

In `Settings → Branches → Branch protection rules → main`, enable **"Require signed commits."** With this enabled:

- Unsigned commits cannot be pushed to `main` (push is rejected).
- PR merge buttons are disabled until every commit in the PR is signed.
- The `gh api` equivalent:

```bash
gh api -X PUT "repos/<owner>/<repo>/branches/main/protection/required_signatures"
```

Add this to your `scripts/setup.sh` extension or run it manually after `setup.sh` completes.

### 4. Enforce at the organization level (optional, recommended)

For organizations with multiple QMS repos, set the requirement at the org level so new repos don't slip through. In `Organization → Settings → Repository → Repository defaults`, enable signed-commit requirements. Requires org owner permissions.

`gh` does not currently expose all org-level signing requirements via CLI; the GitHub web UI is the supported path.

### 5. Monitor

Sign-off enforcement is only as good as continuous monitoring. Two recommended habits:

- **CI step that fails on unsigned commits in the PR's range.** Example workflow snippet:

  ```yaml
  - name: Verify all commits in PR are signed
    run: |
      base="${{ github.event.pull_request.base.sha }}"
      head="${{ github.event.pull_request.head.sha }}"
      unsigned=$(git log --pretty='format:%H %G?' "$base..$head" | grep -v ' G$' || true)
      if [ -n "$unsigned" ]; then
        echo "Unsigned commits found:"
        echo "$unsigned"
        exit 1
      fi
  ```

  This is the belt to branch protection's suspenders — useful if signed-commit enforcement is ever accidentally disabled.

- **Periodic audit** (quarterly) of `git log --show-signature origin/main` against your user master list. Any "Good signature from `<unknown>`" or "BAD signature" entries are findings.

## Limitations

- GitHub's "Verified" badge means the commit is signed by a key registered to a GitHub account — it does not certify that the GitHub account belongs to who you think it does. The HR-mapping step (§2) closes that gap procedurally; nothing closes it cryptographically without a PKI rooted in an enterprise CA.
- Web-edits of files through the GitHub UI use GitHub's own signing key, not the editor's. If you allow web edits on `main`, your "every commit is signed by its author" claim has an exception. Recommended posture: disable web editing of controlled paths via branch protection, force changes through the PR + CI flow.
- Commit signing covers content authorship. It does **not** cover the meaning of the signature (approved? reviewed? authorized for release?) — that is 21 CFR Part 11 §11.50, tracked as OQ-060 in the spec and addressed in `regulatory/overview.md`.

## See also

- `docs/regulatory/overview.md` — full gap analysis including §11.50 signature meaning.
- `docs/guide/configuration.md` — CODEOWNERS, branch protection, label setup.
- `scripts/setup.sh` — repository-level configuration (does not include signing enforcement today).
