#!/usr/bin/env bash
# Explicitly opt-in AI Memory v2.0.1 client MCP and hook integration.
set -euo pipefail
APPLY=0
CLIENT=""
WITH_HOOKS=1
usage() { echo "Usage: $0 --client claude-code|codex|gemini-cli|antigravity-cli|cursor [--no-hooks] [--apply]"; }
while (( $# > 0 )); do
  case "$1" in
    --client) [[ $# -gt 1 ]] || { usage; exit 2; }; CLIENT="$2"; shift 2;;
    --no-hooks) WITH_HOOKS=0; shift;;
    --apply) APPLY=1; shift;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown option: $1" >&2; usage; exit 2;;
  esac
done
case "$CLIENT" in
  claude-code|codex|gemini-cli|antigravity-cli|cursor) ;;
  *) echo "Unsupported client. Consult pinned upstream docs for other clients." >&2; exit 2;;
esac
if [[ $APPLY -eq 0 ]]; then
  echo "DRY RUN — no files changed. Intended operations for $CLIENT:"
  echo "  ai-memory install-mcp --client $CLIENT --apply"
  if [[ $WITH_HOOKS -eq 1 ]]; then echo "  ai-memory install-hooks --agent $CLIENT --apply"; fi
  echo "  Check MCP tool memory_status in the client after reload."
  echo "  Credentials, if needed, must be supplied through secure AI_MEMORY_AUTH_TOKEN environment configuration."
  exit 0
fi
command -v ai-memory >/dev/null 2>&1 || { echo "AI Memory binary not found" >&2; exit 1; }
VERSION="$(ai-memory --version 2>&1)"
if [[ ! "$VERSION" =~ (^|[^0-9])2\.0\.1([^0-9]|$) ]]; then
  echo "Expected ai-memory v2.0.1, found: $VERSION" >&2; exit 1
fi
ai-memory install-mcp --client "$CLIENT" --apply
if [[ $WITH_HOOKS -eq 1 ]]; then ai-memory install-hooks --agent "$CLIENT" --apply; fi
cat <<EOF
Client configuration requested for $CLIENT.
Reload the client and call memory_status through its actual MCP tools.
Then verify hook capture for this client (if supported).
EOF
