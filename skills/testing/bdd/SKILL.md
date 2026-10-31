---
name: bdd
description: Use for reconstructing business behavior and executable acceptance scenarios (Given/When/Then) across a legacy and modernized implementation.
---

# Bdd


## Method

Start from actors, domain goals, decision tables, authorization, state transitions and actual source/runtime evidence. Turn important workflows into scenarios with `Given` fixtures, `When` actions, `Then` observable outcomes **including database and external side effects**. Add rule exceptions, retries, duplicate events, invalid input and forbidden transitions.

Separate business intent from infrastructure details; choose a runner appropriate for the target language (e.g., Cucumber/Godog, Behave/pytest-bdd) only after verifying installed support. A `.feature` file without executable step definitions and a passing test report is documentation, not proof.

Link scenarios to UC/BR/REQ/TC evidence IDs and baseline observations. When legacy behavior differs from an approved requirement, mark an intentional change; do not silently normalize away security problems.
