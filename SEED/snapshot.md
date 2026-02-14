ReSpec Snapshot
phase: iteration
active_deliverable: styx-api
snapshot_date: 2026-02-10
snapshot_author: LLM

status_1p: STYX is stabilized around a contract-first v3.0.0 API. The universal endpoint `/v1/contract` is active with implemented intent handlers, while legacy envelope endpoints remain available for direct compute workflows. Current priority is preserving compatibility and restart reproducibility from `SEED/ + SPEC/`.

key_decisions:
- Canonical version target is `3.0.0` and must be reflected in contract metadata (`metadata.styx_version`) and envelope API metadata (`meta.api_version`).
- `/v1/contract` is the primary public integration surface; envelope endpoints are retained.
- Restart quality is a first-class requirement: docs must be sufficient to rebuild near-current output without `SPIN/`.

recent_findings:
- Contract intent coverage is complete for current matrix, including chart/transit/timeline intents and `contract` status payload.
- Version source is centralized in code and now resolves to `3.0.0`.

open_questions:
- Should envelope endpoint docs be versioned as legacy-compatible or peer-equal with contract endpoint docs?
- Should next release freeze include strict backward-compatibility tests for all contract fixtures in CI gate?

blockers:
- None.

next_actions:
- Keep `SEED/STYX.md` and `SPEC/*` synchronized with runtime behavior after each contract change.
- Maintain Tiered test reporting in every implementation update.
