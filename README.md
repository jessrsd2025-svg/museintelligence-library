# MuseIntelligence Library

A source-code library of the full public scrape of "jessrsd's Blog" —
580 published posts (2023-12-22 to 2026-11-27) as individual markdown
files, with a Python package to load, search, and check them. Every
file carries its provenance: source_id, source_locator (the post
URL), and retrieval_timestamp.

Companion open-source app repo: https://github.com/jessrsd2025-svg/museintelligence-app
— the MuseIntelligence ICD203 reading-room and governance app
(Qwen/Qwen2.5-7B-Instruct, Apache 2.0). This library is the corpus
that app governs.

## What is in here

- `library/` — 580 posts, one file per post, organized by year and
  month: `library/<year>/<month>/<post-id>-<slug>.md`. YAML
  front-matter on every file.
- `index.json` — the index: title, date, url, source_id,
  source_locator, path, and retrieval_timestamp for all 580 posts.
- `readingroom/` — a standard-library Python package: load the
  index, search by keyword/title/date range, load a post by
  source_id, and run the provenance check. CLI included.
- `tools/build_library.py` — rebuilds `library/` and `index.json`
  from a fresh scrape.
- `tools/aequitas_gate_linter.py` — the 18-gate acceptance
  checklist, vendored from the app repo.
- `tests/` — the unittest suite (11 tests).
- `COLLABORATION.md` — how this work was done across Jesse's
  Android phone, ChatGPT, Gemini, Google AI Studio, and the
  open-source model on GitHub.
- `AGENTS.md` — governance for agents working in this repo.
- `MODEL_CONTEXT_PROTOCOL.md` — the MuseIntelligence "Model Context Protocol" for this library: how models and agents access this source-code library, written for Google compliance (GCP Section 17; Workspace AI Tools Addendum).

## Quickstart

Python 3.10+; the core runs on the standard library alone.

```sh
# How many posts are indexed
python3 -m readingroom --count

# Search by keyword, with a date range
python3 -m readingroom --search ICD203 --from 2026-11-20 --to 2026-11-25

# Read one post by source_id
python3 -m readingroom --show SRC-WP-18250

# Check provenance across the index and the files
python3 -m readingroom --check

# Run the tests
python3 -m unittest discover -s tests -v
```

## How it was built

- **Source:** the public WordPress.com REST API scrape of
  jessrsdincyahoocom.wordpress.com, 2026-11-27T16:42:05Z, 580
  published posts. Public published posts only; private and draft
  posts are not reachable through that API and are not included.
- **Build:** `python3 tools/build_library.py` parses the scrape (the
  index table and the post sections, cross-checked against each
  other) and writes the files. Re-run on a fresh scrape to update.
- **Content is reproduced faithfully:** no post was added, edited,
  or removed. The 4 posts with empty titles in WordPress are filed
  as "(untitled — post \<id\>)" with their post id; their slugs are
  the post ids, so those filenames read e.g. `16476-16476.md`.
- **Provenance:** every file and every index entry carries a
  source_id (`SRC-WP-<post id>`), a source_locator (the post URL),
  and a retrieval_timestamp (`2026-11-25T18:01:10Z`). Nothing in
  this repo is VERIFIED_FACT; all claims are SOURCE_REPORTED unless
  a human has reviewed the source. No claim is promoted to
  VERIFIED_FACT without human review.

## Repo status

- This is a new repo, **museintelligence-library** (confirmed
  2026-11-25). It is built locally and not yet pushed; the push is
  pending the GitHub connector authorization.
- Companion app repo: https://github.com/jessrsd2025-svg/museintelligence-app
  (public, created 2026-11-25).

## Limits

- **Snapshot of 2026-11-25:** posts published after that date are
  not included until the scrape is re-run and the library rebuilt.
- **Read-only archive:** the library does not re-assert the posts'
  claims as fact. It does not cover the Neo4j migration (unbuilt)
  or PDF text extraction.
- **Linter:** the full-repo linter run flags quoted content inside
  `library/` (the posts' own words), so the gates workflow excludes
  `library/`; the repo's own artifacts pass 16 passed, 0 failed,
  and 2 manual. See AGENTS.md §16 for the exact counts.
- **Compliance:** `MODEL_CONTEXT_PROTOCOL.md` states how models and
  agents access this library. Access is local (index +
  `readingroom` package); no Google API, MCP server, or Workspace
  API is used to reach it.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
