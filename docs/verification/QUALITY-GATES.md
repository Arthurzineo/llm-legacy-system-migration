# Code Quality and Clean Code Gates

Inspired by the **public workflow description** of [unclebob/ub-mode](https://github.com/unclebob/ub-mode). This project does not include a copy of its source skill.

| Dimension | Optional external tool | Interpretation |
| --- | --- | --- |
| Complexity + coverage | [crapper](https://github.com/unclebob/crapper) | CRAP `CC² × (1 − coverage)³ + CC`; requires valid measured coverage. Configure thresholds based on context; a reference target in ub-mode is CRAP < 10. |
| Structurally similar functions | [dryer](https://github.com/unclebob/dryer) | Jaccard similarity of normalized structural fingerprints. Upstream default reports candidates >= 0.82; ub-mode suggests review around 0.8. **Similarity is not proof of duplicate business semantics.** |
| Mutation strength | [mutator](https://github.com/unclebob/mutator) | Inspect killed, survived, uncovered and invalid mutants. Run a passing test baseline first. |
| Coupling and architecture | Language compiler/dependency graph, architecture audit | Detect verified cycles, high-risk shared mutable state, hidden data writers and forbidden imports. Do not invent metrics when unavailable. |
| Behavior and API compatibility | Characterization, BDD/TDD and differential tests | Compare approved outcomes; classify security fixes separately from regressions. |

**Practical process:** write behavior test -> implement -> run actual checks -> inspect findings -> refactor smallest risky area -> rerun tests -> record exceptions with reviewer or human approval.

Quality metrics can be manipulated; do not trade correctness or usability for a single numerical target. Only tool-produced results can be labeled as measured.

## Optional pinned source and runtime choice

The three upstream programs are included as **Git submodules** (`tools/third-party/{crapper,dryer,mutator}`) but are never mandatory. Review `docs/integrations/OPTIONAL-UNCLE-BOB-TOOLS.md` and run `python3 scripts/setup_optional_quality_tools.py --target /path/to/source --json` first.

Only select tools for supported source-language scopes (Clojure, Java, Go, TypeScript/JavaScript, Rust or Python) after the Chief verifies parsing/build support and, for coverage or mutation, real runnable tests. A mixed or unsupported-language system must not be described as fully analyzed. Do not treat source checkout or dependency installation as successful quality measurement. The original repositories and 0BSD licenses remain attached through their Git submodules.

