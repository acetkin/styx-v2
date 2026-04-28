# Recent

## ENTRY 1
- Project Name: styx-v2
- DateTime: 2026-01-01T00:00:00Z
- LLM: VAi
- Session ID: 019dd310-8394-7933-a1e6-bd08e0ccef8c
- Instruction: Inspect the styx-v2 repository and report the old STYX filtering system.

Goal:
- Find and summarize the previous three-layer / three-part filter system used in STYX.
- Search code, docs, schemas, tests, and route/contract files for terms such as filter, filters, include, exclude, object selection, fields, sections, depth, output, aspect filters, planet filters, chart filters, timeline filters, and any contract options.
- Identify the exact names of the three filter layers if present.
- Explain what each layer controlled.
- Provide file paths where the system appears.
- Provide example request/response snippets if available.
- Do not modify any files.
- Do not commit.

Output expected:
A concise English report with sections:
1. Summary
2. Three-layer filter model found
3. Relevant files
4. Example snippets
5. Recommendation for new Aion/STYX design

Important: This is inspection only. Do not change the repository.
- Response: I’m inspecting the repository for the older STYX filtering model and will trace it through code, docs, schemas, tests, and route contracts before summarizing the exact layer names and behavior.

`rg` is not installed here, so I’m falling back to `find` and `grep` to map the repo and locate the older filtering terminology.

The first pass shows one clear modern output selector in the contract, but I need to inspect whether the older “three-layer” system existed as a richer model elsewhere or only in documentation and legacy endpoints.

The current branch only exposes a thin `request.output` selector plus some intent-specific filters, so I’m checking git history next to find the older, richer filtering model if it was removed from the working tree.

The current history search suggests the richer model may only survive in older design docs, not active code. I’m pulling those older `SPEC` documents directly from git to confirm the terminology and the three-part breakdown.

I haven’t found a literal “three-layer filter” label yet. Next I’m checking the legacy envelope endpoints and older tests/models, because that’s where a practical three-part selection system would have been enforced if it existed.

There is older pre-contract history in tags like `v2.0.0` and `snapshot-2026-02-02-1714`. I’m searching those snapshots directly, since the filtering system may predate the contract-first rewrite.

I found the clearest legacy control model in the oldest tagged implementation: it combined `transit_type`, `metadata.output`, and timeline `level/body` selectors. I’m pulling the old route/model code to map exactly what each control layer did in runtime terms.

I have enough evidence now. The old system was not a single named class or module called “three-layer filter,” but historical docs and route contracts show a three-part selection scheme centered on mode, output shape, and timeline scope.

**1. Summary**
The old STYX filtering system does appear in repo history, but not as a single explicit class named “three-layer filter.” What I found is a historical three-part request-selection model in the pre-contract API, mostly in commit `e121b47` and its descendants:

1. `transit_type` chose the major output family/mode.
2. `output` further narrowed the returned shape for some modes.
3. `level` / `body` narrowed timeline scope.

In the current branch, that older model is mostly gone. The new contract surface is much thinner: `request.output.verbosity` plus `request.output.astrological_objects`, with a few intent-specific parameters such as `focus`, `limit_events`, and rectification `filters`.

**2. Three-layer filter model found**
No file literally says “three-layer filter model,” but the old API contract clearly behaved like this:

1. **Mode layer**
   Exact field names: `metadata.transit_type`, `metadata.chart_type`
   What it controlled:
   - Which major engine or response family ran.
   - Examples: `transit`, `on_natal`, `synastry`, `astrocartography`, `solar_arc`, `secondary_progression`, `timeline_major`, `eclipses`, `eclipse_transits`, `lunations`.
   Evidence:
   - Historical `SPIN/styx-api/app/models.py` at commit `e121b47`
   - Historical `SPIN/styx-api/app/main.py` at commit `e121b47`
   - Historical `SEED/STYX.md` at commit `e121b47`
   - Historical `SPEC/B_Develop.md` at commit `e121b47`

2. **Output-shape layer**
   Exact field name: `metadata.output`
   Exact values found: `aspects | chart`
   What it controlled:
   - Whether a mode returned aspect results or a chart payload.
   - Confirmed specifically for `secondary_progression`; `metadata.output = "chart"` returned the progressed chart instead of aspect output.
   Evidence:
   - Historical `SPIN/styx-api/app/models.py` at commit `e121b47`
   - Historical `SPIN/styx-api/app/main.py` at commit `e121b47`
   - Historical `SPEC/B_Develop.md` at commit `e121b47`
   - Later docs explicitly call `metadata.output` a removed legacy field.

3. **Timeline-scope layer**
   Exact field names: `metadata.level`, `metadata.body`
   Exact level names found:
   - `level1`
   - `level2`
   - `level3`
   - plus body-like aliases/tokens: `outer`, `jupiter`, `saturn`, `uranus`, `neptune`, `pluto`, `nodes`, `lunations`, `eclipses`, `new_moon`, `full_moon`, `solar_eclipse`, `lunar_eclipse`
   What it controlled:
   - Which timeline band or event family to scan.
   - `level1`: outer planets.
   - `level2`: Saturn + Jupiter.
   - `level3`: lunations/eclipses workflow.
   - `body` further narrowed the timeline to one body or nodes.
   Evidence:
   - Historical `SPIN/styx-api/app/models.py` at commit `e121b47`
   - Historical `SPIN/styx-api/app/main.py` at commit `e121b47`
   - Historical `SPEC/B_Develop.md` at commit `e121b47`
   - Historical `SPIN/styx-api/scripts/export_all_features.py` at commit `e121b47`

Important nuance: I did **not** find exact old field names like `aspect_filters`, `planet_filters`, `chart_filters`, or `timeline_filters` in code or contracts. The older system was selector-driven, not a nested named filter object.

**3. Relevant files**
Current branch:
- [SPIN/docs/contract.json](/home/acetkin06/CodeWorks/styx-v2/SPIN/docs/contract.json)
- [SPIN/styx-api/app/contract_v1/models.py](/home/acetkin06/CodeWorks/styx-v2/SPIN/styx-api/app/contract_v1/models.py)
- [SPIN/styx-api/app/contract_v1/intent_handlers.py](/home/acetkin06/CodeWorks/styx-v2/SPIN/styx-api/app/contract_v1/intent_handlers.py)
- [SPIN/styx-api/tests/fixtures/contract_v1/transit_timeline.json](/home/acetkin06/CodeWorks/styx-v2/SPIN/styx-api/tests/fixtures/contract_v1/transit_timeline.json)
- [SPIN/styx-api/tests/fixtures/contract_v1/rectification.json](/home/acetkin06/CodeWorks/styx-v2/SPIN/styx-api/tests/fixtures/contract_v1/rectification.json)
- [SPIN/styx-api/tests/test_api.py](/home/acetkin06/CodeWorks/styx-v2/SPIN/styx-api/tests/test_api.py)

Historical evidence in git:
- `e121b47:SPIN/styx-api/app/models.py`
- `e121b47:SPIN/styx-api/app/main.py`
- `e121b47:SEED/STYX.md`
- `e121b47:SPEC/B_Develop.md`
- `e121b47:SPIN/styx-api/scripts/export_all_features.py`
- `bb9ef38:SEED/STYX.md`
- `bb9ef38:SPEC/A_Design.md`
- `bb9ef38:SPEC/B_Develop.md`

Most useful “removal” evidence:
- In later docs, legacy fields are explicitly listed as removed: `metadata.output`, `metadata.level`, `metadata.body`, `step_years`.

**4. Example snippets**
Old request examples from historical model:

```json
{
  "metadata": {
    "transit_type": "secondary_progression",
    "timestamp_utc": "2026-01-28T10:00:00+03:00",
    "output": "chart",
    "location": "Karadeniz Eregli"
  },
  "frame_a": { "...": "natal frame" }
}
```

Meaning:
- Mode layer: `secondary_progression`
- Output-shape layer: `chart`

Old timeline example:

```json
{
  "metadata": {
    "start_utc": "2026-01-01T00:00:00Z",
    "end_utc": "2031-01-01T00:00:00Z",
    "level": "level1"
  },
  "natal": { "...": "natal payload" }
}
```

Old narrowed timeline example:

```json
{
  "metadata": {
    "start_utc": "2026-01-01T00:00:00Z",
    "end_utc": "2026-12-31T23:59:59Z",
    "level": "eclipses"
  },
  "natal": { "...": "natal payload" }
}
```

Current contract example:

```json
{
  "metadata": { "intent": "natal", "styx_version": "3.0.0", "request_id": "x" },
  "player": { "birth": { "date": "1982-05-08", "place": "Karadeniz Eregli" } },
  "request": {
    "settings": { "house_system": "placidus", "zodiac": "tropical" },
    "parameters": {},
    "output": { "verbosity": "normal", "astrological_objects": ["natal"] }
  }
}
```

Meaning:
- The old 3-part selector has been reduced to output verbosity plus object allowlist, with some per-intent parameter filters such as `focus`, `limit_events`, and rectification `filters`.

**5. Recommendation for new Aion/STYX design**
Keep the old idea, but formalize it cleanly:

1. Use an explicit 3-layer structure in the new contract:
   - `mode`: which engine/result family
   - `scope`: which objects/events/bodies/time slices
   - `shape`: which sections/fields/detail depth to return

2. Replace scattered legacy selectors with one normalized filter block, for example:
   - `request.filters.mode`
   - `request.filters.scope`
   - `request.filters.shape`

3. Preserve the useful old semantics:
   - old `transit_type` maps to `mode`
   - old `level/body` maps to `scope`
   - old `output` plus current `verbosity/astrological_objects` maps to `shape`

4. Avoid reintroducing ambiguous aliases like `level1/level2/level3` unless they are documented presets. Prefer explicit names such as:
   - `scope.timeline_preset = outer_major | saturn_jupiter | lunations`

5. If Aion/STYX needs long-term stability, document these three layers in the public contract directly. In this repo, the older model was real, but mostly implicit and split across docs, routes, and tests.
