---
name: golang
description: Use for Go project design, modernization, idiomatic interfaces, concurrency, tests, error handling and performance-sensitive implementation.
---

# Golang


## Scope

Apply when Go is the target or current language. Do not force Java/C#/Python legacy domain objects into Go class-shaped structures. Read target requirements, performance and failure constraints first.

## Workflow

1. Verify installed Go version, `go.mod`, packages, build tags, vendoring and runtime platform. Pin the supported toolchain and dependency policy; do not claim builds passed without running them.
2. Decompose packages by stable business capability and public interfaces; prefer small consumer-owned interfaces, simple concrete types, explicit constructors and clear direction of imports. Avoid Java-style inheritance, excessive interface layers and global mutable state.
3. Use context propagation for request-scoped cancellation; make goroutines/queues lifecycle-managed. Test races where concurrency exists; review error wrapping, timeouts, retries and resource cleanup.
4. Design persistence around ownership, transactions, migration scripts and rollback. Avoid incorrect behavior caused by `nil` vs zero values, timezone/encoding changes or JSON behavior.
5. Test with `go test ./...` and `go test -race ./...` when appropriate. Inspect real `go vet`, lint and benchmarks if available. Run characterization and differential tests against the legacy behavior.
6. Record semantic differences from the legacy language, public API contracts, data layouts, performance and security impacts.

## Deliverable

Small tested packages and explicit interfaces, no unapproved additional framework; changed paths, tests, tool versions and limitations in the ORCA diary.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Go build/race tests, DB compatibility and source↔target semantic differences.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
