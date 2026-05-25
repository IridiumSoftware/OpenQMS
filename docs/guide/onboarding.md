# Onboarding — first 30 days on the Open QMS repo

**Audience:** new hires, new contractors, and anyone newly granted commit access to this repository.

**Goal:** by the end of day 30, you can confidently navigate the repo, raise a PR that passes CI, sign your commits, and understand which workflows apply to your role.

If you are evaluating Open QMS rather than working on it daily, start with [`README.md`](../../README.md) and [`docs/compliance-architecture.md`](../compliance-architecture.md) instead.

---

## Day 1 — provisioning + identity

Your IT/Security team will have completed most of this before you start. Confirm each item; if anything is missing, open an issue with the `onboarding` label or message your manager.

- [ ] You have a GitHub account (corporate, not personal) with 2FA enabled
- [ ] You are a member of the GitHub org + at least one team that grants you `triage` or `write` access to this repo
- [ ] You have generated a GPG key per [`docs/guide/gpg-signing.md`](gpg-signing.md) and uploaded the public key to GitHub (Settings → SSH and GPG keys)
- [ ] You have submitted your GPG fingerprint to IT/Security per [`templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md`](../../templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md) §3
- [ ] HR has attested your identity-to-GitHub-account mapping (this is a privacy bar: GitHub's "Verified" badge does not certify you-the-person)
- [ ] You can clone the repo + run `pre-commit` checks locally: `git clone <REPO>` + `cd <REPO>` + `git status`

If any checkbox is unchecked, **stop and resolve it before committing**. The audit trail's attribution claim depends on the chain above being complete.

---

## Day 2-7 — orient yourself

Read these in order. Total reading time ~2 hours.

1. [`README.md`](../../README.md) — what Open QMS is + current scope
2. [`docs/compliance-architecture.md`](../compliance-architecture.md) — how the architecture maps to compliance topics
3. [`docs/guide/quickstart.md`](quickstart.md) — running the engine locally
4. [`docs/guide/doc-control.md`](doc-control.md) — how documents are controlled in GitHub
5. [`docs/guide/gpg-signing.md`](gpg-signing.md) — how commits are signed
6. [`docs/guide/signature-meaning.md`](signature-meaning.md) — the §11.50 trailer convention
7. [`BUSINESS/dashboard.md`](../../BUSINESS/dashboard.md) — current status snapshot

Then read the **role-specific** guide for your role:

- Quality Manager → [`docs/guide/role-quality-manager.md`](role-quality-manager.md)
- Engineer (writes code or modules) → [`docs/guide/role-engineer.md`](role-engineer.md)
- Auditor (internal or external) → [`docs/guide/auditor-walkthrough.md`](auditor-walkthrough.md)

If your role isn't named, ask your manager which guide is closest.

---

## Week 2 — your first signed commit

A safe first commit: add yourself to the appropriate CODEOWNERS team, then make a tiny docs-only change.

1. Pick a typo or small clarification in a doc you read in week 1.
2. Create a feature branch: `git checkout -b firstname/onboarding-typo-fix`.
3. Make the change.
4. Stage + commit with signature + meaning trailer:
   ```bash
   git add <file>
   git commit -S -m "$(cat <<'EOF'
   docs: fix typo in <file>

   Signature-Meaning: Authored
   Signature-Role: Engineer
   EOF
   )"
   ```
5. Push: `git push -u origin firstname/onboarding-typo-fix`.
6. Open a PR. Assign a reviewer per CODEOWNERS.
7. Wait for CI green + reviewer approval + merge.

After merge, verify your commit shows as **Verified** on GitHub: navigate to the commit URL, confirm the green "Verified" badge. If it shows "Unverified", check that your GPG key is uploaded to GitHub and your local git is configured with `git config --global user.signingkey <KEY-ID>` + `git config --global commit.gpgsign true`.

---

## Week 3-4 — your first record-issue

Pick the issue type closest to your role's day-to-day:

- Engineer / Designer → [Design Input](../../.github/ISSUE_TEMPLATE/design-input.yml) form
- Quality / Process owner → [CAPA](../../.github/ISSUE_TEMPLATE/capa.yml) or [Nonconformance](../../.github/ISSUE_TEMPLATE/nonconformance.yml) form
- Document author → [Document Review](../../.github/ISSUE_TEMPLATE/document-review.yml) form (after authoring + on the document's review cadence)
- Trainer / trainee → [Training Completion](../../.github/ISSUE_TEMPLATE/training-completion.yml) form

Open an issue using the form (do not free-write — the form fields are the record structure). Fill it in. Close it (or leave open if it tracks ongoing work). The closing commit is the signature.

If you do not yet have a real record to capture, **do not create a placeholder issue**. Wait until you have substance; running the form is muscle memory you'll build naturally.

---

## Month 1 checklist — completion

- [ ] All Day-1 items confirmed
- [ ] All Day-2-7 reading complete
- [ ] At least 1 signed commit merged with a `Signature-Meaning:` trailer
- [ ] At least 1 record-issue raised using the appropriate form
- [ ] Role-specific guide read end-to-end
- [ ] [`docs/guide/document-routing.md`](document-routing.md) read (so you know which paths route to which reviewers)
- [ ] Know how to verify a commit signature: `git log --show-signature -1 <commit>`
- [ ] Know who to ask when blocked (your CODEOWNERS team for code questions; Quality Manager for process questions; IT/Security for access questions)

When this checklist is complete, file a [Training Completion](../../.github/ISSUE_TEMPLATE/training-completion.yml) issue with `Training topic: "Open QMS onboarding"` and `Completion method: "Self-study + supervisor sign-off"`. Your manager closes the issue with `Signature-Meaning: Approved`.

That issue, closed, is the record that you are onboarded.

---

## When something feels stuck

| Symptom | First thing to try |
|---|---|
| "I don't know what to commit" | Re-read the role-specific guide — it lists day-to-day patterns |
| "CI is failing on my PR" | Read the workflow failure output; the YAML linter + pytest output is usually self-explanatory |
| "My commit shows Unverified" | `git config --global user.signingkey <KEY-ID>` + `git config --global commit.gpgsign true` + `git commit --amend -S --no-edit` |
| "I'm not sure which form to use" | Ask in the team channel; over-specificity is a feature here, not a bug — the right form matters for the record |
| "Someone keeps asking me to add a trailer I don't understand" | Read [`docs/guide/signature-meaning.md`](signature-meaning.md); the trailer is the §11.50 binding |
| "Who reviews this PR?" | Check CODEOWNERS for the touched path; see [`docs/guide/document-routing.md`](document-routing.md) |
