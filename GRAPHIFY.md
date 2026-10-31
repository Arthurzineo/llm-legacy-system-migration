# Graphify Project Configuration

```yaml
status: pending
project_root: .
graph_path: graphify-out/graph.json
graphify_cli: graphify
mcp_mode: not-configured
last_build: null
last_update: null
last_verified: null
```

Graphify is an optional, derived **project-scoped** index. Agents must verify both the graph path and the client MCP binding before querying it. Source code, verified evidence, `docs/`, and authoritative `.orca/` records remain the source of truth. Do not fabricate a graph file or claim it is ready. A failure to initialize Graphify does not block direct source analysis.

When available, check the actual installed `graphify` syntax, create a graph from the exact project root, and refresh after material structural changes. Do not index secrets, raw production dumps or unrelated repositories. Store graph generation metadata in this file.
