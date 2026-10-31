# Agent Entry Instructions — LLM - LEGACY SYSTEM MIGRATION

1. Read `README.md`, `.orca/PROJECT.md`, `.orca/EXEC.md`, and `GRAPHIFY.md` before nontrivial work. **Select one of the four `skills/superpowers/` entrypoints** matching the explicit user request (see `docs/skills/SUPERPOWERS.md`). For generic project entry, start with `superpower-orca`, which **must load `orca-setup`** after `orca-project-entry` and before allocating tasks or issuing worker contracts.
2. Determine available workers/reviewers **in the current runtime** by inspecting the real ORCA orchestration interface and available agents. Do not invent agent names, CLI commands, sessions, or capabilities. If only one agent exists, Chief owns and performs all executable tasks; label self-review explicitly.
3. Follow contract, authority, diary, phase, and acceptance rules for solo and delegated tasks. Before any cross-project write, resolve repo root and required permission.
4. For migration work, use the selected `superpower-legacy-discovery`, `superpower-legacy-characterization`, or `superpower-legacy-migration`. These route to the existing specialist skills and optional internal `legacy-migration-orchestrator`. Do not silently skip the optional dynamic stage: present an explicit YES / NO / DEFER choice to the user.
5. Never promote LLM inferences to verified facts without a source revision and evidence. Keep records in `docs/legacy` and `docs/verification`; Graphify and AI Memory are derived indexes.
6. Integrate AI Memory **v2.0.1** via `skills/miscellaneous/ai-memory-v2/SKILL.md` and `docs/integrations/AI-MEMORY-V2.md`. Read-only diagnostics first; actual installation and MCP/hook wiring require approval and a compatible binary. A server responding on a port is not proof a client can use MCP.
7. All repository artifacts are written in English, regardless of user conversation language. Do not translate or change the meaning of externally supplied source code and data without an approved requirement.
8. Never disclose or index secrets, import live databases for experimentation, invoke production services from sandboxed legacy code, or publish this repository without specific authorization.
9. Treat each unverified requirement, inferred diagram edge, or behavior claim as an assumption with explicit verification status.

10. A superpower is not an executable agent runtime. Read each selected specialist SKILL.md, verify actual available tools and permissions, and use native ORCA mechanisms before claiming a delegation or action has run. `scripts/superpower_plan.py` only previews the route.

11. As part of `orca-setup`, propose Chief-only vs delegated work, map verified agent IDs to roles, request approval for optional delegation, allocate worktrees/scopes and issue accepted contracts before implementation. Memory installation and MCP/hook configuration are optional and must be verified per real agent.
12. Optional Uncle Bob Crapper/Dryer/Mutator code is held as pinned submodules. Before executing a tool, run the language-status check, verify compatibility and test baseline, obtain authorization, and preserve real measurements only. See `docs/integrations/OPTIONAL-UNCLE-BOB-TOOLS.md`.

