---
name: tdd
description: Use for red-green-refactor implementation of a behavior, bug fix or migration slice with executable, scoped automated tests.
---

# Tdd


## Loop

**RED:** define one externally meaningful behavior and prove that its test fails for the intended missing behavior, not because setup is broken. **GREEN:** implement the smallest change to pass the test. **REFACTOR:** improve design without changing observed behavior, rerunning relevant tests after each step.

Prefer contract-facing tests to private implementation call counts. Include negative and boundary cases, authorization, persistence and concurrency when relevant. Preserve legacy characterization fixtures where compatible; do not modify baseline expected values merely to make generated code pass. Mutation testing may reveal weak tests but is not a substitute for domain-level scenarios.

## Evidence

Record failing test, code change, passing test, surrounding regression results, tool versions and any skipped verification. In solo ORCA mode this is a self-executed, non-independent evidence trail.
