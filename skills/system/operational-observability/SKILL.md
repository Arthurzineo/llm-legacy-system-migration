---
name: operational-observability
description: Design and verify SLO-based monitoring, alerting, runbooks and service-level operational acceptance for a migrated system.
---

# Operational Observability

## Use
P009, after a deploy or during a read-only operational audit.

## Procedure
1. Define critical user journeys, SLIs/SLOs, failure budgets and relevant dimensions (errors, latency, throughput, saturation).
2. Verify available metrics, structured logs with redaction, traces, audit events, actionable alerts and incident escalation ownership.
3. Measure representative load and failure modes with authorized limits; avoid treating one memory snapshot as concurrent-user capacity proof.
4. Inspect certificate/token expiration, backup freshness, scheduled jobs and deployment drift; record known blind spots.
5. Confirm runbooks and an observation window. Never claim ongoing monitoring without an active authorized mechanism.

## Output
`docs/operations/operational-acceptance.md`: SLO measurements, tool timestamps, alert tests, incident contacts and status PASS / FAIL / NOT_MEASURED.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** SLO baseline, verified alerts, operational logging and measured load envelope.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
