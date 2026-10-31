# Engineering References and Attribution

## ORCA source (user-owned, private)

- https://github.com/Arthurzineo/orca-agent-skills — prior generic ORCA role, phase, contract, diary and Graphify concepts. This draft writes original migration-specific skills and does not claim the project exposes a working parser or orchestrator.

## AI Memory — version pinned

- https://github.com/akitaonrails/ai-memory/releases/tag/v2.0.1
- https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/install.md
- https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/mcp-install.md
- https://github.com/akitaonrails/ai-memory/blob/v2.0.1/docs/ARCHITECTURE.md

AI Memory v3.3.0 exists as of 2026-10-31; this project intentionally targets **v2.0.1** until a reviewed upgrade. Never silently substitute current upstream CLI syntax or images.

## Uncle Bob — Clean Code inspiration

- https://github.com/unclebob/ub-mode — engineering workflow, TDD, quality gates.
- https://github.com/unclebob/crapper — function-level cyclomatic complexity, coverage and CRAP.
- https://github.com/unclebob/dryer — structural similarity, duplication candidates.
- https://github.com/unclebob/mutator — mutation testing and test strength.
- https://github.com/unclebob/uml-viewer — interactive architecture views.

`crapper`, `dryer`, and `mutator` have BSD-0-Clause licenses in their repositories. We **do not embed their source code** here. `ub-mode` content is only referenced and its ideas are re-expressed as an original skill; no verbatim upstream SKILL.md is copied. If vendoring third-party code/skills later, verify the exact LICENSE for that version and preserve attribution and notices.

## Further techniques

- Legacy characterization and golden-master testing.
- AST-based code inspection, graph-aided retrieval and dependency mapping.
- Incremental strangler migrations and anti-corruption layers.
- Domain-oriented decomposition, C4 views, UML/ERD models and evidence-driven requirements.
