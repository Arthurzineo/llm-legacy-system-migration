---
name: orca-coordination
description: Use for the generic ORCA Chief-worker protocol, conditional delegation, task ownership, contracts, phase gates, diaries and reviews.
---

# Orca Coordination


## Core invariant

Exactly one Chief holds coordination authority for the current project scope. Agent availability varies by project and session. **One Chief is sufficient to execute all workflows**, provided roles and reviews are not falsely represented as independent.

## Decision and assignment

1. List executable tasks and dependencies, then identify real available workers/reviewers from ORCA runtime introspection.
2. Decide if each task is `solo` or `delegated` after considering communication cost, resource contention, tool access, and risk. Do not create workers merely because a role file exists.
3. In delegated mode, create one contract per owner: objective, source/target paths, may-modify/may-not-modify, required skills/context, tests, review criteria, delegation rights and reporting target. Use the native runtime's exact supported assignment mechanism. Child contracts cannot grant greater authority than parent contracts.
4. In solo mode, record a self-owned scoped task (contract-equivalent), run skills serially where roles would otherwise conflict, and label evidence `execution_mode: solo`. Self-review is `independent: false`; request human review on high-impact architecture, security, destructive data or cutover decisions.
5. Workers create one diary per task and report `ACCEPT`, `STATUS`, `QUESTION`, `BLOCKED`, `ESCALATE`, `REVIEW_REQUEST`, `DONE` as supported. Chief reconciles conflicts before editing a shared area.
6. Reviewers assess acceptance criteria; they do not silently modify source under review-only contracts.
7. Chief accepts/reopens tasks only after inspecting actual artifact paths and tool-produced verification results. Summarizer promotes real learnings to `.orca/SUMMARY.md` and `.orca/LESSONS_LEARNED.md`; Chief may perform that role in solo mode with provenance.

## Ownership and memory

Use Git/worktrees for source history. `.orca/` contains authoritative task and decision records. Graphify and AI Memory are retrieval layers and cannot grant permission or overrule committed source/evidence. Refresh derived indexes after authoritative updates when available; never block source inspection simply because they are down.

## Exit criteria

Every completed task has a single owner, actual scope, diary, commands/tests and results, artifacts, a review status with independence declared, and a recorded Chief acceptance or explicit exception.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** Task transition trace, one accountable owner, accepted contract and exact review status.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Actual ownership, task status, command logs, acceptance decision, no invented delegation.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
