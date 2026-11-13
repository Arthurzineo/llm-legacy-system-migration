---
name: orca-setup
description: Run the mandatory Chief-led ORCA setup before project execution; discover actual agents, agree on responsibilities, create scoped contracts, and optionally configure shared project memory.
---

# ORCA Setup — Chief-led Project Initialization

This is an internal skill loaded by the **existing** `superpower-orca`, not a fifth user-facing Superpower. The user may invoke it by asking for "setup orca". It is reusable for non-migration projects. Conversation language may vary; write project artifacts in English.

## Required skills and preconditions

Read `orca-project-entry` first, then `orca-setup`, `orca-project-structure` if initialization is needed, `orca-coordination` and `orca-work-contract` before delegating. Only use documented, version-matched native ORCA runtime commands. Skills and role names are not evidence that an executable worker exists.

## Mandatory setup sequence

1. **Inspect** the actual project root and branch; read `.orca/PROJECT.md`, `.orca/EXEC.md`, active tasks/contracts and `GRAPHIFY.md` if they exist. Classify new, ready, unmanaged, or partially organized. Avoid moving legacy source or rewriting existing history.
2. **Inventory available agents in this session** using actual runtime introspection. Record verified runtime ID, current connectivity, capabilities, read/write/tool restrictions, concurrency limits and possible reviewer skills. An agent mentioned in a historical file does not count.
3. **Present the staffing plan to the user**: Chief-only or Chief + verified workers, whether delegation helps, proposed roles and responsibilities, expected deliverables, conflicts, and independent review availability. Allow Chief-only even if other agents exist. Respect explicit user preferences; do not recruit or configure extra agents without authorization.
4. **Create the minimum authoritative structure** only when approved: `.orca/PROJECT.md`, `.orca/EXEC.md`, `.orca/roles/`, relevant `.orca/phases/<phase>/PHASE.md`, tasks/diaries, and contracts/active/completed. Preserve existing contracts and histories. Never create fictitious tasks or completed work.
5. **Plan work ownership** per task. Record one owner, dependencies, input evidence, allowed edit paths, prohibited resources, required skills/context, test/acceptance gates, worktree, escalation path and reviewer. Mark review independence explicitly.
6. **Chief issues formal contracts only for real delegated workers**, using `.orca/contracts/CONTRACT-TEMPLATE.md` and `orca-work-contract`. Each worker reads required skills and context and sends ORCA/ACCEPT before starting. A worker does not receive broader authority than the Chief or its parent contract. If dispatch is unavailable, report it and use solo mode rather than fabricating messages.
7. **Chief-only fallback:** assign bounded tasks to the Chief sequentially with `execution_mode: solo`; maintain diaries and acceptance evidence. Never claim an independent review, even if the Chief separately plays a reviewer role.
8. **Offer optional project memory setup** (see below); treat a missing or broken integration as a documented nonblocking capability, not a reason to invent MCP results.
9. **Verify Graphify** if configured for this exact project; generated graph state is not authoritative source. Record connectivity and staleness without creating an empty graph file.
10. **Present the completed setup report**: Chief identity; runtime-verified worker roster; chosen execution mode; task/contract ownership; reviewer status; current phase; memory and Graphify states; actions actually performed; and the next authorized Superpower.

## Project memory setup (AI Memory v2.0.1)

Memory integration is optional and must be explicitly accepted. Before applying changes, read `ai-memory-v2` and `docs/integrations/AI-MEMORY-V2.md`.

- **Detect:** `python3 scripts/ai_memory_doctor.py --json`. Verify binary version 2.0.1, service origin and health. A reachable HTTP endpoint is not proof of an operational MCP client.
- **Install, if missing and authorized:** preview `bash scripts/install_ai_memory_v2.sh`; after review, `bash scripts/install_ai_memory_v2.sh --apply` on a supported host. Windows uses the documented pinned-release procedure. Verify the full release bundle and executable.
- **Initialize/service:** follow the pinned upstream instructions for native/Docker/user-service, local-only by default. Server lifecycle and storage must be explicitly planned; installer success alone is not server readiness.
- **Per actual agent:** preview `bash scripts/configure_ai_memory_v2.sh --client <client>`; on explicit approval run the same command with `--apply`. Install MCP and lifecycle hooks separately, skipping hooks when unsupported. Never assume configuring Chief automatically configures subordinates.
- **Verify live behavior:** reload each client; invoke real MCP `memory_status` and a scoped `memory_query`; test hook event capture if supported. Record `VERIFIED`, `MISSING`, `INCOMPATIBLE`, `UNREACHABLE` or `UNKNOWN` for each agent. Without MCP, continue using `.orca/` authoritative state.
- **Security:** never commit tokens, prompts, credentials or raw sensitive datasets; project-scoped memory only. External embedding providers, network exposure, and automatic prompt capture require separate informed approval.

## Setup gate

Do not start a delegated task before the real worker has accepted a valid contract. Do not start Part 1 or Part 2 automatically when the user has only requested ORCA setup. Report unresolved risks and request human approval for high-impact architecture/security/deployment decisions.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** Approved solo/delegated staffing matrix, signed-off permissions, and per-client memory status.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.
