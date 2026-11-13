---
name: orca-work-contract
description: Use when creating, accepting, completing or reviewing an ORCA work contract; supports both a real worker and Chief-only task execution.
---

# Orca Work Contract


## Creation

Start from `.orca/contracts/CONTRACT-TEMPLATE.md`. Include real project/phase/task IDs, current Chief, owner, `execution_mode`, source snapshot and worktree, required skills, required context, scope, forbidden changes, criteria, deliverables and security gates. Confirm the runtime role and available tools before assigning. Prefer no delegation where task isolation is weak.

## Lifecycle

`PROPOSED -> ACCEPTED -> ACTIVE -> DELIVERED -> ACCEPTED_BY_CHIEF -> COMPLETED`; `BLOCKED` and `CANCELLED` require explicit reason, remaining work and preserved evidence. The worker must read the contract and all required skills before acceptance.

## Chief-only behavior

A contract-equivalent task may be recorded with Chief as assignee. Never emit fictional inter-agent message traffic or pretend a second person reviewed. Sequentially perform analyst, implementer and tester roles; for critical changes request explicit human acceptance when independent review is unavailable.

## Record keeping

A work diary records the reason for each source change, evidence, executed commands and outputs, uncertainty and deviations. No agent may overwrite another task's worktree without a new assignment. Chief closes a task only after evidence has been inspected.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** Task-specific edit allowlist, explicit acceptance test outputs, escalation path and independent-review flag.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Scoped edit rights, acceptance criteria, reviewer status and command evidence.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
