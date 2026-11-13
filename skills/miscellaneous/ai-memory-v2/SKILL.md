---
name: ai-memory-v2
description: Use to inspect and optionally connect Fabian Akita ai-memory v2.0.1 to ORCA agents via MCP and lifecycle hooks with no automatic user-config changes.
---

# Ai Memory V2


## Exact target

Pin the documented integration to `akitaonrails/ai-memory` **v2.0.1** (official GitHub release 2026-09-02). This is intentionally distinct from v3.x. Install from verified release assets only when explicitly authorized. Read `docs/integrations/AI-MEMORY-V2.md` before running commands.

## Session discovery / fail-safe workflow

1. Read-only probe: `python3 scripts/ai_memory_doctor.py --json`; check for `ai-memory`, parse `--version`, configured server URL and `/mcp` reachability. A healthy listening port is not proof of MCP registration in any agent.
2. Find supported clients in the **current session** (Claude Code, Codex, Gemini CLI, Antigravity CLI, etc.) by real installation/config files, not guessed agent names. Verify existing MCP settings and hooks. For the current agent request `memory_status` through the actual MCP tool if advertised. Label results `VERIFIED`, `MISSING`, `INCOMPATIBLE`, `UNREACHABLE` or `UNKNOWN`.
3. Ask whether the user wants **local native install, Docker, a remote server, or no integration**. Explain storage, credentials, retention, network exposure and lifecycle capture. Never auto-install a service, prompt capture, MCP server or agent hooks.
4. On explicit approval, use `scripts/install_ai_memory_v2.sh --apply` only on a supported Linux/macOS platform after checksum review, or the pinned Windows procedure documented in the integration guide. For existing compatible installation, never overwrite.
5. After approval, preview and then selectively execute `scripts/configure_ai_memory_v2.sh --client <supported-client> --apply` (or the upstream documented `install-mcp` and `install-hooks` commands). MCP registration and hooks are distinct steps. Do not expose bearer tokens on command lines, in Git or in ORCA summaries; use supported environment variables and a secure local configuration.
6. Restart/reload the agent when needed; verify the client actually advertises and can call `memory_status`, then test project-scoped `memory_query`; finally verify hook capture where supported. MCP-only clients are not claimed to offer automatic capture. In multiagent mode, repeat checks **per agent**, not only Chief.

## Authority model

AI Memory stores cross-agent episodic handoffs and retrieval notes; `.orca` task/contract files and verified source records remain authoritative. Do not record credentials or sensitive production data. When memory is unavailable, proceed with ORCA diaries and source inspection, reporting degraded continuity.

## Completion

Report the pinned binary version, service health, MCP usability for each client, hook status, storage/security posture and outstanding manual steps. Never call the integration ready solely because `curl` connected.

## Execution-quality contract

- **Selection:** Activate only when this skill's named task is necessary; otherwise explicitly mark NOT_APPLICABLE. Do not load adjacent skills by default.
- **Minimum verifiable result:** CLI version, successful MCP memory_status per client and hook tests; no secret payloads.
- **Evidence status:** Attach exact source revision, tool invocation, exit status, observed output, scope and timestamp for every executed check. Label proposals as PLANNED, missing tools as NOT_RUN, incomplete observations as PARTIAL and observed checks as PASS/FAIL. Never convert a generated document, skill activation or model assertion into test evidence.
- **Failure behavior:** On missing authority, input, tool or acceptance evidence, stop the affected operation, record a blocker and report the narrowest safe next action. Do not claim independent review when run by the Chief alone.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Pinned binary, server, real MCP handshake, hook status per client; no secret storage.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
