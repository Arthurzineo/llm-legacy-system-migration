---
name: linux
description: Use for Linux host runtime analysis, service deployment, legacy dependencies, permissions and operational troubleshooting.
---

# Linux


## Workflow

Inspect the OS distribution, runtime, architecture, service manager, filesystem, permissions, network rules, packages and environment constraints before making changes. Prefer read-only diagnostics first (`systemctl status`, package manifest, environment logs with secrets redacted, sockets and resource usage). Use documented, distribution-appropriate commands and require permission before restarting or installing services.

For migration, reconstruct necessary service accounts, file paths, cron jobs, environment variables, certificates, locales, encodings and database integration. Avoid copying root privileges or world-writable directories into the target. Preserve an operations manifest and a recovery path for every mutation.

Verify services with real logs and tests. Do not equate an open port with a healthy system. Do not persist live secret values into ORCA diaries or AI Memory.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** Actual service/permission/network checks, minimal privileges and recovery procedures.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
