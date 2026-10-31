# AI Memory v2.0.1 Integration — Explicit Opt-In

**Pinned project:** [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) at [v2.0.1](https://github.com/akitaonrails/ai-memory/releases/tag/v2.0.1) (released 2026-09-02). As of 2026-10-31 the upstream latest release is v3.3.0; **do not substitute v3 commands or assume backwards compatibility**. Do not vendor the binary or the full AI Memory source into this repository.

## What the Chief must verify

1. Is the `ai-memory` CLI present and does `ai-memory --version` report **2.0.1**?
2. Is there a running, *authorized* server at the configured origin (default `http://127.0.0.1:49374`)? A HTTP error on GET `/mcp` may indicate the route exists, but is **not** a successful MCP handshake.
3. Does each actual available ORCA agent have an MCP registration for this server? Verify its current config or runtime tools, not just the project's README.
4. Can each agent actually invoke the MCP tool **`memory_status`**? Next, if authorized, use `memory_query` to verify project scoping. A port scan or `curl` is insufficient.
5. Does each agent have lifecycle hooks installed? MCP-only clients may query memory without automatically capturing sessions. `install-mcp` and `install-hooks` are separate upstream commands.
6. Are credentials, prompts and memory pages protected appropriately? AI Memory's default local mode is not encrypted at rest; configure permissions and avoid sending sensitive data to external embeddings providers without approval.

Read-only diagnostic:

```bash
python3 scripts/ai_memory_doctor.py --json
# or authorized remote origin:
python3 scripts/ai_memory_doctor.py --server-url https://memory.example --json
```

## Install: native Linux/macOS (v2.0.1 only)

Review the official [release](https://github.com/akitaonrails/ai-memory/releases/tag/v2.0.1), verify the expected SHA256 artifact, then opt into the conservative script:

```bash
bash scripts/install_ai_memory_v2.sh              # dry-run
bash scripts/install_ai_memory_v2.sh --apply      # explicit change
```

This verifies the official matching release asset and checksum, refuses to overwrite an existing binary and keeps the full binary-and-hooks bundle under `~/.local/lib/ai-memory/v2.0.1` and creates `~/.local/bin/ai-memory` as a symlink, so v2.0.1 can locate sibling lifecycle hooks. It does **not** create/start a service, set up MCP or change agent configuration. The actual installed runtime was not tested in the design environment; if packaging differs, stop and follow the pinned upstream docs rather than weakening checks.

### Native Windows

Download `ai-memory-windows-x86_64.zip` and the matching `.sha256` from the **v2.0.1** release. Verify the ZIP using `Get-FileHash -Algorithm SHA256`, inspect it and place the executable in a user-controlled directory. Follow the pinned upstream [Windows guide](https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/windows.md). Do not run an unreviewed remote installer with `iex`. Native version and runtime support must be checked on the host.

### Docker option

If the official image/tag for v2.0.1 is available in your registry, run it **only after verifying image digest and the upstream v2.0.1 Docker instructions**. Bind to loopback for a local-only service, isolate data volume and set credentials if exposed. Do not use an unpinned `:latest` image. Avoid passing API keys directly on CLI invocations visible in shell history.

## Initialize and start the service

For an existing native installation, consult [v2.0.1 docs/install.md](https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/install.md) for service configuration appropriate to your OS. Example for a Linux package that installed its documented user unit:

```bash
mkdir -p ~/.config/ai-memory ~/.local/share/ai-memory
ai-memory --data-dir ~/.local/share/ai-memory --config ~/.config/ai-memory/config.toml init
# Only if that package supplies the documented user service:
systemctl --user enable --now ai-memory.service
ai-memory status --json
```

Do not assume this systemd unit exists after manually placing a release binary. If absent, use the pinned upstream's verified `ai-memory serve` command and your approved service manager. Do not create a daemon or open network access automatically.

## Connect each agent — inspect first

The upstream v2.0.1 CLI supports `install-mcp` and `install-hooks` for many clients, including Claude Code, Codex, Gemini CLI, Antigravity CLI and Cursor. The repository provides an opt-in wrapper for a small verified client allowlist:

```bash
bash scripts/configure_ai_memory_v2.sh --client claude-code     # dry run
bash scripts/configure_ai_memory_v2.sh --client codex --apply    # authorized change
bash scripts/configure_ai_memory_v2.sh --client gemini-cli --apply
bash scripts/configure_ai_memory_v2.sh --client antigravity-cli --apply
# MCP-only / skip hooks where not supported:
bash scripts/configure_ai_memory_v2.sh --client cursor --no-hooks --apply
```

These commands write **user-level agent configuration**, not repository source, and require explicit permission. For other agents, consult [v2.0.1 MCP installation guide](https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/mcp-install.md) and select the exact supported identifier from its help. Do not invent client flags or copy Claude settings into Gemini/Codex formats. Use `AI_MEMORY_SERVER_URL` and a securely managed `AI_MEMORY_AUTH_TOKEN` for remote servers; avoid putting secrets in scripts or printed output. For Claude Code concurrent sessions the pinned docs describe a `--session-aware` bridge and corresponding `[auto_scope]` setting; use it only if the installed server and client genuinely support that configuration.

**Verification after config:** restart/reload each client, inspect advertised tools and call `memory_status` in that client, run project-scoped `memory_query`, and check that a test prompt creates a hook observation if hooks were enabled. Record `VERIFIED`, `UNKNOWN`, `UNAVAILABLE`, `INCOMPATIBLE` separately per agent. Some clients (including Codex/Antigravity in v2.0.1) need explicit session finalization for complete end-of-session handoff, per the pinned docs.

## Data ownership, security, and fallback

The source code and ORCA records remain authoritative; AI Memory is an optional cross-agent retrieval layer. Use unique workspace/project scopes to prevent cross-project contamination. Never persist secrets, personal records or full production logs. If the server or the MCP bridge cannot be verified, continue with `.orca` diaries, source files and Graphify (when verified), and report the missing memory capability rather than treating it as configured.
