---
name: legacy-static-decomposition
description: Use after inventory to partition a legacy system by capabilities, data ownership and dependency clusters rather than arbitrarily splitting classes.
---

# Legacy Static Decomposition


## Workflow

1. Read actual AST, calls, schema, runtime entry points and known user workflows. Build a dependency graph of modules, database writes and external services. Record cycles, hubs, shared global state, reflection and dynamic-import ambiguity.
2. Group by business capability and shared invariants; use functions/classes only as implementation units. Identify security and transaction boundaries, state owners, integration seams, deployment units and change cohesion. A package directory alone is not a domain.
3. Suggest reversible migration slices ordered by coupling risk, reachable entry points, data availability and baseline tests. Distinguish a truly independent slice from a component that shares writes or hidden transaction state.
4. Write `docs/legacy/static/decomposition.md` with capability inventory, dependencies, coupling hotspots, unresolved boundaries and candidate seams. Use stable component IDs in diagram/evidence references.
5. Where multiple agents exist, assign bounded capabilities to distinct ORCA contracts/worktrees; in solo mode process the same scopes sequentially.

## Expected checks

No two migration slices silently claim independent ownership of one mutable invariant; essential cross-slice dependencies are visible; unsupported dynamic edges are recorded; every recommendation includes evidence and its reversibility.
