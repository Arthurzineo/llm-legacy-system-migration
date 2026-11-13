---
name: legacy-static-inventory
description: Use for Part 1 source inventory, AST/call/dependency/schema analysis, deterministic tools and source-backed discovery before generating diagrams.
---

# Legacy Static Inventory


## Preconditions

Read `legacy-migration-orchestrator`, source authorization and current ORCA contract. Make read-only changes to source by default; perform analysis in a separate output directory. Record immutable repository commit SHA, checked-out tree, excluded binaries, language/runtime versions and available parsers.

## Workflow

1. Inventory files, packages, services, build configurations, schemas/migrations, data access, routes, CLI commands, frontend entry points, background jobs, third-party APIs, licenses and unsupported dependencies. Distinguish source files, generated code, vendored code and secrets.
2. For each supported language select and **verify** a parser/tree-sitter grammar or native compiler frontend; extract AST and symbol table when possible. Do not treat regex scanning as a complete AST.
3. Build actual imports and call relationships; distinguish compile-time, inferred dynamic dispatch, reflective calls and missing edges. Record tool versions and failures. Record database DDL plus constraints, stored procedures and triggers, not just model class names.
4. Produce `docs/legacy/source-snapshot.md`, `inventory.md`, `static/ast-index.md`, `static/calls.md`, `static/dependencies.md`, `static/database-schema.md` with exact source pointers and unsupported features.
5. Send discovered facts and bounded uncertainty to `legacy-static-decomposition` and `legacy-evidence-and-diagrams`; never automatically modernize source in this stage.

## Acceptance criteria

High-impact claims reference the actual source revision and supporting file/symbol/line or verified environment output. Summaries explicitly distinguish **observed code structure** from **LLM interpretation**. Reports indicate coverage limits and absent parsers.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Immutable revision plus parser versions, AST/graph coverage and unsupported inputs.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
