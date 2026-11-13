---
name: legacy-incremental-implementation
description: Use during Part 2 to migrate one bounded, testable legacy slice with TDD/BDD, feedback from compilers and controlled ORCA contracts.
---

# Legacy Incremental Implementation


## Plan a slice

Select one bounded business capability from `docs/legacy/static/decomposition.md`; collect evidence IDs, characterization tests, approved target contracts and source ownership. Prefer a compatibility seam with reversible routing. Assign an actual ORCA worker or a solo Chief scoped task.

## Execution

1. Write behavior-oriented acceptance tests (Given/When/Then where useful) and expected database/API effects. Run a failing target test first when TDD is applicable.
2. Apply deterministic rewrite tools for mechanical syntax/API changes; use LLMs for semantic adaptation with explicit context and review. Do not blindly transcribe global state or vulnerabilities from the legacy system.
3. Implement the smallest complete vertical path with unit/integration tests and fallbacks. In a multiagent runtime isolate concurrent workers' worktrees and file ownership.
4. Compile, test, lint and inspect actual diagnostic output; use bounded feedback loops with max attempts. Record changes to contract, APIs, data and behavior.
5. Run the relevant `clean-code-quality-gates`, `tdd`, `bdd` and selected language skills. Missing quality tools mean `not_measured`, never invented scores.
6. Request an independent reviewer if available; otherwise mark a genuine Chief self-review and obtain human approval for risky deviations.

## Deliverables

Migrated source, test suite, migration ADR/change notes, evidence/traceability updates, failing/passing test logs, and a completed ORCA task with explicit next slice.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Bounded vertical slice with failing→passing acceptance tests and reviewable diff.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
