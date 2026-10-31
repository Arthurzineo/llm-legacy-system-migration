# LLM - LEGACY SYSTEM MIGRATION

> **Design-stage project.** Local Git development branch only. No GitHub repository has been created, no migration engine has run, and no real legacy application has been analyzed.

A reusable, agent-agnostic operating model for reverse-engineering and migrating unsupported legacy software. It combines ORCA work ownership, agent skills, evidence-backed diagrams, optional isolated characterization, AI Memory v2.0.1, and incremental migration with executable acceptance criteria.

## Principles

1. **Chief-first, single-agent capable.** A single Chief may execute every role; delegate only when extra agents are available and useful. Agent availability is rechecked every session.
2. **No fictional evidence.** Source, tests, runtime observations, and verified schemas outrank inferred diagrams and AI memory.
3. **Behavior before rewrite.** Preserve observable business behavior or explicitly approve deviations. Security defects are not automatically compatibility requirements.
4. **Skills are modular.** The ORCA coordination model is reusable outside legacy migration. Skills are discovered by their `SKILL.md` metadata and activated only when relevant.
5. **English repository artifacts.** Skills, prompts, documentation, variable names, commit templates, and reports are in English. Users may interact in any language, including Portuguese.
6. **Opt-in operations.** Do not install tools, start containers, alter user agent configuration, publish code, or connect external services without authorization.

## Four user-facing Superpowers

Instead of making users remember dozens of skills, the Chief exposes exactly **four primary Superpowers**. Each one reads and routes to the appropriate specialized skills and uses existing ORCA contracts and diaries. The Chief can run **alone** or delegate if other real agents are available; agent availability is checked in the current session, never inferred from a role name.

| User command | Superpower | Scope |
| --- | --- | --- |
| Start ORCA | `superpower-orca` | Generic project bootstrap, Chief, optional delegation, contracts and memory |
| Start Part 1 | `superpower-legacy-discovery` | Static reverse engineering, source evidence and diagrams |
| Start Part 1.1 | `superpower-legacy-characterization` | Optional, explicit YES / NO / DEFER, isolated runtime and characterization |
| Start Part 2 | `superpower-legacy-migration` | Questionnaire, target architecture, incremental implementation, validation and cutover |

See the [Superpowers guide](docs/skills/SUPERPOWERS.md) and the [routing manifest](docs/skills/superpowers.json). Inspect the read-only routing plan with:

```bash
python3 scripts/superpower_plan.py --list
python3 scripts/superpower_plan.py --stage part1
python3 scripts/superpower_plan.py --stage part1.1
```

Superpowers are **orchestration instructions**, not an automatic agent dispatcher. Their selected child `SKILL.md` files are loaded just in time. Actual dispatch, tool execution and installation depend on the current agent runtime, contract and explicit authorization.

## User-facing methodology

| Step | Internal ORCA phase | Objective | Gate |
| --- | --- | --- | --- |
| Foundation | P000 | Configure generic ORCA, agents, memory, skills | ORCA project-entry status checked |
| Part 1 | P001 | Static analysis, decomposition, architecture/UML/ERD documentation | Evidence and diagram review |
| Part 1.1 (optional) | P002 | Isolated runtime, synthetic data, characterization tests | Behavior evidence or justified skip |
| Part 2 — planning | P003 | Interactive intake, architecture target, migration plan | Plan and risk approval |
| Part 2 — implementation | P004 | Incremental implementation with ORCA contracts | Component acceptance |
| Part 2 — verification | P005 | Differential/regression/security verification | Independent evidence or human risk acceptance |
| Part 2 — transition | P006 | Data reconciliation, controlled cutover, rollback | Deployment approval |

The Chief **must ask whether Part 1.1 should be attempted**, explain feasibility and security implications, and record YES / NO / DEFER. If NO, do not claim behavioral equivalence proven by dynamic testing.

## Folder layout

```text
AGENTS.md                       Project entry and routing rules
.orca/                          Work contracts, phases, roles, diaries, Chief state
GRAPHIFY.md                     Optional derived graph configuration
skills/
  superpowers/                  Only four main user-facing stage entrypoints
  core/                         Generic ORCA protocol and session routing
  migration/                    End-to-end and per-stage migration workflows
  programming-languages/        Go, Python; extensible by users
  architecture/                 C4, architectural audits, design patterns
  design/                       Design systems and interface consistency
  system/                       Docker, Linux, isolated runtime
  testing/                      TDD, BDD, QA, differential and mutation testing
  miscellaneous/                AI Memory, Clean Code, quality gates, refactoring
scripts/                         Opt-in integration, skills installer, validators
schemas/                         JSON contracts for findings and observations
docs/                            Architecture, methodology, memory, security, plans
examples/                        Synthetic examples, never live data
tests/                           Scaffolding and integration script tests
```

User-supplied skills belong at `skills/<category>/<slug>/SKILL.md` with unique frontmatter `name`. The installer makes flat, standard `skills/<slug>/SKILL.md` copies in a **selected target directory**; it does not overwrite other agents' skills by default.

## Start locally

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/install_skills.py --list
python3 scripts/install_skills.py --target /tmp/orca-skills-preview
python3 scripts/ai_memory_doctor.py --json
```

Installation and lifecycle changes are always opt-in; see [AI Memory 2.0.1](docs/integrations/AI-MEMORY-V2.md) and [skills installation](docs/skills/CATALOG.md).

## Primary documentation

- [Four Superpowers and invocation guide](docs/skills/SUPERPOWERS.md)

- [ORCA coordination model](docs/architecture/ORCA-OPERATING-MODEL.md) and [protocol](docs/architecture/ORCA-PROTOCOL.md)
- [Migration workflow](docs/methodology/METHODOLOGY.md)
- [Expected outputs and directory contract](docs/methodology/OUTPUT-CONTRACT.md)
- [Skill catalog](docs/skills/CATALOG.md)
- [AI Memory v2.0.1 setup](docs/integrations/AI-MEMORY-V2.md)
- [Traceability and evidence](docs/methodology/TRACEABILITY.md)
- [Quality and equivalence](docs/verification/TEST-STRATEGY.md)
- [Security constraints](docs/security/THREAT-MODEL.md)
- [Original methodology drawing](docs/architecture/original-methodology.png)
- [Third-party references and licenses](docs/research/REFERENCES.md)
- [Prompt to start ORCA](prompts/ORCA-PROJECT-ENTRY.md) and [migration prompt](prompts/LEGACY-MIGRATION-START.md)
- [Local branch and publication restrictions](BRANCH.md)

## Status and non-goals

This branch establishes the **workflow specifications and local validation scripts**, not a finished migration product. Static parsers, automatic diagram accuracy, environment reconstruction, the AI Memory server, and GitHub publication have **not** been executed or verified against a legacy codebase. The original user's diagram is included only as reference material.
