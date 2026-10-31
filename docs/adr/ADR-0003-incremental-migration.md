# Incremental Migration

Status: proposed

## Decision

Prefer bounded, reversible migration slices with compatibility seams unless a justified full rewrite is approved. Preserve data invariants and prepare rollback before cutover.

## Consequences

A gate records the evidence supporting each migration strategy and rejected alternatives.
