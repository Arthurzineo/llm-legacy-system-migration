---
name: isolated-legacy-runtime
description: Use to plan and verify an explicit opt-in runtime isolation environment for executing unpatched or unsupported legacy software.
---

# Isolated Legacy Runtime


## Gate

This skill must not execute unless the Chief recorded a Part 1.1 `YES` decision and security authorization. Prefer a disposable VM when the trust model requires stronger isolation than containers can offer.

## Workflow

1. Inventory required runtime, databases, OS libraries, privileges and outbound connections. Identify danger of remote code execution, obsolete TLS/crypto, deserialization, injection and unsafe startup scripts.
2. Design minimal network policy with deny-by-default egress, approved image provenance, resource limits, nonroot users, no host Docker socket, ephemeral storage and synthetic data. External integrations are mocked with documented fidelity.
3. Make a reproducible build/run/stop/reset procedure. Require manual review of image build and execution steps before first run.
4. Run smoke and characterization tests only in the approved boundary; capture outputs/side effects and destroy the environment after use.
5. If dependency retrieval or deployment cannot be done securely, report blocked/partial rather than disabling isolation controls.

## Output

Approved plan and repeatability record, observed test log or explicit unexecuted status.
