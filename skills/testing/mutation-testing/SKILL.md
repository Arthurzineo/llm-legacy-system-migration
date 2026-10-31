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
