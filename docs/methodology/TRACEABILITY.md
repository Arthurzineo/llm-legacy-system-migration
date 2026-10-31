# Evidence and Traceability Contract

A recovered fact must be linked to the exact snapshot, source path, symbol, supporting observation and the generated artifact(s). Use stable IDs for business rules (BR-*), use cases (UC-*), dependencies (DEP-*), evidence (EV-*), requirements (REQ-*), and tests (TC-*).

```text
source revision + source location
  -> evidence record (verified / inferred / contradicted / unknown)
  -> domain rule or architecture element
  -> diagram and requirements
  -> target module/contract
  -> acceptance and differential test
  -> review result
```

Suggested CSV headers: `requirement_id,evidence_id,behavior_case_id,source_revision,target_component,test_id,review_status`.

An LLM may describe a hypothesis; it must never silently assign it `verified` status. Capture counterexamples, partial coverage and exceptions. Use `schemas/evidence.schema.json` and `examples/evidence.example.json` as a starting point, checking against the actual schema.
