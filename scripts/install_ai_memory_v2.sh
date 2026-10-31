#!/usr/bin/env bash
# Verify and optionally install an official pinned AI Memory v2.0.1 binary.
# Supported hosts: Linux x86_64/aarch64 and macOS arm64/x86_64; Windows uses official ZIP manual flow.
set -euo pipefail
APPLY=0
VERSION=2.0.1
for flag in "$@"; do
  case "$flag" in
    --apply) APPLY=1;;
    --help|-h) echo "Usage: $0 [--apply] (default: dry-run)"; exit 0;;
    *) echo "Unknown option: $flag" >&2; exit 2;;
  esac
done
OS="$(uname -s)"; ARCH="$(uname -m)"
case "$OS:$ARCH" in
  Linux:x86_64) PLATFORM=linux-x86_64;;
  Linux:aarch64|Linux:arm64) PLATFORM=linux-aarch64;;
  Darwin:x86_64) PLATFORM=macos-x86_64;;
  Darwin:arm64) PLATFORM=macos-aarch64;;
  *) echo "Unsupported host ($OS/$ARCH); see pinned release assets" >&2; exit 2;;
esac
ASSET="ai-memory-${PLATFORM}.tar.gz"
BASE="https://github.com/akitaonrails/ai-memory/releases/download/v${VERSION}"
DEST="${HOME}/.local/bin/ai-memory"
INSTALL_DIR="${HOME}/.local/lib/ai-memory/v${VERSION}"
if [[ $APPLY -eq 0 ]]; then
  echo "DRY RUN: download ${BASE}/${ASSET} and ${ASSET}.sha256, verify checksum and preserve full binary/hooks bundle in $INSTALL_DIR; symlink $DEST"
  echo "This script does not initialize or start the server or change agent MCP configurations."
  exit 0
fi
for bin in curl tar awk find install mktemp cp ln sed; do command -v "$bin" >/dev/null 2>&1 || { echo "Missing $bin" >&2; exit 1; }; done
if [[ -e "$DEST" || -L "$DEST" || -e "$INSTALL_DIR" ]]; then
  echo "Refusing to replace an existing AI Memory install at $DEST or $INSTALL_DIR" >&2; exit 1
fi
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
curl -fLsS --proto '=https' --tlsv1.2 "$BASE/$ASSET" -o "$TMP/$ASSET"
curl -fLsS --proto '=https' --tlsv1.2 "$BASE/$ASSET.sha256" -o "$TMP/$ASSET.sha256"
EXPECTED="$(awk 'NR==1 {print $1}' "$TMP/$ASSET.sha256")"
if command -v sha256sum >/dev/null 2>&1; then ACTUAL="$(sha256sum "$TMP/$ASSET" | awk '{print $1}')";
elif command -v shasum >/dev/null 2>&1; then ACTUAL="$(shasum -a 256 "$TMP/$ASSET" | awk '{print $1}')";
else echo 'SHA256 tool unavailable' >&2; exit 1; fi
[[ -n "$EXPECTED" && "$ACTUAL" = "$EXPECTED" ]] || { echo 'SHA256 mismatch' >&2; exit 1; }
# Reject obvious path traversal and archive links before unpacking.
tar -tzf "$TMP/$ASSET" > "$TMP/members"
if grep -Eq '(^/|(^|/)\.\.(/|$))' "$TMP/members"; then echo 'Unsafe archive member' >&2; exit 1; fi
if tar -tvzf "$TMP/$ASSET" | awk '{print substr($1,1,1)}' | grep -Eq '[lhcbp]'; then
  echo 'Archive contains links or special nodes; refusing automated extraction' >&2; exit 1
fi
mkdir -p "$TMP/unpacked"
tar --no-same-owner -xzf "$TMP/$ASSET" -C "$TMP/unpacked"
find "$TMP/unpacked" -type f -name ai-memory > "$TMP/binaries"
COUNT="$(wc -l < "$TMP/binaries" | tr -d ' ')"
if [[ "$COUNT" != 1 ]]; then
  echo 'Could not identify a single ai-memory executable; inspect release manually' >&2; exit 1
fi
BINARY="$(cat "$TMP/binaries")"
install -d "$(dirname "$DEST")" "$(dirname "$INSTALL_DIR")"
# Preserve the entire release archive, including sibling lifecycle-hook sources.
# Copying the binary alone prevents the native hook installer from locating its bundle.
cp -a "$TMP/unpacked" "$INSTALL_DIR"
RELATIVE_BINARY="$(printf '%s\n' "$BINARY" | sed "s|^$TMP/unpacked/||")"
ln -s "$INSTALL_DIR/$RELATIVE_BINARY" "$DEST"
"$DEST" --version
printf 'Installed %s with the full upstream release bundle under %s.\n' "$DEST" "$INSTALL_DIR"
printf 'Server startup, MCP registration and lifecycle hooks require separate opt-in setup.\n'
