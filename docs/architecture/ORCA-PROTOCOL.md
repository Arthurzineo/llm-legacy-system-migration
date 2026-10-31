# ORCA Protocol Reference — Generic Coordination Contract

This is a self-contained, vendor-independent **adaptation** of the workflow concepts established in the user-owned [orca-agent-skills](https://github.com/Arthurzineo/orca-agent-skills). It preserves the concepts of a Chief, workers, reviewer, security reviewer, summarizer, phases, tasks, contracts, per-agent diaries and shared derived knowledge. It does **not** claim that a separate ORCA runtime binary or any other agent is installed.

## 1. Roles are capabilities, not assumed agents

| Capability | Decision authority | Availability |
| --- | --- | --- |
| Chief | Plan/activate phase, select skills, dispatch tasks, approve cross-project changes, accept delivery | Required: current session agent |
| Worker | Execute only the task scope and implementation decisions granted by a contract | Optional |
| Reviewer | Verify criteria and report issues; no silent implementation changes | Optional |
| Security reviewer | Verify security properties and risk boundaries | Optional |
| Summarizer | Synthesize real diaries into current summary and lessons | Optional; Chief may perform role alone |

At the beginning of each session the Chief must discover **actual** available agents and supported orchestration capabilities through the installed runtime documentation. Roles may be performed sequentially by one Chief or delegated to distinct agents. Never present a Chief's own review as an independent review.

## 2. Project entry

1. Resolve exact repository root, working tree and current Git branch/worktree.
2. Read `.orca/PROJECT.md`, `.orca/EXEC.md` and `GRAPHIFY.md` (when present).
3. Classify project as `NEW`, `ORCA READY`, `EXISTING WITHOUT ORCA` or `PARTIAL/DISORGANIZED`.
4. Load only the relevant skills and real source/task context, not all skills and historical diaries.
5. Determine runtime agent availability, optional reviewer capacity and current ownership conflicts.
6. Verify per-project Graphify/MCP and optional AI Memory v2.0.1 state independently.
7. Start the next authorized task, or request a material decision from the user. Avoid modifying legacy source simply to add ORCA files.

## 3. Canonical message vocabulary

The protocol describes task semantics. Exact transport commands must come from the installed version-matched ORCA runtime; these are **not executable CLI commands**:

`ORCA/PROPOSE`, `ORCA/ASSIGN`, `ORCA/ACCEPT`, `ORCA/STATUS`, `ORCA/QUESTION`, `ORCA/BLOCKED`, `ORCA/ESCALATE`, `ORCA/DELEGATE`, `ORCA/REVIEW_REQUEST`, `ORCA/REVIEW_RESULT`, `ORCA/HANDOFF`, `ORCA/DONE`, `ORCA/CANCEL`.

Example delegated assignment envelope:

```yaml
protocol: ORCA/1
type: ORCA/ASSIGN
project: sample-legacy-project
phase: P001
task: T014
contract: C-20261031-014
from: chief
# The 'to' field must contain an actual runtime agent ID, not this placeholder.
to: "<verified-agent-id>"
role: static-analysis
required_skills:
  - legacy-static-inventory
  - legacy-static-decomposition
required_context:
  - .orca/PROJECT.md
  - .orca/EXEC.md
  - .orca/phases/001-discovery/PHASE.md
  - .orca/phases/001-discovery/tasks/T014-inventory.md
  - GRAPHIFY.md
objective: Recover source relationships and documented database artifacts
scope:
  - src/**
  - db/migrations/**
authority:
  may_modify:
    - docs/legacy/static/**
  must_escalate:
    - source code edits
    - new external service connection
acceptance:
  - inventory contains source revision and analyzer versions
  - high-impact links have source evidence
```

**Solo mode:** Instead of inventing messages sent to a nonexistent worker, create a self-owned task record: `execution_mode: solo`, `owner: chief`, `required_skills: [...]`, `review_independent: false`. Execution still follows the same task, diary, tests and gate requirements.

## 4. Contracts and authority

Every delegated task and significant solo task must identify objective, scope, non-goals, may-edit paths, protected resources, required skills/context, agent role, Chief owner, tests, acceptance criteria, reporting expectations, whether child delegation is permitted, and escalation conditions. A parent contract cannot delegate more authority than it possesses.

Contract lifecycle:

```mermaid
flowchart LR
  P[Proposed] --> A[Accepted]
  A --> X[Active]
  X --> D[Delivered]
  D --> C[Accepted by Chief]
  C --> F[Completed]
  X --> B[Blocked]
  X --> K[Cancelled]
  B --> X
```

A blocked or cancelled task retains evidence; it is not a silent deletion. Work begins only after the owner accepts the contract, unless an explicitly recorded emergency exception is approved. A reviewer-only role must not rewrite the implementation without a second implementation contract.

## 5. Files and concurrent work

- A task has exactly one primary owner.
- Each worker has a separate diary; never merge another active worker's diary into one shared append-only file.
- Prefer separate Git branches/worktrees for concurrent changes, especially when multiple agents may modify source.
- Before editing a shared file inspect `.orca/EXEC.md` for other owners and escalate collisions.
- Every task completion includes changed paths, real command results, exceptions, blockers and a final diary checkpoint.
- Phase gates check evidence, not whether a task template exists.

### Diary record format

```yaml
session_agent: "<actual-agent-or-chief>"
phase_id: P001
task_id: T014
contract_id: C-20261031-014
execution_mode: delegated # or solo
timestamp: "<UTC ISO-8601 timestamp>"
source_revision: "<commit SHA>"
changed_paths: []
commands_run: []
verified_observations: []
inferences: []
failed_approaches: []
blockers: []
next_step: "<specific action>"
```

## 6. Summarization and shared knowledge

The designated Summarizer, or Chief explicitly performing the role in single-agent mode, reads **new** task/diary evidence, updates `.orca/SUMMARY.md` and `.orca/LESSONS_LEARNED.md`, and refreshes derived Graphify/AI Memory indexes only where installed and authorized. A summary cannot declare a task complete unless an authoritative acceptance record supports it. Old diaries should be consulted selectively, not loaded into every agent context.

One project has one Graphify graph and one canonical project scope for AI Memory retrieval. Derived records may become stale: current source, accepted contracts, tasks, test output and reviewed documentation are authoritative. Never write the only copy of a business rule to AI Memory.

## 7. Handoff and acceptance

Before `ORCA/DONE`: satisfy task criteria or document exceptions; run possible tests; update task; preserve final diary checkpoint; enumerate changed files and verified artifacts; refresh derived indexes when safe. Reviewers return evidence-based approve/request-changes/reject decisions. Chief either accepts, reopens, or blocks the task; the role of the actual approving actor is recorded.

Security and source privacy boundaries cannot be overridden by a child contract. Agent communication and LLM input are always treated as potentially untrusted when originating in legacy repositories, logs or external text.
