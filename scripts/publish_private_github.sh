#!/usr/bin/env bash
# Publish the reviewed local Git history as a PRIVATE GitHub repository.
# Requires the user to run this script locally with Git and GitHub CLI authenticated.
set -euo pipefail

OWNER="Arthurzineo"
REPOSITORY="llm-legacy-system-migration"
FULL_NAME="${OWNER}/${REPOSITORY}"
FEATURE_BRANCH="feat/orca-core-migration-skills"
PROJECT_URL="https://github.com/${FULL_NAME}"

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
for command_name in git gh; do
  command -v "$command_name" >/dev/null 2>&1 || fail "Missing command: $command_name"
done

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || fail 'Run inside the project Git repository'
cd "$ROOT"

git rev-parse --verify refs/heads/main >/dev/null 2>&1 || fail 'Local main branch not found'
git rev-parse --verify "refs/heads/$FEATURE_BRANCH" >/dev/null 2>&1 || fail "Local feature branch not found: $FEATURE_BRANCH"
[ -z "$(git status --porcelain)" ] || fail 'Uncommitted files detected; commit or stash them before publishing'
gh auth status >/dev/null 2>&1 || fail 'Run gh auth login before publishing'

if gh repo view "$FULL_NAME" >/dev/null 2>&1; then
  visibility="$(gh repo view "$FULL_NAME" --json visibility --jq '.visibility')"
  [ "$visibility" = 'PRIVATE' ] || fail "Existing repository is not private ($visibility). No files were pushed."
  printf 'Using existing PRIVATE repository: %s\n' "$PROJECT_URL"
else
  printf 'Creating PRIVATE repository: %s\n' "$FULL_NAME"
  gh repo create "$FULL_NAME" \
    --private \
    --description 'Agent-orchestrated, evidence-based legacy software modernization' \
    --source=. --remote=origin
fi

if git remote get-url origin >/dev/null 2>&1; then
  remote_url="$(git remote get-url origin)"
  case "$remote_url" in
    "https://github.com/${FULL_NAME}"|"https://github.com/${FULL_NAME}.git"|"git@github.com:${FULL_NAME}"|"git@github.com:${FULL_NAME}.git") ;;
    *) fail "origin points to another repository: $remote_url" ;;
  esac
else
  git remote add origin "${PROJECT_URL}.git"
fi

# Push main first so the default branch is the baseline, not the feature branch.
printf 'Pushing main baseline...\n'
git push origin main:main
printf 'Pushing feature branch...\n'
git push -u origin "${FEATURE_BRANCH}:${FEATURE_BRANCH}"

visibility="$(gh repo view "$FULL_NAME" --json visibility --jq '.visibility')"
[ "$visibility" = 'PRIVATE' ] || fail 'Could not verify private visibility after publishing'

printf '\nPRIVATE repository: %s\n' "$PROJECT_URL"
printf 'Feature branch: %s/tree/%s\n' "$PROJECT_URL" "$FEATURE_BRANCH"
