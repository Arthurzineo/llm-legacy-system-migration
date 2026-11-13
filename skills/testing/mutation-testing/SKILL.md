---
name: mutation-testing
description: Use to evaluate test suite strength by mutating code and measuring surviving mutants with bounded runtime costs.
---

# Mutation Testing


## Preconditions

Obtain approval before running potentially expensive test suites. Verify baseline tests are green; mutation tests on failing baselines are uninterpretable. Record file/commit scope and approved test command. For small changes prefer targeted mutation first, especially when the source system is slow.

## Workflow

Choose a verified mutation tool compatible with the project. Uncle Bob's `mutator` supports Clojure, Java, Go, TypeScript, Rust and Python, but tools and behavior vary by version. Follow the installed tool's actual README and verify prerequisites such as `crapper` checkout arrangement; do not fabricate flags. Record killed, survived, uncovered, timeout and invalid mutants separately; inspect surviving mutants and add tests for real missing behavioral assertions.

## Output

Measured score `killed/(killed+survived)` where defined, coverage gaps, stronger assertions, real commands, elapsed time and limitations. Missing tool => `not_measured`, not 100% mutation coverage.

## Optional pinned Mutator checkout

The external `unclebob/mutator` source is available through a pinned submodule at `tools/third-party/mutator` and expects its sibling `tools/third-party/crapper`. Run the language inventory in `scripts/setup_optional_quality_tools.py` before selecting it; supported languages are Clojure, Java, Go, TypeScript/JavaScript, Rust and Python. For an unsupported language, choose an appropriate alternative, or record `not_measured`. Explicitly authorize any dependency installation or costly mutation suite. Source checkout does not count as a mutation result.


## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Executed seeded mutants, killed/survived results, cost and measured scope.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
