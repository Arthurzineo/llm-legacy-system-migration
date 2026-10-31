# ORCA Contract Template

```yaml
contract_id: C-YYYYMMDD-NNN
project_id: <project-id>
phase_id: P001
task_id: T001
chief: <current-chief-id>
agent: <actual-session-agent-or-chief>
role: <role>
execution_mode: delegated # or solo
parent_contract: null
status: proposed
delegation_allowed: false
required_skills: []
required_context: []
scope: []
non_goals: []
may_modify: []
may_not_modify: []
acceptance_criteria: []
review_requirements: []
security_requirements: []
reports_to: <chief-id>
```

## Contract lifecycle

PROPOSED -> ACCEPTED -> ACTIVE -> DELIVERED -> ACCEPTED_BY_CHIEF -> COMPLETED. BLOCKED/CANCELLED are documented exit states.

**Solo mode:** the Chief records the equivalent assignment and acceptance on the task record with `execution_mode: solo`; no pretend external agent or review. Document self-verification and request human approval for high-risk decisions when an independent reviewer is unavailable.

## Completion

List modified files, evidence locations, tests executed (or not executed), decisions, open risks, and final diary checkpoint. Task ownership is exclusive even when multiple roles are held by the same agent.
