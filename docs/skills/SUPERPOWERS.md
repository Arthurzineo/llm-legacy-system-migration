# Superpowers — Four Entry Skills, Many Specialists

There are **exactly five user-facing superpowers**. They are intentional commands for the Chief rather than dozens of independent skills the user must remember. The Chief uses the actual ORCA runtime to discover available workers, selects the relevant specialists, reads their `SKILL.md` instructions and executes under `.orca/` tasks and contracts. A plain skill file cannot automatically spawn another agent.

| User request (any language) | Entrypoint skill | Phase | Purpose |
| --- | --- | --- | --- |
| Start ORCA / Setup ORCA | `superpower-orca` → `orca-setup` | P000 or project resume | Mandatory Chief setup: verified roster, solo/delegated roles, optional contracts, diaries, Graphify and opt-in AI Memory |
| Start Part 1 | `superpower-legacy-discovery` | P001 | Static inventory, dependency and database analysis, diagrams and evidence |
| Start Part 1.1 | `superpower-legacy-characterization` | P002, optional | Ask YES / NO / DEFER, plan a safe environment and build characterization tests only if approved |
| Start Part 2 | `superpower-legacy-migration` | P003–P006 | Questionnaire, architecture decisions, migration slices, equivalence, quality gates and transition |
| Start Part 3 | `superpower-operational-assurance` | P007–P009 | Release readiness, controlled rollout, cross-client parity, observability, recovery and handoff |

## Activation model

1. The entry superpower is **selected by explicit user request or an approved phase plan**.
2. The Chief reads its workflow and the `required` skill list from `docs/skills/superpowers.json` and evaluates contextual conditions.
3. The Chief reads the actual child skill files just before the corresponding work. It must not claim a skill is executed merely because it appears in the manifest.
4. Each delegated agent receives only role/task-relevant skills plus project context in its ORCA contract. Without extra agents the Chief performs equivalent work sequentially and labels reviews as not independent.
5. Each output is checked against its phase acceptance gate. The next superpower is offered or invoked only when approved and its prerequisites are satisfied.

The superpowers are **not another source of task truth**: authority remains in `.orca/`, repository evidence, contracts and the Chief's permitted actions. Graphify and AI Memory remain derived retrieval layers.

## Deterministic routing preview (does not execute anything)

```bash
python3 scripts/superpower_plan.py --list
python3 scripts/superpower_plan.py --stage orca
python3 scripts/superpower_plan.py --stage part1 --condition architecture --condition language-python
python3 scripts/superpower_plan.py --stage part1.1       # requires Chief to ask YES/NO/DEFER
python3 scripts/superpower_plan.py --stage part1.1 --decision YES
python3 scripts/superpower_plan.py --stage part2 --condition implementation --condition verification
```

`--decision YES` previews the intended skills but **does not authorize actions by itself**; the Chief must have an explicit current user decision and approved execution plan. `--decision NO/DEFER` produces no dynamic execution skill list. The Python program is a **read-only manifest validator and plan viewer**, not a dispatch engine. Genuine agent dispatch uses the installed runtime's version-matched documented orchestration interface.

## Extensibility

Specialists are organized under `skills/{core,migration,programming-languages,architecture,design,system,testing,miscellaneous}/<skill>/SKILL.md`. Add your own language, framework, architecture or QA skills without changing the four user-facing entrypoints. A maintainer may extend the **conditional** groups in `docs/skills/superpowers.json`, validate names, document triggers and keep specialist scope narrow.

`python3 scripts/install_skills.py --list` discovers all categorized skills, including the `superpowers` category. Installing nested skills into a flat agent skill directory is an explicit opt-in; see `docs/skills/CATALOG.md`.

## Gate summary

- `superpower-operational-assurance`: G4 readiness, G5 authorized deployment/parity, G6 production operations and recovery acceptance.

- `superpower-orca`: valid Chief, actual agent capabilities and authoritative project state.
- `superpower-legacy-discovery`: source-backed G1 inventory, diagram traceability and uncertainty review.
- `superpower-legacy-characterization`: explicit YES/NO/DEFER; if YES, isolated and reproducible behavioral observations; otherwise limitations recorded.
- `superpower-legacy-migration`: approved G2 target architecture, P004 slice test results, P005 equivalence and security evidence, G3 human cutover approval.

## Mandatory ORCA setup entry (internal skill)

`setup-orca` is an alias for the **existing** `superpower-orca`, which must load `orca-setup` after `orca-project-entry`. There are five Superpowers. The Chief inventories currently available agents and their tools, proposes division of responsibilities and optional delegation to the user, assigns one owner per task, and issues bounded contracts to real workers. With no workers (or if the user prefers solo), the Chief performs every role sequentially and marks review non-independent.

Before starting a migration phase, the same setup flow offers project-scoped AI Memory **v2.0.1**: binary version check, server health, per-agent MCP connection, lifecycle hooks, and live `memory_status` verification. Neither memory installation nor automatic prompts capture are implied by simply starting ORCA.

