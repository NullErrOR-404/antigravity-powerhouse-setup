---
name: scaffold-spec
description: >-
  Scaffolds the standard 8 living project specification documents in `<project-root>/.spec/`.
  MANDATORY: Trigger automatically when starting any new client project, website, ERP, CRM, or app,
  or when the user runs `/scaffold-spec` or says "init spec", "start project", "create spec docs".
  Ensures zero-hallucination memory across the entire development lifecycle.
user-invocable: true
argument-hint: "[project-name]"
license: MIT
---

# Scaffold Spec - Living Project Memory Engine

Scaffolds the mandatory 8-document living specification matrix inside `<project-root>/.spec/`.

## When to Run
1. Automatically on turn 1 of any new project or when planning a client system.
2. Manually via `/scaffold-spec [project-name]` or "init spec".

## The 8 Documents Scaffolded

Ensure `.spec/` exists and contains:

1. `1_PRD.md` — Product Requirements, Scope, Target Audience Psychographics, Niche Market Model, Core User Stories, and Non-Goals.
2. `2_TRD.md` — Technical Architecture, Chosen Tech Stack, Scalability Profile (Target Concurrency), Connection Pooling, Error Boundaries, Invariants, and Tradeoffs.
3. `3_DATABASE_SCHEMA.md` — Tables, Columns, Foreign Keys, Indexes, Relations, and Migration Logs.
4. `4_BACKEND_SCHEMA.md` — API Endpoints, Payloads, Query Params, Auth Boundaries, and Status Codes.
5. `5_USER_FLOW.md` — Step-by-step user journeys, interaction state machines, edge cases, and graceful failure recovery.
6. `6_UI_UX_DESIGN.md` — Niche-Specific Laws of UX (Jakob's, Hick's, Miller's, Fitts's, Von Restorff, Proximity, Similarity, Common Region), Color Tokens (OKLCH), Typography Scale, 4px Grid, Craft Floor bans, and Motion rules.
7. `7_IMPLEMENTATION_PLAN.md` — 15-minute decomposed task graph with explicit blocking dependencies.
8. `8_DECISION_LEDGER.md` — Chronological log of architecture rulings, schema adjustments, and ADR entries.

## Continuous Synchronization Protocol
- Once scaffolded, the agent reads these files before writing code.
- If an endpoint changes, a database column is added, or a design decision is refined, immediately update the corresponding file and append a 1-line entry to `8_DECISION_LEDGER.md`.
