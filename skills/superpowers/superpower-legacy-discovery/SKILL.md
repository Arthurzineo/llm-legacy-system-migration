---
name: superpower-legacy-discovery
description: User-facing Part 1 superpower. Orchestrate authorized, evidence-backed static legacy discovery, decomposition, diagram generation and the G1 approval gate through ORCA, in solo or delegated mode.
---

# Superpower 1 — Static Legacy Discovery (Part 1 / P001)

## When to use

Invoke when the user requests **start Phase 1**, **Part 1**, **reverse engineer the legacy code**, or **generate legacy architecture documentation**. Requires an authorized repository snapshot. This superpower **does not migrate or edit legacy source**. If ORCA is not bootstrapped, run `superpower-orca` first. A single Chief must complete the same sequence without requiring additional agents.

## Ordered specialist dispatch

1. `orca-project-entry` and `orca-coordination`: identify project state, agent availability, current work ownership and source revision.
2. `legacy-static-inventory` plus language-specific `golang`, `python`, or user-installed language skill: inventory versions, build, entry points, AST tools, symbol/call/dependency relations, schema, integration endpoints and missing analyzers. Check tool availability; do not hallucinate AST output.
3. `legacy-static-decomposition` with `codebase-architecture` and `architecture-audit` as needed: partition by business capabilities, dependency edges, transactional boundaries, hazards and migration seams. Do not assume every class is a module.
4. `legacy-evidence-and-diagrams` with `c4-architecture` and `requirements`-equivalent capability if available: generate only decision-relevant class, ERD, use case, sequence, activity, dependency, C4, data flow or deployment diagram sources and cite their backing code evidence.
5. `qa-methodology` for characterization test candidates, risks and G1 acceptance evidence. When useful invoke `clean-code-quality-gates` **as a diagnostic**, not to refactor the legacy repository.
6. `orca-work-contract` for any real delegations and `ai-memory-v2` only if memory was requested. Reviewers are optional roles; Chief must disclose solo self-review.

Select the minimum necessary subset per task, but **never omit the stages** inventory → decomposition → evidence/diagrams → review. A missing capability becomes an uncertainty record.

## Execution protocol

1. Chief obtains the source authorization, exact revision/commit, repository scope, database artifacts and excluded secrets. Create P001 tasks with independent ownership when delegation is possible.
2. Generate a read-only inventory and tool coverage matrix. Run deterministic parsers/queries where available, recording commands, version, inputs and outputs. Mark any inference as inferred rather than observed.
3. Generate a bounded decomposition report and dependencies/impact map; attach exact source pointers to important decisions.
4. Recover selected architecture and behavior models, each with an evidence ID or `unverified` status. Do not claim a use case is business-confirmed solely from an API route name.
5. Identify golden-master candidate operations, domain invariants, possible risky behavior and missing runtime prerequisites.
6. Reviewer/Chief checks G1: source revision, coverage limits, traceability, explicit uncertainty, sensitive-data exclusions and diagrams with inspectable evidence. Block unverified high-impact business rules, or escalate for human sign-off.
7. Preserve all discoveries and decisions in `.orca` diaries/task files first and project documentation next. Refresh Graphify and AI Memory indexes only after authoritative file updates, if configured.

## Expected target-project directories and files

Read `docs/methodology/OUTPUT-CONTRACT.md` before creating any directory. Use `docs/legacy/source-snapshot.md`, `inventory.md`, `static/{ast-index,calls,dependencies,decomposition,database-schema}.md`, `diagrams/*.{mmd,puml}`, `rules/business-rules.md`, `evidence/`, `uncertainty-register.md`, `reviews/G1-*.md` and `.orca/phases/001-discovery/{PHASE.md,tasks/,diaries/}`. Diagram files are conditional; missing relevant diagrams must have an explanation, not a placeholder.

## Gate and handoff

Do not announce Part 1 complete until G1 is accepted with evidence or a recorded exception. Offer **Part 1.1** by invoking `superpower-legacy-characterization`; the Chief must ask YES/NO/DEFER, including runtime isolation risks. If the user declines, create `docs/legacy/characterization/decision.md` and proceed to `superpower-legacy-migration` only with a prominent verification limitation.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** G1 source-backed inventory, diagram provenance and uncovered-code register.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
