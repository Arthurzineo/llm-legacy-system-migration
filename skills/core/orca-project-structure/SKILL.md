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
