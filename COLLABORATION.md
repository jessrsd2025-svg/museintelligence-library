# COLLABORATION.md — how this work was done

- **Document class:** Collaboration record
- **Project:** MuseIntelligence Library (`museintelligence-library`)
  and the companion app (`museintelligence-app`)
- **Status:** Working record
- **Sources:**
  - `SRC-WP-SCRAPE-2026-11-27` — the full public scrape of
    jessrsdincyahoocom.wordpress.com (580 published posts) —
    retrieved 2026-11-27T16:42:05Z — human-reviewed: no
    (re-scrape; supersedes the 2026-11-25 snapshot of 577 posts)
  - `SRC-ICD203-RENDERING-2026-11-23` — the ICD203 rendering —
    retrieved 2026-11-23 — human-reviewed: no
  - `SRC-ICD203-GEMINI-SPEC-2026-11-25` — the ICD203 Gemini
    app-creation specification — retrieved 2026-11-25T14:50:07Z —
    human-reviewed: no
  - `SRC-AILA-RENDERING-2026-11-24` — the AILA rendering, built from
    arXiv v2 — retrieved 2026-11-24 — human-reviewed: no
- **Epistemic status:** every claim in this file is SOURCE_REPORTED
  unless its cited source is human-reviewed. No claim in this file
  is VERIFIED_FACT.

## Who did what

| Participant | Role |
| --- | --- |
| Jesse marshall (human supervisor) | Directed the work, reviewed the results, signed in to the accounts, and took over the browser when a sign-in needed him. Sole authority for epistemic promotions and for publishing. |
| Muse (the agent) | Built the renderings, the schemas, the linter, the app, the scrape, the AGENTS.md files, and this library. |
| ChatGPT | Supplied the AILA research paper through its library share, and one thread that could not reach the Gemini conversation. |
| Gemini | Produced a paraphrase of the ICD203 document in the shared conversation that became the app specification. |
| Google AI Studio | The build environment the app-creation specification was written for (Gemini Build mode). |
| Open-source model on GitHub | Qwen/Qwen2.5-7B-Instruct (Apache 2.0), the app's runtime model, in the companion repo https://github.com/jessrsd2025-svg/museintelligence-app |

## Where the work happened

Jesse directed the work from his Android phone — a Samsung Galaxy
A16 5G (model SM-S166V) — sending short messages from the Android
app and taking over the live browser when a sign-in needed his
hands: entering the WordPress password himself for the first publish,
signing in to GitHub with "Continue with Google" and completing
device verification, and confirming the library as a new repo. The
files were built on this machine and the posts were published to his
WordPress blog, "jessrsd's Blog" at
jessrsdincyahoocom.wordpress.com.

## Timeline

| Date | What happened |
| --- | --- |
| 2026-10-01 | Onboarding: Jesse chose the name "Muse" for the agent; Gmail was connected. |
| 2026-11-12 | Jesse shared a Google Doc, "2025 Year in Review US Crypto Policy Tracker". Google Docs was not connected, so the document was never opened that way. |
| 2026-11-17 | Jesse uploaded the PDF of the same document (25 pages); `renderings.md` was built from it as a markdown wiki/index. |
| 2026-11-20 | A browsable wiki page (`renderings-wiki.html`) was built from `renderings.md`, with a map of the D.C. regulatory corridor plotted from the document's coordinates. |
| 2026-11-23 | Jesse uploaded the "MuseIntelligence ICD203 Unmanned_News ReadingRoom" PDF (36 pages, created Nov 19, 2026); a rendering and a browsable wiki page were built from it. The same day he shared a Gemini conversation, "Epistemic Governance and Architectural Framework" (created 11:56 AM), in which Gemini had produced a paraphrase of the ICD203 document. The market-sentiment schema and the 18-gate linter were built. |
| 2026-11-24 | Jesse shared a ChatGPT library link holding "Arxiv Papers.pdf" — the paper "Adaptive Integrated Layered Attention (AILA)", arXiv:2503.22742v2. A rendering and a wiki page were built from the arXiv v2 text, with the forecasting numbers checked against the paper: AILA-1 leads forecasting on four of five assets, and the LSTM wins S&P 500. A second ChatGPT link ("Analyze Gemini Conversation") was read the same day; ChatGPT's single reply said it could not access the Gemini link, so no analysis of the ICD203 content was produced there. |
| 2026-11-25 | The ICD203 Gemini app-creation specification (Renderings.md for Google AI Studio) and the TOOL-GH-01 GitHub calls were built, then published as WordPress post 18250. Jesse edited that post himself (8 revisions). The MuseIntelligence ICD203 app repo was built, the existing GitHub account was found (username `jessrsd2025-svg`, signed in via "Continue with Google"), and a public repo named `museintelligence-app` was created. The whole blog was scraped (577 published posts) and an AGENTS.md was built from it. This library was built from that scrape. |

## How each tool contributed

- **ChatGPT** — the AILA paper arrived through a ChatGPT library
  share on 2026-11-24. The rendering was built from the arXiv v2
  full text (not from the library PDF itself, which was viewed in
  the browser, not downloaded), and the forecasting numbers were
  checked against the paper's own tables: AILA-1 lowest on Gold
  (475.63), US Dollar Futures (2.85), Coffee (1,927.13) and Wheat
  (1,536.50); LSTM lowest on S&P 500 (215,838.19). The second
  ChatGPT thread contributed nothing: ChatGPT could not reach the
  Gemini link and asked for the conversation to be pasted instead.
- **Gemini** — the conversation "Epistemic Governance and
  Architectural Framework" (created 2026-11-23 11:56 AM,
  https://share.gemini.google/gPK7Vf1HHMx6) is the source of the
  app specification: the six-tier governance hierarchy, the six
  interdiction triggers, the OBSERVE panel tools, and the OODA
  loop. The material in the specification is a paraphrase of that
  conversation, labeled GENERATED_ANALYSIS, never Gemini's verbatim
  wording, and every Gemini-derived claim is SOURCE_REPORTED.
- **Google AI Studio** — the build environment the app-creation
  specification was written for (Gemini Build mode). It is the
  build environment only; it is not the app's runtime model. Muse
  has no Gemini / Google AI Studio API connection, so the
  specification was written directly, with no Gemini model call.
- **Open-source model on GitHub** — the app's runtime model is
  Qwen/Qwen2.5-7B-Instruct: instruction-tuned 7B open weights
  (7.61B parameters, 131,072-token context, Apache License 2.0,
  ungated on Hugging Face), verified to exist on Hugging Face
  2026-11-25. It is the reasoning engine only; it never assigns
  VERIFIED_FACT. Its commit SHA is to be pinned at build time via
  the TOOL-GH-01 flow — no SHA was invented. The companion app
  repo is https://github.com/jessrsd2025-svg/museintelligence-app
  (public, created 2026-11-25, by the signed-in account
  `jessrsd2025-svg`).
- **Jesse's Android phone** — the directives arrived as short
  messages from the Android app, including "GitHub is ready, try
  now" and the instruction to build this library. Jesse took over
  the browser to sign in to GitHub and to confirm the library as a
  new repo named `museintelligence-library`.

## Notes and open questions

- **The invite code.** On 2026-11-25 Jesse shared a code for 1
  billion tokens and asked for it to be redeemed. It was
  identified as a Muse invite/referral code, redeemable only
  within 48 hours of creating a Muse account (per third-party
  guides, not officially confirmed), so it almost certainly cannot
  be redeemed on his account, which dates to early October 2026.
  Jesse reports the code came from Muse, he thinks the same day
  the crypto-tracker `renderings.md` was done (2026-11-17); the
  record was checked and no code shared in chat that day was
  found — most likely it is the invite code from his own Muse
  account (shown in his Muse Settings), which he can share with
  new users. Nothing was redeemed. (SOURCE_REPORTED.)
- **The library's completion step.** Jesse's message commissioning
  this library was cut off at "When comple...", so the completion
  step is unconfirmed. The repo name was confirmed on 2026-11-25
  as a new repo, `museintelligence-library` (not an addition to
  `museintelligence-app`). The push is still blocked on Jesse's
  GitHub connector authorization. (SOURCE_REPORTED.)
- **The GitHub link in the blog.** When the GitHub publish is
  finished, the link to the MuseIntelligence open-source app is to
  be included in the blog's most recent Renderings.md post
  ("Renderings of Strategic Dynamics", post 18250). That step is
  pending the push. (SOURCE_REPORTED.)

## Limits

- This record covers the collaboration up to 2026-11-25. Later
  work needs its own entry.
- Dates and events are as recorded in the chat, the renderings,
  and the app repo. Where the record is silent, this file says so
  rather than filling the gap.
