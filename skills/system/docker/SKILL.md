---
name: docker
description: Use when building or running reproducible Docker images or Compose environments, especially isolated legacy characterization.
---

# Docker


## Security preflight

Docker is a packaging/runtime mechanism, not a universal strong sandbox. For unsupported or potentially hostile legacy code, decide whether a disposable VM is required. Never mount `/var/run/docker.sock`, run `--privileged`, attach production networks, or pass real credentials as a convenience.

## Workflow

1. Audit runtime and base image versions, dependencies, exposed ports, mounts, data directories, external services and startup/health behavior.
2. Pin approved images/toolchains, lock dependencies, minimize context and layers, use `.dockerignore` and nonroot execution where feasible. Buildkit/Compose capabilities depend on actual installed versions.
3. Use restrictive networking, resource limits, read-only mounts, temporary databases and synthetic fixtures for optional characterization. Design explicit cleanup and reset.
4. Verify build logs, start/stop, healthcheck, source/checksum integrity, test data seeding and repeatability. Avoid treating a successful `docker build` as a passing application test.
5. Save the approved environment manifest under `docs/legacy/characterization/environment/`, including known isolation limits.

## Exit

Reproducible setup or clear infeasibility report, with approved execution scope and no exposure to production.
