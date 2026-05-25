# CAPA lifecycle — the state machine

**Audience:** anyone opening, investigating, or closing a CAPA (Corrective and Preventive Action) issue. Quality Manager (owns the lifecycle), engineers + process owners (open + investigate + execute), management (reviews aggregate at Management Review).

**Goal:** demystify the CAPA workflow so non-technical users can navigate it confidently and so regulators see a defensible state machine, not an ad-hoc free-for-all.

---

## What a CAPA is (and is not)

A **CAPA** is the documented investigation, root-cause analysis, corrective action, preventive action, and effectiveness check for a quality-system nonconformance (actual) or potential nonconformance (anticipated). Per ISO 13485 §8.5.2 + 8.5.3 / 21 CFR §820.100.

A CAPA is **NOT**:

- A bug report. Bugs go to the engineering issue tracker. A CAPA addresses *the process gap* that allowed the bug to occur — different scope.
- A complaint. Complaints come from external parties; complaints can *trigger* CAPAs, but the complaint record and the CAPA record are separate.
- A change request. Change requests propose intentional improvements; CAPAs respond to defects. Sometimes a CAPA closes by raising a change request.
- A nonconformance report. NCRs document a single deviation; CAPAs analyze the *systemic cause* of one or more NCRs.

---

## The states

```
   ┌───────────┐
   │   OPEN    │  Triage label: capa-open
   └─────┬─────┘  Created via .github/ISSUE_TEMPLATE/capa.yml
         │
         ▼
   ┌───────────────┐
   │ INVESTIGATION │  Root-cause analysis underway
   └─────┬─────────┘  (5-Why, fishbone, fault-tree, etc.)
         │
         ▼
   ┌──────────────┐
   │  ROOT-CAUSE  │  Root cause identified + documented
   │  IDENTIFIED  │
   └─────┬────────┘
         │
         ▼
   ┌──────────────────┐
   │ ACTION  PLANNED  │  Corrective + Preventive action defined
   └─────┬────────────┘  with owner + deadline
         │
         ▼
   ┌──────────────────┐
   │ ACTION EXECUTED  │  Actions completed; PRs merged;
   └─────┬────────────┘  documents updated; training delivered
         │
         ▼
   ┌────────────────────┐
   │ EFFECTIVENESS CHECK│  Verify the action actually fixed the
   └─────┬──────────────┘  problem; typically 30-90 days later
         │
         ▼
   ┌───────────┐
   │  CLOSED   │  Signature-Meaning: Approved from QM
   └───────────┘  Label removed; archived in git history
```

State transitions are tracked via **issue comments + labels**, not a separate workflow engine. The GitHub issue IS the workflow ground truth.

---

## State-by-state guide

### 1. OPEN

**Trigger:** anyone opens a CAPA issue using [`.github/ISSUE_TEMPLATE/capa.yml`](../../.github/ISSUE_TEMPLATE/capa.yml).

**Required at this state:**
- CAPA Type (Corrective / Preventive / Both)
- Description of the nonconformance or potential nonconformance
- Triage labels (`capa`, `capa-open`)

**What happens next:** Quality Manager (or designate) triages within 1 business day:
- Assigns an owner (the person who will lead the investigation)
- Sets priority label (`P0` immediate / `P1` 7-day / `P2` 30-day / `P3` next-quarter)
- May ask for clarification in comments

### 2. INVESTIGATION

**Trigger:** owner assigned + investigation method picked (5-Why, fishbone, fault-tree, etc.).

**Required at this state:**
- Owner has commented on the issue identifying the chosen method + expected completion date
- Investigation may involve interviews, data review, replication attempts, log analysis

**What happens next:** owner posts findings as the investigation progresses. When the root cause is identified, transition to next state.

**Aging warning:** if an investigation is at this state > 30 days without an update comment, the Quality Manager should ping or reassign.

### 3. ROOT-CAUSE IDENTIFIED

**Trigger:** owner posts a comment titled or labeled "Root cause" with the analysis.

**Required at this state:**
- Root cause documented with supporting evidence (data, logs, witness statements)
- Distinguish *contributing factors* from *primary root cause* — multiple contributing factors are common; primary root cause is the one whose removal would have prevented the nonconformance
- If multiple root causes are plausible, document the elimination reasoning

**What happens next:** plan the action.

### 4. ACTION PLANNED

**Trigger:** owner posts a comment titled "Action plan" with concrete steps.

**Required at this state:**
- For **Corrective Action**: what immediate steps remove the existing nonconformance + prevent recurrence in the affected process / product / batch
- For **Preventive Action**: what systemic changes prevent the nonconformance from occurring elsewhere or in the future
- Each action has: named owner + deadline + acceptance criteria
- If the action requires a document change, link to the planned PR
- If the action requires training, link to the planned Training Completion issue(s)
- If the action requires a registry/spec change, note which entries change

**What happens next:** execute the actions.

### 5. ACTION EXECUTED

**Trigger:** all planned actions completed.

**Required at this state:**
- Every PR referenced in the plan is merged
- Every Training Completion issue is closed
- Every document update is committed + version-bumped
- Action-completion comment on the CAPA issue summarizes what was done with links to the evidence

**What happens next:** wait for the effectiveness check window (typically 30-90 days; longer for low-frequency processes).

### 6. EFFECTIVENESS CHECK

**Trigger:** the effectiveness-check date arrives.

**Required at this state:**
- Owner verifies the original nonconformance has not recurred (process data review, error-rate sampling, audit-of-affected-process)
- If preventive action: owner verifies the prevented-scenario also hasn't manifested in adjacent processes
- Effectiveness comment posted with supporting data
- If effectiveness check **passes** → ready to close
- If effectiveness check **fails** → re-open the lifecycle from INVESTIGATION (the original root cause was wrong or incomplete)

### 7. CLOSED

**Trigger:** Quality Manager (or designate) closes the issue.

**Required at close:**
- Close commit (or merge commit if closure was via a merging PR) carries `Signature-Meaning: Approved` + `Signature-Role: Quality Manager`
- Label `capa-open` removed; label `capa-closed-effective` added
- Final summary comment summarizes the journey

**Closed = archived.** The issue is read-only in practical terms (still editable, but edits are tracked + visible). The issue + its comments + the linked PRs + the linked Training Completions are the CAPA record.

---

## Anti-patterns

### "We took action so we closed it"

**Pattern:** issue jumps from OPEN → ACTION EXECUTED → CLOSED without root-cause documentation or effectiveness check.

**Why it's bad:** the most common audit finding. Auditors will ask "how do you know it worked?" If the answer is "because we did the thing," that's not enough.

**Fix:** every CAPA closure requires evidence of effectiveness check. No exceptions.

### "Close it as duplicate of another open CAPA"

**Pattern:** two CAPAs opened for the same underlying issue; one is closed as a duplicate of the other.

**Why it's bad:** actually fine IF the duplicate issue's close comment links to the remaining open CAPA with `Signature-Meaning: Reviewed`. The duplicate-closure is a record that you considered + de-duped.

**Caveat:** don't close as duplicate if the duplicate has unique investigation findings that the open CAPA lacks. Merge the findings into the open CAPA first.

### "Effectiveness check skipped because action was obviously effective"

**Pattern:** "we updated the SOP so we know it's fixed."

**Why it's bad:** SOP updates don't fix anything unless people read them, understand them, and apply them. "Obviously effective" is the kind of phrase that gets flagged in audit.

**Fix:** wait the effectiveness window. Sample compliance with the updated SOP. Document the result.

### "Investigation completed but root cause is 'human error'"

**Pattern:** root cause field says "human error" or "training issue."

**Why it's bad:** "human error" is a symptom, not a root cause. The root cause is the system condition that allowed the error to occur and not be caught (poor SOP, missing checklist, insufficient training material, no double-check step, ambiguous interface, etc.).

**Fix:** ask "5 whys" until you arrive at a system condition you can change.

### "Preventive Action with no measurable acceptance criterion"

**Pattern:** "we will be more careful in the future."

**Why it's bad:** unmeasurable; cannot pass an effectiveness check.

**Fix:** every action has a "how will we know it's working?" Concrete metric, sampling plan, or audit step.

---

## When CAPAs trigger other workflows

| Triggered by | Workflow |
|---|---|
| Complaint with safety / regulatory implication | Open CAPA from the complaint; link both ways via comment |
| NCR (single deviation) | If NCR reveals a systemic pattern, open a CAPA from the NCR |
| Internal audit finding (major) | Open a CAPA per finding |
| External audit / inspection finding | Open a CAPA per finding; response window typically driven by regulator-specified deadline |
| Restoration test failure | Open a CAPA per `BACKUP-RESTORE-SOP-TEMPLATE.md` §4 step 14 |
| Document review identifies systemic doc-quality issue | Open a CAPA covering the doc-quality pattern (not just the single document) |
| Management review identifies trending issue | Open a CAPA from the management review |

---

## When a CAPA triggers a Change Request

Common pattern: the CAPA's planned action is itself a substantive change to a controlled process or document. In that case, the CAPA opens a Change Request issue + linked PR. Workflow:

1. CAPA in ACTION PLANNED state.
2. Owner opens [Change Request issue](../../.github/ISSUE_TEMPLATE/change-request.yml) describing the change.
3. Change Request gets its own review + approval (typically QM + the functional CODEOWNERS team).
4. PR raised + merged closes the Change Request.
5. CAPA owner updates the CAPA issue: "Action completed via #NNN (Change Request)" + link.
6. CAPA proceeds to EFFECTIVENESS CHECK after the change has been in effect for the check window.

---

## Aggregation at Management Review

Per [`docs/guide/role-quality-manager.md`](role-quality-manager.md), the annual Management Review aggregates CAPA data. The QM typically reports:

- **Open CAPA count** at start + end of review period
- **CAPA close rate** (closures per quarter)
- **Average open-to-close duration** (target: ≤ 90 days for P1; ≤ 30 days for P0)
- **Effectiveness-check-fail rate** (re-opens)
- **CAPAs by root-cause category** (training / process / document / tool / external)
- **Trending root causes** (same category appearing repeatedly suggests a systemic underlying gap)

If aggregate CAPA load is increasing, that's a process-load signal worth raising at Management Review even if individual CAPAs are well-handled.

---

## Linkage to other Open QMS controls

- **OQ-040 + OQ-046** medical-devices module clauses for CAPA (ISO 13485 §8.5.2 + 21 CFR §820.100) — your CAPA workflow satisfies these
- **OQ-119 §3** ISO 13485 expectations — operationalized by this lifecycle
- **OQ-064** management-review aggregation — CAPA data is a primary input
- **`templates/qms-capa/CAPA-FORM-TEMPLATE.md`** — the document-template counterpart to the issue-form (use when the CAPA needs to be exported / printed for external review)
- **Future P15** integration trace network — would let you walk CAPA → upstream trigger (complaint / NCR / audit finding) → downstream effect (linked Change Request / training / doc update) as a single graph; today this is tracked via free-text issue references
