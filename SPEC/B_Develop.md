# B_Develop

## OVERVIEW (Living)
- implementation_strategy: Maintain a dual-interface runtime:
  - contract-first API (`POST /v1/contract`) as primary integration surface
  - envelope endpoints for direct compute and operational diagnostics
- quality_bar: Deterministic outputs, stable schema names, stable intent names, and explicit version invariants (`3.0.0`).
- packaging_policy: Deliverable code lives in `SPIN/styx-api`; non-submission artifacts remain in `SPIN/_local` and `SPIN/_logs`.
- test_policy:
  - Tier 1 (quick): `pytest -q -k fixture_smoke_suite` plus focused touched-area tests
  - Tier 2 (PR gate): `pytest -q tests/test_contract_v1.py` and `pytest -q tests/test_smoke.py`
  - Tier 3 (full): `python -m pytest -q` only for schema/core-risk changes

## STAGES (Living)
- current_stage: S3
- next_stage: NONE
- active_deliverable: styx-api

### S0 - Setup / Alignment
- goal: Establish deterministic repository skeleton and seed/spec governance.
- exit_criteria:
  - `SEED/reSpec.md`, `SEED/STYX.md`, `SEED/snapshot.md` exist
  - `SPEC/A_Design.md`, `SPEC/B_Develop.md`, `SPEC/C_Distribute.md` exist
  - `SPIN/` workspace created with deliverable structure

### S1 - MVP / First Working Slice
- goal: Build compute endpoints and baseline envelope behavior.
- exit_criteria:
  - `/v1/health`, `/v1/config`, `/v1/chart` implemented
  - deterministic payload behavior verified
  - baseline tests green

### S2 - Hardening / Feedback Loop
- goal: Add universal contract endpoint and complete intent handlers.
- exit_criteria:
  - `/v1/contract` operational with implemented intent matrix
  - contract fixture smoke suite passing
  - contract errors/validation return stable envelope shape
  - envelope endpoints still operational

### S3 - Release / Stable
- goal: Freeze compatibility semantics for v3.0.0 and keep restart reproducibility high.
- exit_criteria:
  - `metadata.styx_version == "3.0.0"` across contract responses (ok/error/contract)
  - `meta.api_version == "3.0.0"` for envelope responses
  - seed/spec are sufficient to rebuild near-current behavior without `SPIN/`
  - release docs and policy aligned to current runtime

## TASKS (Living)

### BACKLOG

#### T-20260210-01 Restart blueprint hardening
- intent: Make restart from `SEED/ + SPEC/` reproducibly regenerate near-current API.
- plan_refs:
  - `SEED/STYX.md#Restart-Reconstruction-Profile`
  - `SPEC/A_Design.md#A2`
- implement_path:
  - `SPEC/A_Design.md`
  - `SPEC/B_Develop.md`
  - `SEED/STYX.md`
- acceptance:
  - restart instructions include endpoint matrix and version invariants
  - architecture section references contract modules and version source
- steps:
  - keep intent matrix in seed/spec synchronized with contract artifact
  - ensure test tier policy is documented in develop plan
- done_check:
  - [ ] implemented
  - [ ] basic test / verification
  - [ ] docs updated (if needed, via DUP)

#### T-20260210-02 Compatibility policy finalization
- intent: Finalize contract/envelope backward-compatibility and deprecation workflow.
- plan_refs:
  - `SPEC/C_Distribute.md#C3`
- implement_path:
  - `SPIN/docs/compatibility.md`
- acceptance:
  - documented policy for non-breaking vs breaking changes
  - explicit deprecation lead time and communication path
- steps:
  - write policy draft
  - run stakeholder review
- done_check:
  - [ ] implemented
  - [ ] basic test / verification
  - [ ] docs updated (if needed, via DUP)

### CURRENT

- T-20260210-01 Restart blueprint hardening.

### COMPLETED

#### T-20260210-00 Contract version invariant (done)
- intent: Ensure `metadata.styx_version` returns real `3.0.0` for all contract statuses.
- plan_refs:
  - `SPEC/A_Design.md#A3`
  - `SPEC/C_Distribute.md#C3`
- implement_path:
  - `SPIN/styx-api/app/core/version.py`
  - `SPIN/styx-api/app/contract_v1/responses.py`
  - `SPIN/styx-api/tests/test_contract_v1.py`
- acceptance:
  - contract ok/error metadata version equals `3.0.0`
  - smoke/focused Tier 1 tests pass
- done_check:
  - [x] implemented
  - [x] basic test / verification
  - [x] docs updated (if needed, via DUP)

### RELEASE-CHECKLIST

## LOG (Append-only)

### [2026-01-26 16:47] Session 01
- scope_level: SPEC
- summary: Created SPEC skeleton and SEED/snapshot.md after seed normalization.
- llm_reasoning_summary: Followed ReSpec Kickstart creation step to initialize governed docs.
- human_llm_conversation_summary: User approved continuing with SPEC and snapshot creation.
- decisions:
  - Proceeded with template-based SPEC files and a short snapshot.
- files_touched:
  - SPEC/A_Design.md
  - SPEC/B_Develop.md
  - SPEC/C_Distribute.md
  - SEED/snapshot.md
- terminal_summary_id: TS-20260126-01

### [2026-01-26 16:47] Terminal Summary TS-20260126-01
- commands: New-Item SPEC; Set-Content SPEC/A_Design.md; Set-Content SPEC/C_Distribute.md; Set-Content SEED/snapshot.md; Set-Content SPEC/B_Develop.md
- exit_codes: all 0
- stdout_summary: Directories/files created.
- stderr_summary: none

### [2026-01-26 16:51] Session 02
- scope_level: SPIN
- summary: Created SPIN workspace and updated SPEC/SEED summaries for spin phase.
- llm_reasoning_summary: Entered Spin phase and aligned living docs and tasks to seed scope.
- human_llm_conversation_summary: User requested sequential execution of SPIN creation, SPEC updates, and task planning.
- decisions:
  - Set current stage to S1 and queued MVP implementation tasks.
- files_touched:
  - SPIN/
  - SPEC/A_Design.md
  - SPEC/B_Develop.md
  - SPEC/C_Distribute.md
  - SEED/snapshot.md
- terminal_summary_id: TS-20260126-02

### [2026-01-26 16:51] Terminal Summary TS-20260126-02
- commands: New-Item SPIN; Set-Content SPEC/A_Design.md; Set-Content SPEC/C_Distribute.md; Set-Content SEED/snapshot.md; Set-Content SPEC/B_Develop.md
- exit_codes: all 0
- stdout_summary: SPIN directories created; SPEC/SEED updated.
- stderr_summary: none

### [2026-01-28 23:20] Session 03
- scope_level: SPIN
- summary: Hardened /v1/chart and /v1/transit, added astrocartography results, moved runtime assets/logs, and simplified response meta per requirements.
- llm_reasoning_summary: Implemented user-requested payload changes, added astrocartography computation with dataset support, and aligned SPIN structure with updated delivery rules.
- human_llm_conversation_summary: User directed response schema changes, transit mode expansion, astrocartography behavior, ephe/log placement, and generic ReSpec updates.
- decisions:
  - Keep deliverable-only assets under SPIN/styx-api and move scratch/venv/caches to SPIN/_local.
  - Astrocartography uses cities dataset with top-N nearest by orb; location not required.
  - Config centralizes defaults/aspects/provenance; meta trimmed to essentials.
- files_touched:
  - SPIN/styx-api/app/main.py
  - SPIN/styx-api/app/services/astro.py
  - SPIN/styx-api/app/services/geocode.py
  - SPIN/styx-api/app/models.py
  - SPIN/styx-api/tests/test_api.py
  - SPIN/styx-api/data/cities5000.txt
  - SPIN/styx-api/data/countryInfo.txt
  - SPIN/styx-api/tests/fixtures/cities.txt
  - SPIN/styx-api/tests/fixtures/countries.txt
  - SPIN/styx-api/pyproject.toml
  - SEED/reSpec.md
- terminal_summary_id: TS-20260128-01

### [2026-01-28 23:20] Terminal Summary TS-20260128-01
- commands: Move-Item SPIN/_local/ephe -> SPIN/styx-api/ephe; Move-Item uvicorn logs -> SPIN/_logs; pytest -q; Invoke-WebRequest cities5000.zip/countryInfo.txt; Move-Item .venv/.pytest_cache/__pycache__ -> SPIN/_local
- exit_codes: all 0 (last pytest passed)
- stdout_summary: Runtime assets/logs moved; datasets downloaded; tests passing.
- stderr_summary: none

### [2026-01-29 00:40] Session 04
- scope_level: SPIN
- summary: Finalized astrocartography with country names, orb filtering, and crossings output.
- llm_reasoning_summary: Added country-name mapping, max-orb filter, and crossings list to improve astrocartography usefulness.
- human_llm_conversation_summary: User requested full country names and crossings like Pluto/Nodes; accepted defaults and asked to log completion.
- decisions:
  - Astrocartography filters results by max orb (default 2.0; env override).
  - Add crossings list with bodies + nodes + angles and top-N cap.
  - Country names resolved via countryInfo dataset.
- files_touched:
  - SPIN/styx-api/app/services/astro.py
  - SPIN/styx-api/app/main.py
  - SPIN/styx-api/tests/test_api.py
  - SPIN/styx-api/tests/fixtures/countries.txt
  - SPIN/styx-api/data/countryInfo.txt
- terminal_summary_id: TS-20260129-01

### [2026-01-29 00:40] Terminal Summary TS-20260129-01
- commands: pytest -q
- exit_codes: all 0
- stdout_summary: Tests passing after astrocartography updates.
- stderr_summary: none

### [2026-01-29 01:10] Session 05
- scope_level: SPEC
- summary: Updated S2 notes for astrocartography crossings and solar arc sun mode; marked transit skeleton task done.
- llm_reasoning_summary: User requested doc updates after completing astrocartography and solar arc work.
- human_llm_conversation_summary: User asked to log completed work and proceed with secondary progression next.
- decisions:
  - Treat /v1/transit skeleton as completed.
- files_touched:
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260129-02

### [2026-01-29 01:10] Terminal Summary TS-20260129-02
- commands: n/a (doc update)
- exit_codes: n/a
- stdout_summary: Updated living notes and task status.
- stderr_summary: none

### [2026-01-29 02:05] Session 06
- scope_level: SPIN
- summary: Implemented secondary progression aspects (day-for-year) and updated docs.
- llm_reasoning_summary: Added progressed chart computation for secondary progression and aspects vs natal; kept response as aspects list.
- human_llm_conversation_summary: User requested to continue after astrocartography and proceed with secondary progression.
- decisions:
  - Use day-for-year progression based on natal timestamp and target timestamp.
- files_touched:
  - SPIN/styx-api/app/main.py
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260129-03

### [2026-01-29 02:05] Terminal Summary TS-20260129-03
- commands: pytest -q
- exit_codes: all 0
- stdout_summary: Tests passing after secondary progression update.
- stderr_summary: none

### [2026-01-29 02:20] Session 07
- scope_level: SPEC
- summary: Logged user confirmation that astrocartography is complete; prepared to continue with next S2 item.
- llm_reasoning_summary: User requested doc/log update after finishing astrocartography.
- human_llm_conversation_summary: User marked astrocartography done and asked to proceed with item 2.
- decisions:
  - Record astrocartography completion status in living log.
- files_touched:
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260129-04

### [2026-01-29 02:20] Terminal Summary TS-20260129-04
- commands: n/a (doc update)
- exit_codes: n/a
- stdout_summary: Logged astrocartography completion and next-step intent.
- stderr_summary: none

### [2026-01-29 02:35] Session 08
- scope_level: SPIN
- summary: Added secondary progression chart-only output option.
- llm_reasoning_summary: User requested progressed chart without aspects for easier validation.
- human_llm_conversation_summary: User asked for a progressed chart output without transit aspects.
- decisions:
  - `secondary_progression` accepts `metadata.output = chart`.
- files_touched:
  - SPIN/styx-api/app/models.py
  - SPIN/styx-api/app/main.py
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260129-05

### [2026-01-29 02:35] Terminal Summary TS-20260129-05
- commands: n/a (code+doc update)
- exit_codes: n/a
- stdout_summary: Added chart-only secondary progression output.
- stderr_summary: none

### [2026-01-29 03:05] Session 09
- scope_level: SPEC
- summary: Marked completed charts/transits and recorded remaining calculated items.
- llm_reasoning_summary: User confirmed tests for synastry and requested end-of-session checklist/log update.
- human_llm_conversation_summary: User asked to mark completed endpoints and capture notes before closing session.
- decisions:
  - Treat all chart and transit modes as completed for S2 tracking.
  - Leave calculated outputs pending.
- files_touched:
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260129-06

### [2026-01-30 15:35] Session 10
- scope_level: SPEC
- summary: Marked eclipses outputs as LLM workflow via lunations CSV and updated calculated chart notes.
- llm_reasoning_summary: User opted to avoid API-side eclipse events/transit generation in favor of lunations CSV + LLM requests.
- human_llm_conversation_summary: User approved documenting eclipses handling via lunations CSV.
- decisions:
  - Treat eclipses and eclipse_transits as handled by lunations CSV + LLM workflow (no API calc).
- files_touched:
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260130-01

### [2026-01-30 20:57] Session 11
- scope_level: SPEC
- summary: Updated Level 1/2/3 timeline definitions and removed node timeline from calculated outputs.
- llm_reasoning_summary: Aligned calculated outputs with user-defined levels and moved nodes to transit outputs only.
- human_llm_conversation_summary: User requested Level 1 (outer), Level 2 (Saturn+Jupiter), Level 3 (lunations) with nodes removed from timeline.
- decisions:
  - Level 1: outer planets only.
  - Level 2: Saturn + Jupiter.
  - Level 3: lunations CSV + LLM workflow.
- files_touched:
  - SPEC/B_Develop.md
- terminal_summary_id: TS-20260130-02

### [2026-01-30 20:57] Terminal Summary TS-20260130-02
- commands: n/a (doc update)
- exit_codes: n/a
- stdout_summary: Updated S2 calculated levels and notes.
- stderr_summary: none

### [2026-01-30 22:09] Session 12
- scope_level: SPIN
- summary: Reworked secondary progression timeline output to match transit timeline schema and added tests.
- llm_reasoning_summary: Aligned progression timeline with the same event/phase structure used by transit timeline for readability and consistency.
- human_llm_conversation_summary: User requested secondary progression timeline in the same format as transit timeline with station info.
- decisions:
  - Progression timeline returns transit/natal/aspect plus phases with exact_index.
  - Outer planets excluded from progression timeline.
- files_touched:
  - SPIN/styx-api/app/services/progression_timeline.py
  - SPIN/styx-api/app/models.py
  - SPIN/styx-api/app/main.py
  - SPIN/styx-api/tests/test_api.py
  - SPIN/styx-api/app/config.py
- terminal_summary_id: TS-20260130-03

### [2026-01-30 22:09] Terminal Summary TS-20260130-03
- commands: pytest -q
- exit_codes: all 0
- stdout_summary: All tests passing after progression timeline changes.
- stderr_summary: none

### [2026-01-30 23:10] Session 13
- scope_level: SPIN
- summary: Normalized endpoint latency + description logging into a single JSON file under SPIN/_logs.
- llm_reasoning_summary: Consolidated per-endpoint latency into endpoint_descriptions.json for easier Kharon reference.
- human_llm_conversation_summary: User requested log consolidation and updated to-do tracking before ending the day.
- decisions:
  - Maintain endpoint descriptions with a single Latency_in_ms key per entry.
- files_touched:
  - SPIN/_logs/endpoint_descriptions.json
- terminal_summary_id: TS-20260130-04

### [2026-01-30 23:10] Terminal Summary TS-20260130-04
- commands: python -c (endpoint_descriptions normalization)
- exit_codes: all 0
- stdout_summary: endpoint_descriptions.json updated and latency keys normalized.
- stderr_summary: none

### [2026-02-01 10:50] DUP Entry DUP-20260201-01
- target:
  - SPEC/A_Design.md (OVERVIEW, A1, A2, A3)
  - SPEC/B_Develop.md (OVERVIEW, STAGES, TASKS, S2 notes)
  - SPEC/C_Distribute.md (OVERVIEW, C1, C2, C3)
  - SEED/STYX.md (Project Brief, Deliverables, Constraints, Acceptance, API Surface, Response/Output Types)
  - SEED/snapshot.md (full refresh)
- change_intent:
  - Align design scope to current endpoints: /v1/health, /v1/config, /v1/chart, /v1/transit, /v1/timeline, /v1/progression_timeline.
  - Document envelope responses (meta/settings/input_summary/data/timing/errors) and deterministic rounding to 2 decimals for chart/transit outputs.
  - Record astrocartography data inputs (cities5000 + countryInfo), crossings output, and lunations CSV workflow for level3/eclipses.
  - Update interaction rules: location input supports place string, object, and auto/ip; timestamp_utc supports "now" where applicable; geocode/geoip failures -> 422.
  - Refresh stages/tasks to reflect S2 completion and S3 stabilization focus; update distribution deliverables/metrics accordingly.
- applied_edits:
  - Updated SPEC/A_Design.md, SPEC/B_Develop.md, and SPEC/C_Distribute.md to reflect envelope responses, current endpoints, and S3 focus.
  - Refreshed SEED/STYX.md and SEED/snapshot.md to match current API scope, datasets, and timeline/progression behavior.

### [2026-02-01 10:50] Session 14
- scope_level: SPEC
- summary: Updated SEED/SPEC living docs to match current API scope, envelope responses, datasets, and S3 focus.
- llm_reasoning_summary: Aligned governed docs with implemented endpoints, workflows, and release stage for accurate handoff.
- human_llm_conversation_summary: User approved updating SPEC and seed files to the latest state.
- decisions:
  - Treat S2 as complete and move focus to S3 stabilization.
  - Standardize documentation around envelope responses and CSV-backed lunations/eclipses.
- files_touched:
  - SPEC/A_Design.md
  - SPEC/B_Develop.md
  - SPEC/C_Distribute.md
  - SEED/STYX.md
  - SEED/snapshot.md
- terminal_summary_id: TS-20260201-01

### [2026-02-01 10:50] Terminal Summary TS-20260201-01
- commands: apply_patch (SPEC/A_Design.md, SPEC/B_Develop.md, SPEC/C_Distribute.md); Set-Content SEED/STYX.md; Set-Content SEED/snapshot.md
- exit_codes: all 0
- stdout_summary: Updated SPEC and SEED living docs and refreshed snapshot.
- stderr_summary: none

### [2026-02-02 17:14] DUP Entry DUP-20260202-01
- target:
  - SPEC/A_Design.md (OVERVIEW, A1, A2, A3)
  - SPEC/B_Develop.md (OVERVIEW, STAGES, S2 notes)
  - SPEC/C_Distribute.md (OVERVIEW, C1, C2, C3)
  - SEED/STYX.md (full refresh)
  - SEED/snapshot.md (full refresh)
- change_intent:
  - Align design/seed scope to latest API: /v1/health, /v1/config, /v1/chart, /v1/transit, /v1/timeline; chart types include natal/moment/solar_arc/secondary_progression; unify timelines and remove deprecated modes/endpoints.
  - Remove legacy fields and tighten request/response descriptions to current shapes (transit only, timeline bodies, lunations/eclipses tokens).
  - Refresh distribution and snapshot to match S3 focus.
- applied_edits:
  - Updated SPEC/A_Design.md and SPEC/B_Develop.md to reflect unified timelines, transit-only, and removed legacy fields.
  - Updated SPEC/C_Distribute.md deliverables to remove progression_timeline and non-transit modes.
  - Refreshed SEED/STYX.md and SEED/snapshot.md to match latest API scope and examples.

### [2026-02-10 05:40] DUP Entry DUP-20260210-01
- target:
  - SEED/STYX.md (full refresh)
  - SEED/snapshot.md (full refresh)
  - SPEC/A_Design.md (OVERVIEW, A1, A2, A3 full refresh)
  - SPEC/B_Develop.md (OVERVIEW, STAGES, TASKS living sections refresh)
  - SPEC/C_Distribute.md (OVERVIEW, C1, C2, C3 full refresh)
- change_intent:
  - Align seed/spec with current runtime contract-first scope and version `3.0.0`.
  - Capture restart objective explicitly: regenerate near-current output from only `SEED/ + SPEC/`.
  - Encode version invariants for both interfaces:
    - contract metadata: `metadata.styx_version == "3.0.0"`
    - envelope metadata: `meta.api_version == "3.0.0"`
  - Refresh architecture/task/distribution sections around `/v1/contract` and intent matrix.
- applied_edits:
  - Rewrote `SEED/STYX.md` to include contract intent matrix, version semantics, and restart reconstruction profile.
  - Updated `SEED/snapshot.md` with 2026-02-10 state and next actions.
  - Rewrote `SPEC/A_Design.md` and `SPEC/C_Distribute.md` for v3.0.0 alignment.
  - Updated `SPEC/B_Develop.md` living sections and added this DUP/session trail.

### [2026-02-10 05:40] Session 15
- scope_level: SPEC
- summary: Refreshed SEED/SPEC to match current v3.0.0 behavior and restart-from-seed/spec objective.
- llm_reasoning_summary: Existing seed/spec reflected older envelope-first scope and lacked contract/version invariants required for reliable restart reconstruction.
- human_llm_conversation_summary: User asked to align SEED and SPEC with current implementation so future development can start from seed/spec only and reach near-current output.
- decisions:
  - Treat `/v1/contract` as primary public surface in planning docs.
  - Keep envelope endpoints documented as active secondary interface.
  - Make version invariants explicit and non-negotiable in acceptance/distribution criteria.
- files_touched:
  - SEED/STYX.md
  - SEED/snapshot.md
  - SPEC/A_Design.md
  - SPEC/B_Develop.md
  - SPEC/C_Distribute.md
- terminal_summary_id: TS-20260210-01

### [2026-02-10 05:40] Terminal Summary TS-20260210-01
- commands: `rg` scans for version/scope drift; `Get-Content` reviews; `apply_patch` updates for SEED/SPEC files
- exit_codes: all 0
- stdout_summary: living docs refreshed to contract-first v3.0.0 state; append-only log entries added.
- stderr_summary: none
