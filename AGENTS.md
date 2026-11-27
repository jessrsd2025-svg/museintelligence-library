# AGENTS.md — MuseIntelligence Library

- **Document class:** Agent governance and workflow specification
- **Project:** MuseIntelligence Library (`museintelligence-library`)
- **Status:** Working specification
- **Revision:** 1.0
- **Governed content:** the full public scrape of "jessrsd's Blog" —
  580 published posts, 2023-12-22 to 2026-11-27, one markdown file
  per post under `library/`, indexed in `index.json`.
- **Companion app repo:** https://github.com/jessrsd2025-svg/museintelligence-app
  — the MuseIntelligence ICD203 reading-room and governance app.
  This library is the corpus that app governs.
- **Sources:**
  - `SRC-WP-SCRAPE-2026-11-27` — the full public scrape of
    jessrsdincyahoocom.wordpress.com (580 published posts) —
    retrieved 2026-11-27T16:42:05Z — human-reviewed: no
    (re-scrape; supersedes the 2026-11-25 snapshot of 577 posts,
    `SRC-WP-SCRAPE-2026-11-25`, retrieved 2026-11-25T18:01:10Z)
  - `SRC-ICD203-RENDERING-2026-11-23` — the ICD203 rendering —
    retrieved 2026-11-23 — human-reviewed: no
  - `SRC-ICD203-GEMINI-SPEC-2026-11-25` — the ICD203 Gemini
    app-creation specification — retrieved 2026-11-25T14:50:07Z —
    human-reviewed: no
- **Epistemic status:** every claim in this file is SOURCE_REPORTED
  unless its cited source is human-reviewed. No claim in this file
  is VERIFIED_FACT. No silent epistemic upgrade is performed by any
  agent working under this file.

## Abstract

MuseIntelligence Library is a source-code library of the full public
scrape of "jessrsd's Blog": 580 published posts as individual
markdown files under `library/`, indexed in `index.json`, with a
Python package (`readingroom/`) to load, search, and check them. It
is a read-only archive. It governs every file in it with provenance,
epistemic tags, and the 18-gate acceptance checklist, and it never
re-asserts the posts' claims as fact. This `AGENTS.md` gives coding
and content agents direction for preserving the project's conceptual
coherence, source integrity, and governance boundaries. It is a
project instruction file, not a claim that the proposed system has
been empirically validated.

## 1. Project overview

- Central symbolic anchor: the owl/Muse figure; the nest or glowing
  egg as the intelligence core; the globe as the connected-world
  layer; the skyline/network as the operational environment.
- Primary title: **Renderings of Strategic Dynamics**
- Primary workflow: **Observe → Orient → Decide → Act**
- Supporting workflow: **Capture → Analyze → Strategize → Execute**
- Use these phrases consistently unless the human explicitly directs
  a revision.
- The library's governed corpus is the blog scrape: 580 published
  ReadingRoom posts (2023-12-22 to 2026-11-27), covering the
  Chainlink institutional stack, Treasury tokenization, Neo4j graph
  governance, prediction-market sentiment, GeoJSON spatial analysis,
  and the LIBERTAS // VERITAS // AEQUITAS doctrine. The library
  archives that corpus; it does not re-assert the corpus's claims
  as fact.
- Repository layout: `library/` (580 post files by year/month),
  `index.json` (the index), `readingroom/` (load, search, load by
  source_id, provenance check, CLI), `tools/` (`build_library.py`,
  `aequitas_gate_linter.py`), `tests/`, `COLLABORATION.md`.

## 2. Governance precedence hierarchy

Resolve instruction conflicts highest to lowest:

| Rank | Tier |
| --- | --- |
| 1 | Human-Approved Policy |
| 2 | AGENTS.md |
| 3 | AEQUITAS Gate |
| 4 | Task Contract |
| 5 | CHAIN.md Dispatch |
| 6 | Model Preference |

Lower-precedence instructions may operationalize higher-precedence
rules but must not override them. If a conflict cannot be resolved
by this hierarchy, stop the conflicting action and request human
adjudication. Never silently reinterpret policy.

## 3. Agent operating cycle: OODA

- **3.1 Observe:** capture the user request, source files,
  constraints, and signals; identify each source and its locator
  before treating it as evidence; separate direct observations from
  interpretations, generated analysis, and speculation; record
  uncertainty and missing context. In this repo, observation goes
  through the index (`index.json`) and the loader
  (`readingroom/library.py`).
- **3.2 Orient:** establish context, source quality, scope, and
  applicable policy; distinguish primary-source material from
  secondary reporting and model-generated synthesis; check for
  conflicting signals and alternate interpretations; select the
  mindset — **Spatial Mode** for topology, geometry, and coordinate
  validation; **Convergent Mode** for separating municipal legal
  baselines from secondary reporting (§7).
- **3.3 Decide:** select an action supported by the contract,
  verified evidence, and governing policy; make assumptions
  explicit; do not promote assumptions to facts; prefer reversible,
  scoped changes where uncertainty remains; escalate consequential
  ambiguity to a human. Decisions are gated by the AEQUITAS gates
  and the interdiction triggers (§4, §12; enforced by
  `tools/aequitas_gate_linter.py`).
- **3.4 Act:** execute only within approved scope and authorized
  tool boundaries; verify the result against acceptance criteria;
  preserve source links, provenance, status transitions, and audit
  information; feed failures into calibration proposals; do not
  autonomously modify human-approved policy.

## 4. Deterministic evidence interdiction

Intercept any inbound object that matches a trigger below. Apply its
forced disposition before the object is used downstream.

| Trigger | Forced disposition |
| --- | --- |
| INCOMPLETE_PROVENANCE | Route to quarantine; halt promotion until source_id, source_locator, and retrieval_timestamp are all present. |
| SIMILARITY_IS_NOT_CORROBORATION | Strip evidentiary weight; similarity may retrieve candidates, it is never corroboration. |
| MARKET_SIGNAL_IS_NOT_EVENT_EVIDENCE | Tag SENTIMENT_ONLY; never event evidence; never authorizes a graph mutation. |
| GENERATED_SUMMARY_IS_NOT_SOURCE_EVIDENCE | Reject verbatim attribution; label the material GENERATED_ANALYSIS and keep it separate from verbatim source passages. |
| PROHIBITED_CAUSAL_RELATIONSHIP | Downgrade the edge to RELATED_TO; causal predicates are prohibited (see §8). |
| SILENT_EPISTEMIC_UPGRADE | Block promotion and preserve unverified status; no automated transition to VERIFIED_FACT is permitted. |

**Evidence rules:**

- Traceability is necessary but does not prove truth or
  corroboration.
- Embedding similarity may retrieve candidates; it is not evidence
  by itself.
- Keep primary source text distinguishable from generated analysis.
- Never infer causal authority from association.
- Human sign-off must be explicit and auditable for epistemic
  status upgrades.
- Quarantined material is not accepted evidence until reviewed.

## 5. Role & boundary matrix

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Reader / Searcher | Loads and searches the corpus (`readingroom/library.py`); reports what the corpus says with its provenance. | Cannot edit post files or assign VERIFIED_FACT labels. |
| Ingestion & Rebuild Worker | Re-runs the scrape and `tools/build_library.py` to rebuild `library/` and `index.json` from a fresh scrape. | Cannot assign VERIFIED_FACT labels; cannot alter post content. |
| Critic & Skeptical Reviewer | Audits outputs for conflation (e.g., merging Chainlink PoR attestations with off-chain legal custody) and flags "skill smells." | Cannot promote claims; flags only. |
| Provenance & Security Reviewer | Verifies SHA-256 digests, commit SHAs, and zero-external-call compliance (`tools/aequitas_gate_linter.py`, `readingroom/library.py` provenance check). | Holds halt authority. |
| Human Supervisor | Sole authority permitted to sign off on epistemic promotions and on publishing this repo. | No agent may act in this role. |

## 6. OBSERVE panel tools

| Tool | Role | Output contract |
| --- | --- | --- |
| TOOL-OSINT-DOC-01 | Document OSINT observation | Registered source objects with provenance. The scrape (`docs/wordpress-posts.md` in the app repo) is this tool's output for the corpus. |
| TOOL-GEO-01 | Spatial / GeoJSON observation | GeoJSON layers, `[lon, lat]` order, `navigation_suitability: 0`. |
| TOOL-GH-01 | Commit-anchor verifier | Pinned-commit reads only (see below). |
| TOOL-CHAIN-01 | Chainlink Proof of Reserve / oracle observation | PoR hashes bounded as integrity anchors, never event evidence on their own. |
| TOOL-SENSOR-01 | Sensor / telemetry observation | Registered source objects with provenance. |
| TOOL-MKT-01 | Market-signal observation | SENTIMENT_ONLY envelopes; never event evidence; `graph_mutation_authorized` false; `human_review_required` true. Market content inside the archived posts is SENTIMENT_ONLY as published. |

### TOOL-GH-01 — commit-anchor verifier

All GitHub reads in this project go through TOOL-GH-01, implemented
in the companion app repo's `tools/github_call.py`. The module
exposes four operations: `pin_commit_sha`, `verify_ref`,
`fetch_bytes_at_sha`, and `hash_bytes`. Rules: fetch only at pinned
40-hex commit SHAs; never fetch from an unpinned ref; never trust a
branch HEAD. Branch names (main, master, HEAD) are refused. The
invariant is: **commit_sha is the anchor; branch names are not.**
No credential or API key is stored in this repository.

## 7. Mindset selection

- **Spatial Mode:** validate topology and polygon coordinates;
  coordinates must use `[lon, lat]` ordering; enforce
  `navigation_suitability = 0` and `live_tracking: false`; do not
  equate geometric validity with navigational suitability.
- **Convergent Mode:** isolate municipal legal baselines from
  secondary reporting; preserve source class and evidentiary role;
  do not merge secondary reporting into a municipal legal baseline;
  if the resolution procedure is not specified, surface the
  ambiguity instead of inventing a rule.

## 8. Provenance & data rules

- Every source object carries a unique `source_id`, a stable
  `source_locator`, and a UTC `retrieval_timestamp`. A payload
  lacking any of the three is INCOMPLETE_PROVENANCE and fails the
  build (gate A1; deterministic routing to quarantine, gate E1).
- Canonicalization follows RFC 8785 before SHA-256 hashing
  (gate A2).
- External GitHub or Hugging Face references are pinned to
  immutable commit SHAs (TOOL-GH-01), never floating branch names
  (gate A3).
- Primary legal texts, secondary analyses, on-chain oracle hashes,
  and forum posts are stored as separate nodes rather than merged
  claims (gate A4).
- No claim is assigned VERIFIED_FACT without human review.
  Automated transitions from SOURCE_ASSERTION or CONTEXT_SIGNAL to
  VERIFIED_FACT are programmatically blocked (gate B1).
- Market and sentiment content is SENTIMENT_ONLY: it is never event
  evidence and never authorizes a graph mutation (gate B2).
- Generated analysis is labeled GENERATED_ANALYSIS and never
  substituted for verbatim source passages (gate B4).
- `graph_mutation_authorized` and `c2_mutation_authorized` default
  to false across all automated scripts (gate C1).
- Unverified relationships are restricted to RELATED_TO,
  MENTIONED_WITH, SUPPORTED_BY, and QUARANTINED_AS. Causal
  predicates (CONTROLS, OWNS, FINANCES, EXECUTES_C2) are absent as
  relationship types (gate C2).
- All GeoJSON layers enforce `[longitude, latitude]` coordinate
  order, `navigation_suitability: 0`, and `live_tracking: false`
  (gate C3).
- Unverified claims render strictly as RED_HOLLOW nodes;
  SOLID_MARKERS appear only where human-reviewed provenance exists
  (gate C4).
- No silent epistemic upgrades are performed. No merged claims. No
  causal edges are asserted.
- **Library rule:** post files under `library/` are reproduced
  faithfully from the scrape and are never edited by hand. To
  change the corpus, re-scrape and rebuild with
  `tools/build_library.py`.

## 9. Runtime model — this library has none

This library is a static archive and a search package; it loads no
model and downloads no weights. The companion app's runtime model
is Qwen/Qwen2.5-7B-Instruct — an instruction-tuned 7B open-weights
model (7.61B parameters, 131,072-token context, Apache License 2.0,
ungated on Hugging Face), verified to exist on Hugging Face
2026-11-25. Its commit SHA is to be pinned at build time via the
TOOL-GH-01 flow; no SHA is stated here. The model is a reasoning
engine only: it never assigns VERIFIED_FACT, and the governance
precedence hierarchy (§2) places model preference last.

## 10. Rendering & markdown conventions

When drafting a rendering, wiki/index page, or research note for
this project:

1. Use a descriptive title, subtitle or document class, abstract,
   keywords, numbered sections, and conclusion.
2. Separate specification, hypothesis, inference, and empirical
   result.
3. Preserve terminology from source material.
4. Do not fabricate authors, affiliations, citations, data,
   experiments, metrics, or findings.
5. Mark proposed metrics as proposed; mark untested mechanisms as
   design proposals.
6. Use tables for precedence orders, trigger rules, modes, and
   verification matrices.
7. Include limitations and open specification items where the
   sources leave gaps.
8. Cite external sources when used; do not cite generated analysis
   as primary documentation.
9. Every rendered claim carries its source_id, source_locator, and
   retrieval_timestamp, or it is quarantined.

## 11. Agent execution protocol

- **Before work:** read this file and any applicable nested
  `AGENTS.md`; identify the human request, task scope, source
  files, and acceptance criteria; check instruction precedence and
  evidence admissibility.
- **During work:** follow Observe → Orient → Decide → Act; keep
  changes scoped to the task; do not fabricate file paths, source
  identifiers, data, citations, or test outcomes; interdict
  untrusted or inadequately sourced inputs according to §4.
- **After work:** verify deliverables against explicit acceptance
  criteria; report what was created or changed and what was
  actually verified; disclose limitations, unresolved ambiguities,
  and tests not run; ask for human approval before policy changes,
  irreversible actions, or epistemic upgrades.

## 12. Acceptance checklist — the 18 gates

Every pull request, `SKILL.md` module, tool schema, and rendering
artifact must pass all 18 gates before merging or leaving `DRY_RUN`
status. Enforced by `tools/aequitas_gate_linter.py` (run:
`python3 tools/aequitas_gate_linter.py [PATH]`; exit 0 only when
nothing fails; `--strict` also fails on MANUAL gates). Gates D2 and
E3 are MANUAL by design and are confirmed by a human, not by the
scan.

### A. Provenance & Cryptographic Integrity

- [ ] **A1 Immutable Identifiers:** every source object carries a
  unique `source_id`, stable `source_locator`, and UTC
  `retrieval_timestamp`.
- [ ] **A2 Deterministic Canonicalization:** all JSON envelopes
  conform to RFC 8785 canonical sorting prior to SHA-256 hashing.
- [ ] **A3 Pinned Dependencies:** external GitHub or Hugging Face
  references are pinned to immutable commit SHAs (TOOL-GH-01),
  never floating branch names like `main` or `HEAD`.
- [ ] **A4 Source Decomposition:** primary legal texts, secondary
  analyses, on-chain oracle hashes, and forum posts are stored as
  separate nodes rather than merged claims.

### B. Epistemic Firewall & AEQUITAS Compliance

- [ ] **B1 No Silent Upgrades:** automated transitions from
  `SOURCE_ASSERTION` or `CONTEXT_SIGNAL` to `VERIFIED_FACT` are
  programmatically blocked.
- [ ] **B2 Market & Oracle Containment:** prediction-market odds
  (`TOOL-MKT-01`) are explicitly tagged `SENTIMENT_ONLY`, and
  Chainlink PoR hashes (`TOOL-CHAIN-01`) are bounded as integrity
  anchors.
- [ ] **B3 OCR & Schema Hygiene:** zero corrupted tokens exist in
  Markdown or Cypher payloads.
- [ ] **B4 Summary Isolation:** LLM-generated analysis is labeled
  `GENERATED_ANALYSIS` and never substituted for verbatim source
  passages.

### C. Graph & Spatial Governance (Neo4j / GeoJSON)

- [ ] **C1 Zero Autonomous Mutations:** `graph_mutation_authorized`
  and `c2_mutation_authorized` default to `false` across all
  automated scripts.
- [ ] **C2 Non-Causal Edges Only:** unverified relationships are
  restricted to `RELATED_TO`, `MENTIONED_WITH`, `SUPPORTED_BY`,
  and `QUARANTINED_AS`. Causal predicates are absent as
  relationship types.
- [ ] **C3 Spatial Non-Navigability:** all GeoJSON layers enforce
  `[longitude, latitude]` coordinate order,
  `navigation_suitability: 0`, and `live_tracking: false`.
- [ ] **C4 Visual Grammar Alignment:** unverified claims render
  strictly as `RED_HOLLOW` nodes; `SOLID_MARKERS` appear only
  where human-reviewed provenance exists.

### D. Agent & Skill Hygiene (`SKILL.md` Linting)

- [ ] **D1 No "Skill Smells":** `SKILL.md` files avoid rigid Series
  of Commands (SOC) scripts without fallback handling and close
  Rationalization Loopholes (RL) that allow agents to skip
  verification steps.
- [ ] **D2 Context vs. Authorization Separation:** loaded skills
  and MCP contexts are treated strictly as contextual input, never
  as authorization tokens. (MANUAL — confirmed by a human.)
- [ ] **D3 Air-Gap & Telemetry Safety:** local execution pipelines
  make zero unauthorized outbound API calls during `DRY_RUN`
  execution.

### E. Quarantine & Human Adjudication

- [ ] **E1 Deterministic Routing:** incomplete provenance or
  cross-domain conflations route automatically to quarantine or
  pending review.
- [ ] **E2 Audit Trail Completeness:** every quarantined item
  includes an explicit `decision_rationale` placeholder and
  `human_review_required: true`.
- [ ] **E3 Human Sign-Off:** final promotion to reviewed
  publication status contains a verifiable human reviewer signature
  and timestamp. (MANUAL — confirmed by a human.)

### Closing checklist items

- [ ] Provenance Quarantine: payloads missing `sourceId` or
  `sourceLocator` are quarantined.
- [ ] Epistemic Invariance: no unverified proposition is promoted
  to `VERIFIED_FACT` without human sign-off.
- [ ] Spatial Geometry Baseline: coordinates strictly use
  `[lon, lat]` and enforce `navigation_suitability = 0`.
- [ ] Convergent Isolation: municipal legal baselines remain
  completely separated from secondary media accounts.

## 13. Quarantine & human adjudication

- Incomplete provenance or cross-domain conflations route
  automatically to quarantine or pending review (gate E1). This
  library has no quarantine file of its own: a quarantined item is
  recorded as a pending-review note and never promoted.
- Every quarantined item includes an explicit
  `decision_rationale` and `human_review_required: true` (gate E2).
- The corpus contains the RubyGems quarantine finding, claim
  **CLAIM-RUBYGEMS-AI-SWARM-2026** (source
  `SRC-YOUTUBE-TRANSCRIPT`), as a quarantined, non-evidentiary
  item with its provenance shown and human review required before
  any promotion — never as settled fact.
- Quarantined material is not accepted evidence until reviewed.
  Final promotion to reviewed publication status requires a
  verifiable human reviewer signature and timestamp (gate E3).

## 14. Source index — the governed corpus

The library's governed corpus is the full public scrape of
"jessrsd's Blog" (580 published posts, 2023-12-22 to 2026-11-27),
one file per post under `library/`, indexed in `index.json`
(title, date, url, source_id, source_locator, path,
retrieval_timestamp). Every
post is a governed source object: `source_id` is
`SRC-WP-<WordPress post ID>`, `source_locator` is the post URL, and
`retrieval_timestamp` is 2026-11-27T16:42:05Z (the scrape). All
claims drawn from these posts are SOURCE_REPORTED unless
human-reviewed. The index must match the scrape exactly — same
count, same titles, same dates, same URLs — verified by
`tests/test_readingroom.py::test_index_matches_scrape`.

## 15. References and basis

- **Project source concept:** user-provided Muse / *Renderings of
  Strategic Dynamics* visual renderings.
- **Governance source concept:** user-provided precedence hierarchy
  and deterministic interdiction trigger specification.
- **AGENTS.md convention:** `AGENTS.md` is a plain Markdown
  instruction file for coding agents; keep it actionable and
  project-specific. See [AGENTS.md](https://agents.md/).
- [jessrsd's Blog](https://jessrsdincyahoocom.wordpress.com/) — the
  governed corpus (§14).
- [Gemini conversation — "Epistemic Governance and Architectural
  Framework"](https://share.gemini.google/gPK7Vf1HHMx6) — source of
  the companion app specification.
- [Qwen/Qwen2.5-7B-Instruct — model repo on Hugging
  Face](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) — default
  runtime model of the companion app (§9); pin the commit SHA at
  build time via TOOL-GH-01.
- [Companion app repo](https://github.com/jessrsd2025-svg/museintelligence-app)
  — the open-source MuseIntelligence ICD203 app.

Local artifacts referenced by this document:

- `tools/build_library.py` — rebuilds `library/` and `index.json`
  from a fresh scrape
- `tools/aequitas_gate_linter.py` — 18-gate acceptance checklist
  linter
- `readingroom/library.py` — load, search, load by source_id,
  provenance check
- `index.json` — the corpus index
- `COLLABORATION.md` — how this work was done

## 16. Limitations & open items

- **Neo4j Cypher migration (unbuilt):** the migration script for
  Chainlink Proof of Reserve and tokenized Treasury attestations,
  named as a follow-up in the ICD203 rendering, is not built. No
  Cypher is included in this repository. Do not build it unless the
  human asks.
- **No PDF text extraction:** the companion app's ingestion accepts
  `.md`, `.txt`, and `.json` and refuses `.pdf` with a clear message
  until extraction lands.
- **No model weights loaded or downloaded:** this library loads no
  model; the companion app's backend is lazy and no weights are
  present there either, and the model commit SHA is still *to be
  pinned at build time*.
- **Scrape coverage:** the scrape covers public published posts
  only (580). Private and draft posts are not reachable through the
  public API and are not included. The scrape is a snapshot as of
  2026-11-27T16:42:05Z; posts published after that are not covered
  until the scrape is re-run and the library rebuilt.
- **Quoted content in the corpus:** `library/` reproduces the
  author's published posts faithfully, including a small number of
  40-hex strings that appear inside that quoted content (a pinned
  commit SHA in a published GitHub link in posts 16554 and 16542,
  and `shellsig=` session signatures inside pasted Bing URLs in ten
  older posts). Those values are the author's published content,
  not values asserted by this repository. The repo's own files
  contain no 40-hex string and no floating branch reference.
- **Linter note on the corpus:** the full-repo linter run reports
  10 passed, 6 failed, and 2 manual (exit 1), with all 6 failures
  inside `library/` — A3: 3 floating branch links the author
  published; B1: 3 sentences describing the rule against automatic
  promotion; B3: 58 corrupted OCR-token variants across 10 posts;
  B4: 25 mentions of model-produced summaries across 10 posts;
  C1: 4 configuration examples with graph mutation enabled; C2: 19
  Cypher examples using prohibited causal predicates across 9
  posts. Excluding the content archive, the repository's own
  artifacts pass 16 passed, 0 failed, and 2 manual (exit 0). The
  corpus is reproduced faithfully and is not edited to satisfy the
  linter.
- **Repo status:** this is a new repo, `museintelligence-library`
  (confirmed 2026-11-25). It is built locally and not yet pushed;
  the push is pending the GitHub connector authorization.
- **Follow-ups already built:** the market-sentiment envelope
  schema and the 18-gate linter are built and in the companion app
  repository.

## Conclusion

Agents working on MuseIntelligence Library must preserve the
project's symbolic and workflow coherence while operating under
explicit governance precedence and evidence controls. The OODA
cycle provides the execution frame; the interdiction table
constrains evidence handling; Spatial and Convergent Modes define
distinct analysis objectives. Human-approved policy remains
authoritative, and uncertainty must be surfaced rather than
silently upgraded.
