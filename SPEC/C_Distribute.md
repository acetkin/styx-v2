# C_Distribute

## OVERVIEW (Living)
- positioning: Contract-first deterministic astrology API for integrators that need stable JSON semantics.
- channels: Internal development, partner beta, public API consumers.
- release_policy: Contract compatibility first; endpoint additions allowed, breaking intent/field changes require explicit version strategy.
- versioning: Current stable target is `3.0.0` (SemVer). `metadata.styx_version` and `meta.api_version` must stay aligned with release intent.

## C1 - Stage 1 (Early/Internal) (Living)
- audience: Core team and local QA.
- deliverables:
  - runnable API with `/v1/contract` and envelope endpoints
  - fixture-backed contract smoke tests
  - local runbook and Swagger verification path
- metrics:
  - local startup reliability
  - deterministic output shape
  - Tier 1 tests passing

## C2 - Stage 2 (Beta/Feedback) (Living)
- audience: partner integrators and selected external testers.
- deliverables:
  - intent completeness for contract matrix
  - validation hardening and clearer error payloads
  - compatibility notes and migration guidance
- metrics:
  - low contract error regressions
  - no unplanned schema drift
  - partner feedback resolved in bounded cycles

## C3 - Stage 3 (Stable/Public) (Living)
- audience: public developers and production integrators.
- deliverables:
  - stable `v3.0.0` contract behavior
  - versioned docs/examples for contract + envelope endpoints
  - backward-compatibility and deprecation policy
  - restart playbook from `SEED/ + SPEC/`
- metrics:
  - release stability and uptime targets
  - strict metadata version consistency
  - reproducible rebuild quality from seed/spec artifacts
