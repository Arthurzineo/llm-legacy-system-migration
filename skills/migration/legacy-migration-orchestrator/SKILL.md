---
name: legacy-migration-orchestrator
description: Use when the user requests an end-to-end migration project: route ordered Part 1, optional Part 1.1, and Part 2 through ORCA with explicit artifacts and gates.
---

# Internal Legacy Migration Orchestrator


## Trigger and prerequisites

Activate only for an authorized legacy-modernization effort. First load `orca-project-entry` and `orca-coordination`, identify actual workers, source revision, and whether the project already has ORCA files. A single Chief must be able to complete the workflow sequentially. Read `docs/methodology/OUTPUT-CONTRACT.md` **before creating target folders**.

## Route, not duplication

This is an **internal specialist coordinator**, not an additional user-facing superpower. The user-facing entrypoints are `superpower-legacy-discovery`, `superpower-legacy-characterization` and `superpower-legacy-migration`. This skill is the parent coordinator for internal routing. Read the child skill needed for the current stage. Do **not** preload every child into every agent context:

1. **Part 1 / P001:** `legacy-static-inventory` -> `legacy-static-decomposition` -> `legacy-evidence-and-diagrams`. Run tools/validators and evidence checks before proposing a gate.
2. **Part 1.1 / P002:** the Chief explicitly asks YES/NO/DEFER for isolated dynamic characterization. YES -> read `legacy-dynamic-characterization` and `isolated-legacy-runtime`. NO/DEFER -> persist decision and risks; do not execute. This gate is always represented, even when skipped.
3. **Part 2 / P003:** read `legacy-migration-intake` and `legacy-target-design`. Ask only unknown material preferences after presenting findings and test feasibility. Create target requirements, ADRs, architecture, migration slices, and data plan.
4. **Part 2 / P004:** read `legacy-incremental-implementation` and relevant Go/Python/testing/code-quality skills; implement a verified slice under an ORCA task/contract.
5. **Part 2 / P005:** read `legacy-equivalence-validation` plus QA/security skills; compare target behavior to known legacy behavior and label intentional deviations.
6. **Part 2 / P006:** read `legacy-cutover` and run human go/no-go gates.

## Expected directories

Static analysis belongs to `docs/legacy/static/`; selected diagram source under `docs/legacy/diagrams/`; evidence under `docs/legacy/evidence/`; characterization under `docs/legacy/characterization/`; requested target design under `docs/target/`; differential reports under `docs/verification/`; tasks/diaries/contracts under `.orca/`. **These paths are created in a real target project, not prefilled in this reusable template.** See the full directory tree and file-level contents in `docs/methodology/OUTPUT-CONTRACT.md`.

## Gates and failure paths

G1 requires provenance, bounded diagram coverage, uncertainty register and high-risk inferred-rule review. G2 requires approved target architecture, strategy, budget and data plan. Every migrated slice requires real tests with outputs. G3 requires reconciliation, security approval and rollback. Blocking conditions become logged questions/risks, not invented resolutions. Always report incomplete capabilities and solo-review limitations.
