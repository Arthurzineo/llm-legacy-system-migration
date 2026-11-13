---
name: design-system
description: Use for consistent UI migration, design tokens, accessibility, component conventions and frontend modernization when user interfaces are in scope.
---

# Design System


## Scope and goals

Do not invent a frontend migration if the user requests only backend modernization. Capture existing user journeys, accessibility constraints, navigation, roles, form validation and API dependencies.

## Workflow

1. Catalog present UI components and assets; identify repeated patterns, obsolete libraries and hidden client-side business rules.
2. Define tokens for typography, spacing, semantic color, layout and states; support keyboard navigation, screen-reader labels and contrast requirements.
3. Establish reusable components with explicit interfaces, visual and behavior regression criteria, error/loading/empty states and interaction boundaries.
4. Preserve important workflows while allowing approved UX improvements. Record BDD scenarios and screenshot/DOM accessibility checks when tools exist.
5. Test API contract compatibility, session handling, authorization and safe input rendering. Do not imply visual parity from a generated image alone.

## Output

Versioned tokens/components, workflow comparison, accessibility checks and approved intentional changes.

## Evidence and completion contract

- **Activation:** Read only for a relevant task; record NOT_APPLICABLE when its conditions do not hold.
- **Concrete result:** UI parity/accessibility outcomes backed by real browser/native checks.
- **Verification:** Cite source revision, file/symbol, executed command, exit status, observation scope, artifacts, timestamps and exceptions where applicable. A written plan is not an executed check. Use PASS, FAIL, PARTIAL, NOT_RUN, NOT_APPLICABLE rather than an unsupported green status.
- **Stop and escalate:** Missing source, tooling, authorization, or objective evidence blocks a completion claim. Chief-only reviews are non-independent.
