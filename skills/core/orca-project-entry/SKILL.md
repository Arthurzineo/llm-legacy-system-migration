---
name: orca-project-entry
description: Use at the beginning of every ORCA project session to inspect authoritative project state, discover actual agents, and select single-Chief or delegated execution.
---

# Orca Project Entry


## Inputs and trigger

Use when an agent starts or resumes a project. This skill is generic and works for any software project, not only legacy migration. Input: current repository root and installed ORCA runtime documentation.

## Required steps

1. Verify the exact repository root, current Git branch/worktree and owner of active edits. Inspect `.orca/PROJECT.md`, `.orca/EXEC.md`, `GRAPHIFY.md`, current phase, active tasks and accepted contracts. If absent, classify project as `NEW`, `ORCA READY`, `EXISTING WITHOUT ORCA`, or `PARTIAL/DISORGANIZED` before proposing additive initialization; never move application files without permission.
2. Discover which real agents, tools and runtime orchestration features exist **this session**, by reading version-matched ORCA runtime help or invoking documented introspection interfaces. Do not confuse installed skill files with available agents. Never invent ORCA CLI commands or agent IDs.
3. Choose `solo` when only the current Chief can execute; otherwise choose `delegated` if parallel execution brings a measurable benefit. Recheck after agent availability changes. Verify that a reviewer/security reviewer is genuinely available before assigning that role.
4. If Graphify exists, verify `graphify-out/graph.json` belongs to this project, verify MCP binding and timestamp. If not, mark `PENDING`, `STALE`, `UNAVAILABLE` or `ERROR`; proceed with source reads when possible.
5. Run the read-only AI Memory v2.0.1 checks described in `skills/miscellaneous/ai-memory-v2/SKILL.md` if the project opts in. No installation or client rewiring without permission.
6. Load only relevant task skills, not the entire catalog. Read relevant task/role/contract and just enough recent diary context.

## Output and exit

Report project state, current phase, execution mode, actual available agent capabilities, Graphify status, AI Memory status, assigned task(s), known blockers and next valid action. No historical completed work may be inferred from placeholder templates.
