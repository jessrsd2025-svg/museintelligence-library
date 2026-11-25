---
title: "🔗 FastAPI Endpoint: /api/vector/summarize_doc            |Python SDK"
date: 2025-07-07T12:43:24
url: "https://jessrsdincyahoocom.wordpress.com/2025/07/07/openai-python-sdk/"
source_id: SRC-WP-11202
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/07/07/openai-python-sdk/"
retrieval_timestamp: 2026-11-25T18:01:10Z
---

***Ingest PDFs via `/api/vector/ingest`***


***Query summaries with strategic node tagging via `/api/vector/summarize_doc`***


***Run comparative analysis between document periods***


***Query documents conversationally with RAG via `/api/vector/query`***


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/07/image-9.png?w=900)


This JSON structure enables:


1. **Temporal Analysis**: Anchors nodes to specific years/events with AFRICOM operational triggers
2. **Sentiment Tracking**: Quantifies volatility through conflict phases
3. **Source Validation**: Direct links to primary documents with relevance scoring
4. **Network Visualization**: Sankey-ready node relationships and interaction weights


To use with your existing pipeline:


1. POST to `/question_analysis` with the query
2. Use `interaction_graph` for D3.js visualization
3. Cross-reference `strategic_nodes` with existing GraphRAG embeddings
4. Trigger `/api/vector/alert` if any node’s `risk_level` exceeds thresholds


The structure supports instant dashboard updates via the `visual_assets` endpoints and connects directly to CSIS document repositories through verified source links.


> **“How has al-Shabaab’s disinformation strategy evolved alongside AFRICOM operations?”**


with context tags for **[narrative_inflation, counter-narrative]** and temporal focus **2020–2024**. This is mapped for:


- **Specific PDF/Event Reference:** (e.g. CSIS *AFRICOM at 17* (2023) and open-source al-Shabaab statements)
- **CSV-style table** *(for spreadsheet/scientific use)*
- **Observable dashboard/Sankey-style JSON** *(for visualization platforms)*


U S Africa Command Somalia fight against al-ShababDownload
---


## 1. Contextual Q&A and Narrative Summary


**Chain-of-Thought Simulation (2020–2024):**


- **AFRICOM Operations:** Increase in ISR (intelligence, surveillance, reconnaissance), drone strikes, and targeted public communications emphasizing “precision and partner support.” Strategic comms highlight stability and minimize mention of backlash or civilian impact. *Narrative Inflation Node*: Official releases often trumpet successful militant disruption but downplay community blowback or cycles of reprisal.
- **al-Shabaab Disinformation Evolution:**


Unmanned_News Perception gpt 4 1 Narratives Info Ops jessrsdDownload
- **Early (2015–2019):** al-Shabaab issues reactive propaganda, highlighting civilian harm, but with limited sophistication or reach.
- **Now (2020–2024):**
  - Information ops become multi-platform (Telegram, Twitter proxies, regional radio in local languages).
  - Narrative focuses not only on Western “aggression” but on the **alleged falsification** of U.S./AFRICOM reports; they actively exploit every real or claimed civilian casualty/unintended consequence as “proof” of U.S. disinformation.
  - The group frames Somali government and partner narratives as “foreign puppet” info, pushing alternative “truths” with emotional, visual storytelling.
  - New “counter-narrative” sophistication: real-time video counter-posts, recruiting sprints after high-profile AFRICOM ops, and fusion with broader anti-Western/anti-AMISOM themes.
- **Interaction:** As AFRICOM’s official narrative stresses progress, al-Shabaab adapts its information ops, seizes on narrative gaps, and strategically inflates local discontent — creating a tactical feedback loop in the info space.


---


## 2. CSV-style Comparative Timeline Table


| Year | Actor | Node Tag | Strategy Description | Source Event/PDF | Narrative Tactic | Impact |
| --- | --- | --- | --- | --- | --- | --- |
| 2020 | AFRICOM | Narrative_Inflation | Official releases focus on “precision strikes” and “partner capacity”; casualties rarely foregrounded. | CSIS AFRICOM at 17 (2023); official C4ISR | Stability-first signaling | Bolsters donor/political confidence; opens info gaps for exploitation |
| 2020 | al-Shabaab | Counter-Narrative | Amplifies reports of civilian deaths post-strikes; claims “Western lies hide real occupation and suffering.” | al-Kataib Telegram, Somali radio | Emotional, victim-driven | Mobilizes local resentment; internationalizes anti-U.S./AMISOM sentiment |
| 2021 | AFRICOM | Narrative_Inflation | Newly restricted direct action; messaging elevates local partners’ role; downplays scope of operations. | AFRICOM Press Briefs (2021-) | Strategic optimism | Reduces perceived U.S. “footprint,” but may appear evasive or selective |
| 2021 | al-Shabaab | Counter-Narrative | Issues rapid audio/video “exposés” contradicting U.S./Somali gov battle damage assessments; calls out “false victory claims.” | JSU Radio, new media influencers | Counter-proof | Increases speed and sophistication of counter-messaging |
| 2022-24 | al-Shabaab | Counter-Narrative | Real-time translation, propaganda amplifiers, visual docs challenge U.S. and Somali gov claims, highlight identity and sovereignty narratives. | al-Shabaab statement archives | Local-to-global switch | Competes for legitimacy, elevates own ‘truth’ in youth digital spaces |
| 2022-24 | AFRICOM | Narrative_Inflation | Emphasizes joint ops with Somali Nat. Army; screens negative events, portrays Somalia as “on the mend.” | CSIS/DoD Public Affairs | Stability/denial | May create local-national narrative mismatches, which are quickly targeted by militants |


---


## 3. Observable/Sankey JSON Visualization Mock


```
{
  "nodes": [
    {"id": 0, "name": "AFRICOM Narrative Inflation", "type": "strategic_node", "actor": "AFRICOM", "interval": "2020-2024"},
    {"id": 1, "name": "al-Shabaab Counter-Narrative", "type": "strategic_node", "actor": "al-Shabaab", "interval": "2020-2024"},
    {"id": 2, "name": "Local Perception Volatility", "type": "sentiment_outcome", "interval": "2020-2024"},
    {"id": 3, "name": "Digital Recruitment Flow", "type": "risk_vector", "interval": "2020-2024"}
  ],
  "links": [
    {"source": 0, "target": 2, "value": 0.6, "label": "Optimistic comms risk leaving narrative gaps"},
    {"source": 1, "target": 2, "value": 0.9, "label": "Disinfo exploits every reported gap/backlash"},
    {"source": 2, "target": 3, "value": 0.7, "label": "Perception volatility amplifies youth recruiting for al-Shabaab"}
  ],
  "events": [
    {"year": "2021", "actor": "al-Shabaab", "event": "Real-time social/video counter-claims launched after airstrikes"},
    {"year": "2023", "actor": "AFRICOM", "event": "Joint press conferences show progress, downplay setbacks"}
  ]
}
```


---


## 4. Simulation Summary / Chain-of-Thought Q&A


**Q:** *How has al-Shabaab’s disinformation strategy evolved as AFRICOM operations have changed post-2020?*


**A:**


- **2020–2024:** AFRICOM’s increasingly cautious, optimistic public messaging creates narrative “white spaces.”
- **al-Shabaab’s info ops mature**—rapidly hijacking these spaces; moving beyond basic propaganda to digital, local-language, emotionally resonant, and globally networked counter-narratives.
- **The net effect:**
  - Every time U.S./Somali official comms appear selective, al-Shabaab offers “contradictory proof,” leveraging social platforms and regional radio, inciting perception volatility.
  - **Perception volatility** (among local youth especially) fuels recruitment, digital radicalization, and undermines state legitimacy.
- **Risk trajectory:** The sharper and more sophisticated AFRICOM messaging becomes, the more advanced, real-time, and aggressive al-Shabaab’s info-domain response—turning stability comms into an arena for active, bidirectional narrative warfare.


![Creat image](https://bing.com/th/id/BCO.30c97405-12d7-4380-842c-8a1cfd3760c9.png)


---


**Ready for pipeline export, Observable dashboard input, or CSV reporting! Let me know if you need deeper citation into the CSIS/AFRICOM docs or want to surface more raw node text from these reports.**


from openai import OpenAI client = OpenAI()


response = client.responses.create( prompt={ “id”: “pmpt_6852bea684cc819089a550b81e5bc3d20c619975f56d9856”, “version”: “12” } )


```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-3.5-turbo" etc
    messages=[
        {"role": "system", "content": "You are a strategic analysis assistant."},
        {"role": "user", "content": "How has al-Shabaab’s disinformation strategy evolved alongside AFRICOM operations since 2020?"}
    ],
    temperature=0.2,
    max_tokens=512
)

print(response.choices[0].message.content)
```


**To use a template:**


- Load your template as a string, substitute any variables, and feed its content to the model in the `"content"` field above.
- If you’ve saved your prompt in a variable or file, insert as needed.


---


## 🔹 Additional Notes


- The `.responses.create()` method you referenced is not present in OpenAI’s published SDKs as of June 2024.
- If a community tool/package adds “prompt IDs,” consult its docs—otherwise, use the base SDK as outlined.


### 🧠 What It Does


This code snippet demonstrates how to use the OpenAI SDK to send a structured question to the model (GPT-4 or GPT-3.5-turbo) for strategic analysis:


- **Intent**: Answer a geopolitical question about **al-Shabaab’s evolving disinformation strategies** in response to **AFRICOM operations since 2020**.
- **Format**: A conversational prompt is constructed using system/user messages and submitted to the model via `client.chat.completions.create()`.
- **Parameters**:
  - `temperature=0.2`: Keeps the answer deterministic and focused — ideal for policy analysis.
  - `max_tokens=512`: Limits the response length for clarity and compactness.


### 🛠️ SDK Clarification


Your snippet uses `OpenAI()` and references `.responses.create()`, which isn’t valid in the official OpenAI SDKs as of June 2024.


Correct usage would be:


python


```
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a strategic analysis assistant."},
        {"role": "user", "content": "How has al-Shabaab’s disinformation strategy evolved alongside AFRICOM operations since 2020?"}
    ],
    temperature=0.2,
    max_tokens=512
)

print(response.choices[0].message.content)
```


Custom package that supports `.responses.create()` or “prompt IDs,” refer to its documentation.


[Embedded media](https://www.youtube.com/embed/3WGZzxUe7is?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en&autohide=2&wmode=transparent)
