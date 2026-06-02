# Role guide — Engineer

**Audience:** software engineers, hardware engineers, design engineers, system engineers, and other technical contributors who commit code, designs, modules, or templates to an Open QMS deployment. Assumes you have completed [`docs/guide/onboarding.md`](onboarding.md).

**What this guide covers:** the day-to-day workflows engineers actually do — making changes, signing commits, requesting review, raising design inputs, responding to CAPA / NCR triggers, and feeding the system without leaving compliance gaps.

---

## Your daily loop

```
git checkout -b firstname/<short-task-name>
<make changes>
git add <specific files — not -A>
git commit -S -m "summary

Signature-Meaning: Authored
"
git push -u origin <branch>
gh pr create
<wait for CI + reviewer>
<merge>
```

The two non-negotiable parts:

- **`git commit -S`** — sign every commit. Configure once: `git config --global commit.gpgsign true`.
- **`Signature-Meaning:` trailer** — Authored, Reviewed, Approved, Witnessed, Acknowledged. Authored is your default. The trailer matters even on small commits because the system reads it as the §11.50 binding (see [`docs/guide/signature-meaning.md`](signature-meaning.md)).

---

## When to use which `Signature-Meaning`

| Trailer | When you use it | Common scenario |
|---|---|---|
| **Authored** | You wrote the change | Default for almost every commit you push |
| **Reviewed** | You reviewed someone else's change | Closing a Document Review or Access Review issue with no substantive change |
| **Approved** | You authorized the change to take effect | Quality Manager approving a controlled-doc PR (rarely you, unless you ARE the QM for this path) |
| **Witnessed** | You observed a process step required to be witnessed | Engineer attesting that a colleague performed a calibration step per SOP |
| **Acknowledged** | You confirm you have read and understood | Closing a Training Completion issue |

If unsure, **Authored** is correct for your own work and **Reviewed** is correct for someone else's. Don't use Approved unless you have approval authority for the path being changed.

---

## What kinds of changes you'll make

### Code or engine changes (under `engine/`)

- Run `pytest engine/tests -q` locally first. CI will fail without 100% pass; better to catch locally.
- If you add a new test, add it to the appropriate `test_*.py` file under `engine/tests/`.
- If you add a dependency, add it to `engine/pyproject.toml` AND regenerate the lockfile: `cd engine && uv lock`. Commit both files together.
- If you change a public API, update the doctring + `BUSINESS/ENGINE_SPEC.md` entry note + flag the change in your PR description.

### Module changes (under `modules/<vertical>/`)

- Run `openqms validate --module <name>` locally before committing.
- Run `python3 scripts/lint-module-yaml.py` locally before committing.
- If you add a clause, also bind it to at least one template via `addresses:` (the zero-orphan invariant will fail CI otherwise).
- If you add a new standard reference, also add a row to `registry/standards.yaml`.
- If you change a clause summary, consider whether the bound templates still satisfy the (new) summary; if not, update the templates in the same PR.

### Template changes (under `templates/<group>/`)

- If you add a new template, ensure at least one module's `module.yaml` references it via `templates: - path: ...` (or accept it ships as standalone per OQ-099 precedent — document this choice in the PR).
- Template frontmatter must include `document_id`, `version`, `effective_date`, `owner`, `status`, and (if relevant) `addresses: [<clause-id>, ...]`.
- Version-increment rules: minor (X.Y.0 → X.Y+1.0) for content change; major (X.0.0 → X+1.0.0) for breaking change to template structure.

### Design input (a NEW thing you want to build)

- Open a [Design Input issue](https://github.com/IridiumSoftware/OpenQMS/issues/new?template=design-input.yml) BEFORE writing code.
- Issue captures: rationale, requirements, success criteria, applicable standards.
- Get Quality Manager / Product Owner sign-off on the issue before opening PRs.
- Link your PRs to the issue via `Closes #NNN` (or `Refs #NNN` if multi-PR).

### Nonconformance (you discovered something broken in a controlled process)

- Open an [NCR issue](https://github.com/IridiumSoftware/OpenQMS/issues/new?template=nonconformance.yml).
- Be specific: which document, which clause, which behavior diverges.
- If you know the fix, open a PR with `Closes #NNN`; otherwise leave triage to Quality Manager.

### CAPA (you discovered a process pattern that needs fixing)

- Open a [CAPA issue](https://github.com/IridiumSoftware/OpenQMS/issues/new?template=capa.yml).
- Be specific about whether it's Corrective (incident already happened), Preventive (incident not yet happened, you spotted the gap), or both.
- See [`docs/guide/capa-lifecycle.md`](capa-lifecycle.md) for the full lifecycle.

### Complaint (an end-user / customer reported a defect)

- Open a [Complaint issue](https://github.com/IridiumSoftware/OpenQMS/issues/new?template=complaint.yml).
- **Do NOT include PHI / PII in the issue body** — the form captures triage metadata only; the identifiable record lives in the PHI-restricted store (see [`docs/guide/complaints.md`](complaints.md)).

---

## When your PR is blocked

| Block | Resolution |
|---|---|
| YAML linter fails | Read the linter output; usually unquoted colon in a template `name:` value (chemicals-arc lesson) |
| pytest fails | Read the failure; if your change broke an existing test, fix your change or update the test with rationale |
| Coverage gate fails (< 100%) | You added a clause without binding a template (or vice versa); fix the orphan |
| Bundle baseline regression | You changed something that affected a baseline; either revert if unintended OR regenerate the baseline: `openqms regenerate --bundle <name> --write-matrix` |
| CODEOWNERS reviewer not assigned | Push triggers automatic CODEOWNERS assignment; if it didn't, manually request review |
| Reviewer asks for change | Make the change, push the additional commit (do NOT force-push or amend — see below) |
| GPG signature invalid | Local git config issue; `git config --global commit.gpgsign true` + `git config --global user.signingkey <KEY-ID>` |

---

## What you should never do

- **Never force-push to `main` or any protected branch.** Force-push is disabled at branch-protection level; this should not be possible, but adopters with weak branch protection might allow it. Don't try.
- **Never `git rebase -i` on commits already pushed to a shared branch.** Rebase rewrites history; signed-commit attribution depends on history being immutable.
- **Never amend a commit after CI has run.** Same reason — `--amend` rewrites SHA, and CI evidence is keyed to SHA.
- **Never commit binary files without rationale + GPG sign-off.** Binaries break the diff-reviewability claim of the audit trail.
- **Never use `git add -A` blindly.** Stage specific files. Accidental commits of `.env`, credentials, large logs, or temp files are real failure modes.
- **Never skip `pre-commit` hooks (`--no-verify`).** The hooks exist to catch regressions before they enter the history.
- **Never copy/paste regulatory standard text into a module or template.** This is the standards-licensing firewall (OQ-070 + OQ-071). Reference clause numbers + summarize in your own words.

---

## Linkage to other Open QMS controls

- **OQ-001** bidirectional traceability invariant — enforced by the engine; your PRs must satisfy it
- **OQ-022** force-push-disabled — your branch-protection-respecting workflow is what makes the immutability claim true
- **OQ-023** GPG-signed commits — your signing key is the §11.100 unique-attribution anchor for everything you commit
- **OQ-060** §11.50 signature meaning — your `Signature-Meaning:` trailers operationalize this
- **OQ-067** zero-orphan trace invariant — your PR cannot land if it adds orphans

---

## Quick references

- [`docs/guide/quickstart.md`](quickstart.md) — engine CLI
- [`docs/guide/gpg-signing.md`](gpg-signing.md) — GPG setup
- [`docs/guide/signature-meaning.md`](signature-meaning.md) — trailer convention
- [`docs/guide/doc-control.md`](doc-control.md) — document frontmatter requirements
- [`docs/guide/document-routing.md`](document-routing.md) — CODEOWNERS + path-to-team mapping
- [`docs/guide/capa-lifecycle.md`](capa-lifecycle.md) — CAPA state machine
- [`docs/guide/traceability.md`](traceability.md) — clause ↔ template trace system
- [`docs/guide/release.md`](release.md) — release tagging + signature requirements
