---
name: orca-project-structure
description: Use when initializing or normalizing an ORCA repository around existing source code without moving user files or inventing work history.
---

# Orca Project Structure


## Creation and normalization

Check `AGENTS.md`, source directories, `.orca/`, `GRAPHIFY.md`, Git history and existing docs. For new projects, create minimal `.orca/PROJECT.md`, `.orca/EXEC.md`, roles, phases/tasks/directories, contracts and a documented Graphify status. For existing projects, **propose** non-destructive additions and ask before moves/deletions. Do not create a graph file unless Graphify truly generates it. Do not create fake active tasks, diary entries or completed phases.

## Required semantics

PROJECT is durable scope; EXEC is current ownership; phases are gated milestones; tasks have one owner and criteria; contracts grant permissions; diaries record chronological evidence; summaries promote findings; Git is history; Graphify is derived relationships; AI Memory is optional session continuity. Do not conflate any two. Preserve a single source of truth for each claim.

## Output

Report actual structure created or proposed, files changed, remaining conflicts, tool availability, and the next approved initialization action.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** Created paths verified on disk, conflicts preserved and source files untouched without authority.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.
