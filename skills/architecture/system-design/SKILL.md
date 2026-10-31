---
name: system-design
description: Use to design target system architecture from requirements, consistency, throughput, resilience, security and operational constraints.
---

# System Design


## Workflow

1. Separate confirmed requirements, unknowns, hard constraints and measurable quality targets.
2. Identify actors, write ownership, data classification, APIs/events and critical state transitions.
3. Define runtime architecture, persistence, concurrency model, transaction boundaries and deployment topology. Estimate capacity only where it affects a choice.
4. Evaluate synchronous vs asynchronous processing, retries/idempotency, distributed consistency, graceful degradation and migration coexistence.
5. Include auth, secrets, security zones, logging/metrics/tracing, operational SLOs, backups/restore, release and rollback from the start.
6. Write ADRs for nontrivial tradeoffs; validate with representative failure/change scenarios rather than only normal-path sequence diagrams.

## Output

Target architecture and testable assumptions connected to requirements and legacy evidence.
