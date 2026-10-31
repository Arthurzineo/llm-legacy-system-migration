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
