# Mapping From the Existing ORCA Skills Collection

The user-owned repository `Arthurzineo/orca-agent-skills` contains a generic skill library organized primarily as `skills/<name>/SKILL.md`. This project provides **new English, categorized, migration-aware instructions**, not a verbatim mirror. The following source areas informed the corresponding new skills and should be compared before importing updates:

| Original skill (source repository) | Categorized target skill |
| --- | --- |
| `orca-project-entry`, `orca-project-structure`, `orca-protocol`, `orca-work-contract` | `core/orca-project-entry`, `core/orca-project-structure`, `core/orca-coordination`, `core/orca-work-contract` |
| `golang`, `python` | `programming-languages/golang`, `programming-languages/python` |
| `architecture-audit`, `codebase-architecture`, `c4-architecture`, `system-design` | `architecture/*` matching these names |
| `design-patterns`, `design-patterns-best-practices` | `architecture/design-patterns` |
| `docker`, `linux-admin` | `system/docker`, `system/linux` |
| `tdd-best-practices`, `qa-methodology` | `testing/tdd`, `testing/qa-methodology`; `testing/bdd` is new |
| `refactoring-best-practices` | `miscellaneous/refactoring` |
| `graphify-project-knowledge` | `GRAPHIFY.md` and `core/orca-project-entry` protocol integration |
| `requirements`, `secure-software-engineering` | integrated into `legacy-migration-intake`, `legacy-target-design`, QA and threat-model docs |
| `orca-summarizer` | `.orca/roles/summarizer.md`, `core/orca-coordination` |

The original repository and its installed skills are not modified by this branch. Existing upstream skills may be added to categories manually, after validating name uniqueness and any license constraints. Third-party Clean Code repositories (`unclebob/ub-mode`, `crapper`, `dryer`, `mutator`) are referenced in `docs/research/REFERENCES.md` rather than vendored.
