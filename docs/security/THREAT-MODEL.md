# Security Requirements and Legacy Execution Risks

Legacy code may be malicious, unpatched, and capable of reaching production systems. Execution requires **explicit user approval**, an approved test scope, controlled images, and isolation chosen after threat assessment. A Docker container alone is not a guaranteed security boundary; use a disposable VM when threat or runtime privileges warrant it.

Minimum constraints: no production credentials/data; no Docker socket mount; nonroot where possible; read-only legacy source mounts; no privileged mode; restricted egress; resource/time/process limits; explicit volume ownership; pinned dependency hashes; sandbox teardown; no connection to production services. Use synthetic fixtures, test accounts and local mocks. Never use a production database as a characterization fixture.

For tool integrations: read-only diagnostics before configuration changes; pin AI Memory release; do not log bearer tokens or paste credentials into prompts; protect any persisted memory files, MCP clients and derived embeddings. Never import client-held secrets into shared project memories. For migrated code, SAST, SCA, threat modeling, authorization tests and verified security deviation approvals start during implementation rather than only at final QA.
