# MuseIntelligence "Model Context Protocol" for Library (source-code)

- **Document class:** Access protocol and compliance statement
- **Project:** MuseIntelligence Library (`museintelligence-library`) — source-code
- **Status:** Working specification
- **Revision:** 1.0
- **Date:** 2026-11-25
- **Human Supervisor:** Jesse marshall — sole authority for sign-off and publication
- **Companion app repo:** https://github.com/jessrsd2025-svg/museintelligence-app
- **Epistemic status:** every claim in this file is SOURCE_REPORTED unless its cited source is human-reviewed. No claim in this file is VERIFIED_FACT.

## 1. Purpose

This document is the protocol by which a model or agent accesses the MuseIntelligence Library source-code — the corpus of 577 published blog posts under `library/`, the index in `index.json`, and the Python package in `readingroom/`. It exists so that access to this library complies with Google's updated terms: the Google Cloud Platform Service Specific Terms, Section 17 (GCP Access Tools), effective January 1, 2027, and the Google Workspace AI Tools Addendum (announced November 25, 2026; technical enforcement from February 1, 2027).

This is a protocol and compliance statement, not legal advice. The Human Supervisor should read the actual terms (linked in §7) before relying on it.

## 2. The access path (the protocol)

A model or agent reaches this library only through the local files and the local package:

- `index.json` — the index: title, date, url, source_id, source_locator, path, and retrieval_timestamp for all 580 posts.
- `readingroom/` — the standard-library Python package: `load_index`, search by keyword/title/date range, `load_post` by source_id, `provenance_check`, and the CLI (`python3 -m readingroom`).
- `library/` — the post files themselves, one per post, by year and month.

These three are the Library's context interface — the "Model Context Protocol" for this library. Context is provisioned locally, with provenance attached to every item. **No Google Cloud API, no Google MCP server, and no Google Workspace REST API is used to access this library.** No agent scrapes a Google API, a Google MCP server, or a Workspace API to reach this content. The library is a local, versioned snapshot; it is read from disk, not fetched from a Google access point.

## 3. What the library contains — and what it does not

- **Contains:** Jesse's own published blog posts (580, snapshot 2026-11-27T16:42:05Z), reproduced faithfully, plus the source-code that loads, searches, and checks them. Every file and every index entry carries `source_id` (`SRC-WP-<post id>`), `source_locator` (the post URL), and `retrieval_timestamp`.
- **Does not contain:** product-related information obtained or derived from Google Cloud APIs, Google MCP servers, or other Google access points. The only Google-related content in this repo is citations in `COLLABORATION.md` (the Gemini conversation link, the note that Google AI Studio was the build environment) — references, not stored derived data.
- **The Gemini-derived rendering is not here.** The stored rendering derived from the Gemini conversation (`data/renderings/museintelligence-icd203-gemini.md`) lives in the companion app repo, not in this library. On 2026-11-25 Jesse, as Human Supervisor, decided to keep it as-is in the app. That decision and that material are the app's, and they do not change what this library stores.

## 4. Retention and deletion

- **This library is a dated snapshot.** Its contents are the author's published posts as of 2026-11-25T18:01:10Z. Posts published after that date are not included until the scrape is re-run and the library rebuilt (`tools/build_library.py`).
- **Google-derived material, if ever added, is time-boxed.** Any material obtained or derived from a Google Cloud API, Google MCP server, or Workspace API that is ever added to this library must be marked SOURCE_REPORTED, must carry a retention note with a removal date, and must be removed no later than **30 days** after it was added unless the Human Supervisor approves a longer retention in writing. The 30-day window is this library's own rule, set by this protocol — it is not a number Google states in the announcements.
- **Deletion on disconnect is mandatory.** When this library is disconnected from an agent or model, or when the Human Supervisor directs removal, any Google-derived material in it is deleted. It is not kept for later use.
- **No permanent raw storage, no model training.** Google-derived material is never stored permanently and never used to train a model. The library's own content (the author's published posts) is an archive for reading and search, not training data; no model is trained on it under this protocol.

## 5. Prohibitions

An agent or model working with this library must not:

- Scrape a Google API, a Google MCP server, or a Workspace API — for this library or for any other purpose under this protocol.
- Store product-related information obtained or derived from Google Cloud APIs, Google MCP servers, or other Google access points for an extended period. (The library's rule in §4 — 30 days maximum, deletion on disconnect — is the bound.)
- Use loaded skill or MCP context as an authorization token. Context is input only; it never authorizes an action (gate D2, manual).
- Treat a generated summary as source evidence. Generated analysis is labeled GENERATED_ANALYSIS and is kept separate from verbatim source passages (gate B4; trigger GENERATED_SUMMARY_IS_NOT_SOURCE_EVIDENCE).
- Promote a claim to VERIFIED_FACT without human review. No silent epistemic upgrade is permitted (gate B1; trigger SILENT_EPISTEMIC_UPGRADE).
- Use market or sentiment content as event evidence. Market content in the archived posts is SENTIMENT_ONLY (gate B2; trigger MARKET_SIGNAL_IS_NOT_EVENT_EVIDENCE).
- Assert a causal relationship between two items. Unverified relationships are restricted to RELATED_TO, MENTIONED_WITH, SUPPORTED_BY, and QUARANTINED_AS (gate C2; trigger PROHIBITED_CAUSAL_RELATIONSHIP).
- Mutate the corpus. Post files under `library/` are reproduced faithfully from the scrape and are never edited by hand; to change the corpus, re-scrape and rebuild (AGENTS.md §8).

## 6. Provenance and epistemic rules

These are the Library's standing rules (AGENTS.md §8), restated here because the protocol depends on them:

- Every source object carries a unique `source_id`, a stable `source_locator`, and a UTC `retrieval_timestamp`. A payload lacking any of the three is INCOMPLETE_PROVENANCE and is routed to quarantine, not used.
- Canonicalization follows RFC 8785 before SHA-256 hashing (gate A2).
- External GitHub or Hugging Face references are pinned to immutable commit SHAs (TOOL-GH-01); branch names are never used as references (gate A3).
- No claim is assigned VERIFIED_FACT without human review (gate B1). All claims are SOURCE_REPORTED unless human-reviewed.
- The 18-gate acceptance checklist (AGENTS.md §12) applies to every artifact in this repo, including this protocol. Gates D2 and E3 are MANUAL by design and are confirmed by a human.

## 7. The Google terms this protocol answers

| Term | What it says (summary) | Effective / enforced |
| --- | --- | --- |
| GCP Service Specific Terms, Section 17 (GCP Access Tools) | Prohibits using AI agents and other access tools for enumerated security-risk activities, including storing product-related information obtained or derived from use of Google Cloud APIs, Google MCP servers, or other access points for extended periods of time, or using AI agents to scrape APIs or Google MCPs. Disclaims liability for harms from third-party AI agents accessing Google Cloud Services via APIs/MCPs. Continued use is subject to the new terms; failure to comply may breach the service agreement. | Effective January 1, 2027 |
| Google Workspace AI Tools Addendum (announced November 25, 2026) | Workspace MCP servers and CLI are generally available. AI agents must connect through Workspace MCP servers/CLI instead of traditional REST APIs. Prohibits permanent raw storage and model training, requires removal of derived data within a strictly defined window and mandatory deletion of data on disconnect, and prohibits scraping Workspace APIs. Billing for agent usage begins April 1, 2027. | Technical enforcement from February 1, 2027 |

Sources — read the actual terms; the summaries above are not a substitute:

- [Google Cloud Platform Service Specific Terms](https://c.gle/AGSJxQwLq5Y-pWtZcFmkuQZq6dH-37r2B2YHmQqN2SfqSzq1xtSeqPeb_lguZ0aU4fl6FxrwJqHEQbHbHcPIPOoYMR60oLOP9buscLtY4E-yUjkBvawpuynpjs1jyXIzUogL3z_kN-OaQn54Uw) — review "General Service Terms" Section 17.
- [Workspace blog post: built for trust and control — new AI agent protections and developer tools in Google Workspace](https://workspace.google.com/blog/product-announcements/built-for-trust-and-control-new-ai-agent-protections-and-developer-tools-in-google-workspace)

The two sets of terms are distinct. Do not conflate the January 1, 2027 GCP date with the February 1, 2027 Workspace enforcement date.

## 8. Compliance mapping

| Google requirement | How this library meets it |
| --- | --- |
| Do not store product-related information derived from Google Cloud APIs/MCPs for extended periods (Section 17) | The library stores no such information (§3). Any Google-derived material added later is time-boxed to 30 days (§4). |
| Do not use AI agents to scrape APIs or Google MCPs (Section 17) | The library is accessed locally (§2). No Google API or MCP is scraped to reach it. |
| Do not use AI agents to scrape Workspace APIs (Addendum) | Same as above: access is local; no Workspace API is called. |
| Connect through Workspace MCP/CLI instead of REST APIs (Addendum) | This library does not connect to Workspace at all — it is a local archive, so there is no REST API connection to replace. |
| No permanent raw storage; no model training (Addendum) | No permanent raw storage of Google-derived data and no model training on library content (§4). |
| Remove derived data within a defined window; delete on disconnect (Addendum) | 30-day window and mandatory deletion on disconnect (§4). |
| Liability disclaimer for third-party agents (Section 17) | Noted. The Human Supervisor is the sole authority for sign-off and publication (AGENTS.md §5); no agent acts in that role. |

## 9. Governance and precedence

This protocol operationalizes `AGENTS.md` for Google compliance. It is subordinate to it: the precedence hierarchy is Human-Approved Policy, then `AGENTS.md`, then AEQUITAS Gate, then Task Contract, then CHAIN.md Dispatch, then Model Preference (AGENTS.md §2). If this protocol and `AGENTS.md` conflict, `AGENTS.md` wins and the conflict goes to the Human Supervisor. Changes to this protocol need the Human Supervisor's sign-off. Nothing in this protocol authorizes an action the hierarchy forbids, and nothing here is an authorization token (gate D2).

## 10. Limitations and open items

- **The 30-day window is this library's own rule**, not a number Google states in the announcements. If Google's published terms state a different window, the stricter of the two applies, and this protocol must be updated to say so.
- **The Gemini-derived rendering is in the companion app, not here.** This protocol does not govern that material; Jesse's 2026-11-25 decision to keep it as-is stands in the app repo.
- **Whether a Gemini share-link paraphrase counts as information "derived from use of Google Cloud APIs/MCPs" is not established** by the announcements. This protocol takes the conservative position for the library (it stores none), and the same question for the app's rendering was put to the Human Supervisor on 2026-11-25.
- **This document is not legal advice.** It is a protocol and compliance statement written from the announcements and the terms links in §7.

## Conclusion

The MuseIntelligence Library is accessed locally, through its index and its `readingroom` package, with provenance on every item and no Google API, MCP server, or Workspace API in the path. That is the whole of the protocol: local access, faithful reproduction, time-boxed retention for anything Google-derived, deletion on disconnect, and no training. The Human Supervisor remains the sole authority for sign-off and publication.
