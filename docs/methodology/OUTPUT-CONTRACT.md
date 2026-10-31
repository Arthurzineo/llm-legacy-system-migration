# Expected Folder and Artifact Contract

**Each target project** receives the following only when analysis is authorized. This repository contains templates; do not create fake analysis in its own docs.

```text
<target-project>/
  .orca/                              authoritative execution state
    PROJECT.md
    EXEC.md
    phases/
    contracts/
    roles/
    SUMMARY.md
    LESSONS_LEARNED.md
  GRAPHIFY.md                        optional derived graph metadata
  docs/legacy/
    source-snapshot.md               revision, license, data scope
    inventory.md                     languages, runtime, framework, packages
    static/
      ast-index.md                   parser outputs and limitations
      calls.md                       call relationships
      dependencies.md                imports, modules, external APIs
      decomposition.md               capabilities and migration seams
      database-schema.md             DDL, procedures and triggers
    diagrams/
      use-cases.puml                  optional; actors and outcomes
      classes.puml                    optional; source structure
      erd.mmd                         optional; entities/constraints
      c4-components.mmd               optional; boundaries/dependencies
      sequence.mmd                    optional; observable call sequences
      activities.mmd                  optional; decisions and workflows
      data-flow.mmd                   optional; source/sink transformations
      deployment.mmd                  optional; runtime topology
    rules/business-rules.md           IDs and source evidence
    evidence/                        machine-readable claim records
    uncertainty-register.md          unverified claims and blockers
    reviews/                          G1 approval and exceptions
    characterization/                only after optional user opt-in
      decision.md                    YES / NO / DEFER + justification
      environment/                   pinned Dockerfile/Compose or VM instructions
      fixtures/                      synthetic and isolated test inputs
      observations/                  input/output/state effects
      golden-master/                 normalized expected behavior
  docs/target/
    questionnaire.md                  user choices and unresolved answers
    requirements.md                   requirements and acceptance tests
    architecture.md                   target design, diagrams and rationale
    data-migration.md                 mapping and reconciliation rules
    adrs/                             architecture decisions
  docs/verification/
    traceability.csv                  requirement->source->design->test
    equivalence/                      differential reports and deviations
    quality/                          CRAP, duplication, mutation, coupling
    security/                         threat model and verified scan output
    release/                          deployment plan, gates, rollback
```

## Storage and source authority

- Write derived evidence with source revision, path, line/identifier, deterministic tool versions and analysis timestamp.
- Never overwrite legacy files as a documentation side effect; use worktrees for generated code.
- Diagram source files and a provenance record are authoritative for generated PNG/SVG renders, not vice versa.
- Diagram files listed here are **conditional**. Missing irrelevant diagrams are acceptable if a rationale is documented; missing critical runtime semantics must be flagged.
- `docs/legacy/characterization/decision.md` is required even when characterization is skipped.
- Do not commit production secrets, identifiers, raw dumps or privileged scan outputs.
