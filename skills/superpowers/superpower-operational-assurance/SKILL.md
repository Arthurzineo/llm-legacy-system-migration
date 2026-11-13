---
name: superpower-operational-assurance
description: User-facing Part 3 superpower for release readiness, controlled deployment, operational validation, observability and post-release handoff; never assumes production authorization.
---

# Part 3 — Operational Assurance (P007–P009)

## Trigger
Use only after Part 2 verification/cutover planning when the user requests operational release, production validation or operational handoff. Also usable to audit an existing deployment without changing it. Do not use for code modernization alone.

## Prerequisites
Read the current ORCA project state, P005 verification evidence and P006 cutover plan. Establish deployment target and authorization boundaries. Missing tests or unknown infrastructure must be reported, not inferred. Read-only inspection is allowed within access scope; any deploy, restart, rollback, DNS, database or access-control change needs explicit approval.

## Workflow
1. P007 — release readiness: activate `release-readiness`. Validate source SHA, artifact hashes/signatures, SBOM/dependencies, security checks, contract and database compatibility, tested backup/restore, capacity goals, implementation and rollback plan. Record GO / NO-GO / CONDITIONAL plus owner approval. A passing CI job is insufficient.
2. P008 — deployment and parity: activate `controlled-rollout` and `cross-client-parity` when multiple clients exist. Prefer canary/blue-green/gradual release as applicable; verify TLS, authentication, authorization, migrations, health checks and client/server version compatibility. Do not deploy merely because a plan was generated.
3. P009 — operation and handoff: activate `operational-observability` and `operational-recovery`. Verify logs, metrics, alerts, restore procedures, SLOs, incident response, credentials/certificates lifecycle, operational runbooks and decommission decision. Monitor an agreed observation window using available tools; do not claim continuous monitoring without real execution.

## Required artifacts and exit gates
Produce `docs/operations/release-readiness.md`, `deployment-evidence.md`, `client-parity.md` (or not-applicable), `operational-acceptance.md` and `risk-register.md` with actual revisions, commands, timestamps, observed results and human decisions. 
- G4: approved plan, independently verified recovery where possible, readiness criteria met or explicit risk acceptance.
- G5: deployment/version and functional parity verified in real target environment, or clearly marked not-verified.
- G6: operational handoff accepted; monitoring, backups, restore, capacity and rollback evidence or explicit unresolved blockers.

## Safety and truthfulness
Never record a planned command as run. Do not mark owner-reported deployment independently verified. Do not equate pilot availability with production-wide acceptance. Do not use production secrets, personal data or unrestricted tests as fixtures. Chief-only review is non-independent. Every external write requires explicit per-action authority and must be logged in the ORCA diary.
