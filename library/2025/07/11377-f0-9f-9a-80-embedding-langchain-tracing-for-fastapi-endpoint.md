---
title: "“langchain_index”🚀 Embedding LangChain Tracing for FastAPI Endpoint🔌 API/Agents Role in Orchestrated Workflow"
date: 2025-07-11T13:48:52
url: "https://jessrsdincyahoocom.wordpress.com/2025/07/11/%f0%9f%9a%80-embedding-langchain-tracing-for-fastapi-endpoint/"
source_id: SRC-WP-11377
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/07/11/%f0%9f%9a%80-embedding-langchain-tracing-for-fastapi-endpoint/"
retrieval_timestamp: 2026-11-27T16:42:05Z
---

Laing Chain API agents role in Orchastrated Workflow_Unmanned_News jessrsd_blogsDownload
![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/07/image-24.png?w=683)


[https://www.linkedin.com/in/flagship3jesse-marshall-2613b94b?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAqPTSkBeQ6WiFBmMkWIndknmbkWgggn0gM](https://www.linkedin.com/in/flagship3jesse-marshall-2613b94b?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAqPTSkBeQ6WiFBmMkWIndknmbkWgggn0gM)[Jesse Marshall Renderings of Strategic Dynamics](https://www.linkedin.com/in/flagship3jesse-marshall-2613b94b?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAqPTSkBeQ6WiFBmMkWIndknmbkWgggn0gM)


> FastAPI Endpoints for GraphRAG🧪 1. Nitazenes: The Dark Horse in Synthetic Opioids

[Embedded media](https://jessrsdincyahoocom.wordpress.com/2025/07/09/fastapi-endpoints-for-graphrag%f0%9f%a7%aa-1-nitazenes-the-dark-horse-in-synthetic-opioids/embed/#?secret=BDlUnFaYnW#?secret=ondp2NYI9O)


🔌 API/Agent Role in Your Orchestrated Workflow – “langchain_index”

API/LLM Agent: Serve as RAG-ready context for legal, policy, or field ops Q&A


[https://python.langchain.com/](https://python.langchain.com/)


![](https://media.licdn.com/dms/image/sync/v2/D4D27AQFTx2Ok8fkasg/articleshare-shrink_480/articleshare-shrink_480/0/1726649398643?e=1752850800&v=beta&t=RY1i5VqslkJyz3jR75ohC5KyfvvJEupCBkZWWOAIsFU)


[https://python.langchain.com/](https://python.langchain.com/)


[Introduction | 🦜️🔗 LangChain](https://python.langchain.com/)


[python.langchain.com](https://python.langchain.com/)


🔍 Q&A Module: Law Enforcement Focus json [ { “question”: “Which countries have activated multisectoral law enforcement responses to Kush?”, “answer”: “Liberia (national emergency and task force), The Gambia (zero-tolerance raids), Nigeria (parallel variant monitoring), Côte d’Ivoire (network mapping).” }, { “question”: “Where are the highest trafficking risks located?”, “answer”: “Coastal cities like Conakry, Bissau, and Freetown; these serve as maritime entry points for synthetic drugs, confirmed by FTIR and overdose clusters.” }, { “question”: “What regional patterns suggest the presence of organized criminal syndicates?”, “answer”: “Mass burials in Sierra Leone, xenophobia-linked migrant flows in The Gambia, and structured distribution routes in Côte d’Ivoire and Guinea all signal coordinated trafficking networks.” }, { “question”: “How are alerts escalated in the workflow?”, “answer”: “High-risk nodes (e.g. fatality cluster >0.9) trigger MISP event creation, escalation via TheHive case templates, and operator alerts through Slack, Signal, or email.” } ]”QandA_Analysis”: [{ “question”: “What is the primary demographic affected by the Kush crisis?”, “answer”: “Males aged 18-25 across Sierra Leone, Liberia, and Nigeria, with increased vulnerability tied to unemployment, post-conflict trauma, and poor mental health services.” }, { “question”: “Which cities are seeing the most severe overdose events?”, “answer”: “Freetown, Kenema, and Monrovia are epicenters, with mass detox admissions and emergency declarations indicating escalating public health impact.” }, { “question”: “Where has chemical confirmation of nitazenes occurred?”, “answer”: “Guinea-Bissau and Sierra Leone—FTIR testing revealed active nitazenes, confirming toxic profiles of local Kush variants.” }, { “question”: “What health system gaps are impeding response?”, “answer”: “Limited psychiatric facilities (e.g. one hospital for all Sierra Leone), low mental health worker ratios, and inadequate infrastructure for community reintegration and rehabilitation.” } ] Each Q&A response can be dynamically generated through LangChain RAG pipelines using semantic retrieval over regional JSON metadata, format these for a live dashboard module or embed them into your case ingest automation { “question”: “How is raw incident data transformed into usable intelligence?”, “answer”: “Raw data (CDC reports, ER logs, MISP feeds) is ingested, normalized via ETL tools (e.g., AWS Glue), validated against JSON schemas, then enriched with geolocation and demographic metadata before storage in Elasticsearch or PostgreSQL.” }, { “question”: “What triggers a real-time alert in MISP?”, “answer”: “Events such as new attributes, indicators sightings, or confidence scores >90% activate MISP’s ZeroMQ workflows using PyMISP. Tags like ‘tlp:red’ route alerts via email, webhook, or Slack.” }, { “question”: “How does TheHive handle incoming alerts?”, “answer”: “TheHive API receives the JSON payload from MISP or SIEM. Cases are created using predefined templates with observables, tasks, and escalation logic for analyst workflows.” }, { “question”: “What role does LangChain play in the workflow?”, “answer”: “LangChain enables Retrieval Augmented Generation (RAG) Q&A by indexing incident data (via RecursiveCharacterTextSplitter) into a VectorStore. This supports semantic search and context-injected prompting for informed decisions.” }, { “question”: “How are field operators notified?”, “answer”: “Using OAuth2-authenticated push mechanisms, alerts are sent to Slack (via Bolt SDK), Signal (via REST-API signal-cli), and email (SMTP or RedMail). These include traceable logs and audit metadata.” }, { “question”: “Can the pipeline support edge-case or manual interventions?”, “answer”: “Yes. Form-based UIs (e.g., JSONForms or Ngx-Formly) allow operators to override automated logic, submit custom attributes, or inject exception cases directly to sandbox endpoints for validation.” }, { “question”: “Is this architecture modular and scalable?”, “answer”: “Absolutely. Each node—ingestion, alerting, Q&A, notification—is stateless and independently retryable. Airflow or LangChain’s StateGraph enables DAG orchestration across cloud-native or hybrid deployments.” } ] }


---


## 1. JSON for Observable Dashboard (Law Enforcement/Public Health Q&A Module)


Structure your JSON so it’s easily mapped into dashboard cards, accordion panels, chatbot APIs, or case ingest screens:


```
{
  "QandA_Analysis": [
    {
      "category": "Law Enforcement",
      "question": "Which countries have activated multisectoral law enforcement responses to Kush?",
      "answer": "Liberia (national emergency and task force), The Gambia (zero-tolerance raids), Nigeria (parallel variant monitoring), Côte d’Ivoire (network mapping)."
    },
    {
      "category": "Geo-Intelligence",
      "question": "Where are the highest trafficking risks located?",
      "answer": "Coastal cities like Conakry, Bissau, and Freetown; these serve as maritime entry points for synthetic drugs, confirmed by FTIR and overdose clusters."
    },
    {
      "category": "Criminal Syndicates",
      "question": "What regional patterns suggest the presence of organized criminal syndicates?",
      "answer": "Mass burials in Sierra Leone, xenophobia-linked migrant flows in The Gambia, and structured distribution routes in Côte d’Ivoire and Guinea all signal coordinated trafficking networks."
    },
    {
      "category": "Automation",
      "question": "How are alerts escalated in the workflow?",
      "answer": "High-risk nodes (e.g. fatality cluster >0.9) trigger MISP event creation, escalation via TheHive case templates, and operator alerts through Slack, Signal, or email."
    },
    {
      "category": "Public Health",
      "question": "What is the primary demographic affected by the Kush crisis?",
      "answer": "Males aged 18-25 across Sierra Leone, Liberia, and Nigeria, with increased vulnerability tied to unemployment, post-conflict trauma, and poor mental health services."
    },
    {
      "category": "Hotspot Detection",
      "question": "Which cities are seeing the most severe overdose events?",
      "answer": "Freetown, Kenema, and Monrovia are epicenters, with mass detox admissions and emergency declarations indicating escalating public health impact."
    },
    {
      "category": "Chemical Surveillance",
      "question": "Where has chemical confirmation of nitazenes occurred?",
      "answer": "Guinea-Bissau and Sierra Leone—FTIR testing revealed active nitazenes, confirming toxic profiles of local Kush variants."
    },
    {
      "category": "Healthcare Infrastructure",
      "question": "What health system gaps are impeding response?",
      "answer": "Limited psychiatric facilities (e.g. one hospital for all Sierra Leone), low mental health worker ratios, and inadequate infrastructure for community reintegration and rehabilitation."
    },
    {
      "category": "Data Engineering",
      "question": "How is raw incident data transformed into usable intelligence?",
      "answer": "Raw data (CDC reports, ER logs, MISP feeds) is ingested, normalized via ETL tools (e.g., AWS Glue), validated against JSON schemas, then enriched with geolocation and demographic metadata before storage in Elasticsearch or PostgreSQL."
    },
    {
      "category": "Alerting",
      "question": "What triggers a real-time alert in MISP?",
      "answer": "Events such as new attributes, indicators sightings, or confidence scores >90% activate MISP's ZeroMQ workflows using PyMISP. Tags like 'tlp:red' route alerts via email, webhook, or Slack."
    },
    {
      "category": "Case Management",
      "question": "How does TheHive handle incoming alerts?",
      "answer": "TheHive API receives the JSON payload from MISP or SIEM. Cases are created using predefined templates with observables, tasks, and escalation logic for analyst workflows."
    },
    {
      "category": "AI / LangChain",
      "question": "What role does LangChain play in the workflow?",
      "answer": "LangChain enables Retrieval Augmented Generation (RAG) Q&A by indexing incident data (via RecursiveCharacterTextSplitter) into a VectorStore. This supports semantic search and context-injected prompting for informed decisions."
    },
    {
      "category": "Field Ops Notification",
      "question": "How are field operators notified?",
      "answer": "Using OAuth2-authenticated push mechanisms, alerts are sent to Slack (via Bolt SDK), Signal (via REST-API signal-cli), and email (SMTP or RedMail). These include traceable logs and audit metadata."
    },
    {
      "category": "Edge Cases & Exception Handling",
      "question": "Can the pipeline support edge-case or manual interventions?",
      "answer": "Yes. Form-based UIs (e.g., JSONForms or Ngx-Formly) allow operators to override automated logic, submit custom attributes, or inject exception cases directly to sandbox endpoints for validation."
    },
    {
      "category": "Architecture",
      "question": "Is this architecture modular and scalable?",
      "answer": "Absolutely. Each node—ingestion, alerting, Q&A, notification—is stateless and independently retryable. Airflow or LangChain's StateGraph enables DAG orchestration across cloud-native or hybrid deployments."
    }
  ]
}
```


---


## 2. Display as Markdown (Perfect for Dashboards or Documentation)


```
### Law Enforcement and Public Health Q&A Module

**Q:** Which countries have activated multisectoral law enforcement responses to Kush?  
**A:** Liberia (national emergency and task force), The Gambia (zero-tolerance raids), Nigeria (parallel variant monitoring), Côte d’Ivoire (network mapping).

**Q:** Where are the highest trafficking risks located?  
**A:** Coastal cities like Conakry, Bissau, and Freetown; these serve as maritime entry points for synthetic drugs, confirmed by FTIR and overdose clusters.

**Q:** What regional patterns suggest the presence of organized criminal syndicates?  
**A:** Mass burials in Sierra Leone, xenophobia-linked migrant flows in The Gambia, and structured distribution routes in Côte d’Ivoire and Guinea all signal coordinated trafficking networks.

**Q:** How are alerts escalated in the workflow?  
**A:** High-risk nodes (e.g. fatality cluster >0.9) trigger MISP event creation, escalation via TheHive case templates, and operator alerts through Slack, Signal, or email.

*...and so on for all above Q&A pairs.*  
```


---


## 3. LangChain Integration Example


**All of these Q&As can be indexed as document “chunks” or vectors, so that the LangChain-powered Q&A chatbot retrieves the most relevant answer based on user query.**


```
from langchain.vectorstores import InMemoryVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter

qna = [ ... ]  # list of dicts above

# Prepare docs for vector store
docs = [f"Q: {item['question']}\nA: {item['answer']}" for item in qna]
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
splits = splitter.split_documents(docs)

vector_store = InMemoryVectorStore().add_documents(splits)

def get_qna_answer(query):
    results = vector_store.similarity_search(query)
    return results[0]['content'] if results else "No answer found."
```


---


## 4. Best Practice for Use Cases


- **Ops Dashboard**: Load as cards with Q (expand) and A (reveal/click). Filter by category.
- **API/LLM Agent**: Serve as RAG-ready context for legal, policy, or field ops Q&A.
- **Documentation**: Publish as Markdown, providing real-world evidence-backed answers for teams, partners, or leadership.


---


- HTML/JS module boilerplate
- Streamlit/Gradio demo for these Q&A
- Additional public health/law enforcement-specific query groups
- Dashboard wireframe/mockups


Edge endpoint integration, SlackOps alert hook, blend your real-time ingestion into regional Q&A fusionpython from fastapi import FastAPI, Request from langchain.chat_models import ChatOpenAI from langchain.vectorstores import InMemoryVectorStore from langchain.schema import Document from langchain.chains import RetrievalQA import os


# Tracing setup


os.environ[“LANGCHAIN_TRACING_V2”] = “true” os.environ[“LANGCHAIN_API_KEY”] = “your-langsmith-api-key”


app = FastAPI()


# Dummy docs for demo


docs = [ Document(page_content=”Mass overdose in Bo linked to Type C Kush”, metadata={“region”: “Bo”, “risk”: 0.91}), Document(page_content=”Confirmed cemetery desecration in Freetown”, metadata={“region”: “Freetown”, “risk”: 0.94}) ]


llm = ChatOpenAI(model=”gpt-4″) retriever = InMemoryVectorStore.from_documents(docs, llm.embedder).as_retriever() qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)


@app.post(“/query_kush_qna”) async def query_agent(request: Request): body = await request.json() question = body.get(“question”) response = qa_chain.run(question) return {“answer”: response}


This is an excellent **fusion of regional Q&A, real-time ingestion, and edge endpoint architecture** using FastAPI, LangChain, and embedding regional metadata. Here’s how to make it a fully actionable blueprint, including **SlackOps alert hooks** for immediate field notification—ideal for live ops.


---


## 1. Complete Real-Time Regional Q&A FastAPI Endpoint


- **Vector store** includes region/risk metadata.
- **RetrievalQA** chain enables semantic Q&A.
- **SlackOps alert** is triggered on high-risk responses (customize-able).


Below is an extended and annotated version for clarity and operational value:


```
from fastapi import FastAPI, Request
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import InMemoryVectorStore
from langchain.schema import Document
from langchain.chains import RetrievalQA
import os
import requests

# === LangChain/Tracing Setup ===
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-api-key"

app = FastAPI()

# Dummy ingestion example; replace with real streaming ingestion into docs
docs = [
    Document(page_content="Mass overdose in Bo linked to Type C Kush", metadata={"region": "Bo", "risk": 0.91}),
    Document(page_content="Confirmed cemetery desecration in Freetown", metadata={"region": "Freetown", "risk": 0.94}),
    # ...add docs from real ingestion pipeline here
]

# Vector Embedder Selection
llm = ChatOpenAI(model="gpt-4")
vector_store = InMemoryVectorStore.from_documents(docs, llm.embedder)
retriever = vector_store.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# === SlackOps Integration ===
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  # Set your webhook

def post_slack_alert(answer, region, risk):
    if SLACK_WEBHOOK_URL and risk > 0.9:
        msg = f":rotating_light: *High-risk Kush incident* in {region}\n>{answer}"
        requests.post(SLACK_WEBHOOK_URL, json={"text": msg})

# === Edge Endpoint ===
@app.post("/query_kush_qna")
async def query_agent(request: Request):
    body = await request.json()
    question = body.get("question")
    response = qa_chain({"query": question})
    answer = response["result"]

    # Extract region/risk if available from the returned source document
    source_docs = response.get("source_documents", [])
    if source_docs:
        metadata = source_docs[0].metadata
        region = metadata.get("region", "unknown")
        risk = metadata.get("risk", 0)
        # SlackOps alert on high-risk
        post_slack_alert(answer, region, risk)
    return {"answer": answer, "region": region, "risk": risk}

# Example curl command for testing:
# curl -X POST http://localhost:8000/query_kush_qna -H "Content-Type: application/json" -d '{"question":"Where have the deadliest Kush incidents happened?"}'
```


---


## 2. How it Works (and Why This Matters)


- **Real-time ingestion** (`docs`) can be updated live from Kafka, database, or manual ingest (expand with actual ETL).
- **LangChain RetrievalQA** gives instant, region-aware, evidence-backed answers.
- **Edge endpoint** (`/query_kush_qna`) supports secure local or cloud deployment—from command centers to mobile field ops.
- **SlackOps Alert Hook** posts urgent, high-risk findings directly to your operations channel—closing the loop between data ingestion, AI, and human action.


---


## 3. Extensibility & Best Practices


- Swap `llm.embedder` for custom embedding models if fine-tuning is needed for West African substance/crisis context.
- Use richer doc ingestion (stream from JSON ingestion microservices) for up-to-the-second operational intelligence.
- Add authentication and audit logging for production field ops (see oauth2/jwt notes in your earlier pipeline).
- Expand the SlackOps logic to include geographic coordinates, time, and links to open an incident in TheHive or MISP.


---


## 4. Integration Schema for Case Automation


If you wish to automate the escalation to TheHive or MISP:


- Add a post-processing step to create a case/alert if `risk > threshold`.
- Integrate with your case ingestion API (as in previous Q&A steps).
- Optionally, notify not just Slack but also Signal, SMS, or field ops dashboards.


---


**Let me know if you want:**


- A template for *streaming ingestion* into your `docs` list (from CDC/MISP feeds)
- *OAuth2 field operator auth* for this endpoint
- *Full ops dashboard* wireframe (Streamlit, Observable, etc.)


Your stack is modern, modular, and ready for scale—this pattern is exactly how to make *AI-powered alerting* actionable in complex regional crises!


FastAPI: Expose /query_kush_qna endpoint for field use
Your agent acts as a semantic gateway layered on top of: LangChain tracing for orchestrated Kush Crisis pipeline—particularly for legal, public health, and enforcement Q&A nodes—you’ll want to optimize for observability, semantic transparency, and chain introspection

🔍 What LangChain Tracing Provides
LangChain tracing (via LangSmith or local traces) helps:
Visualize how each step of your pipeline (e.g., document loading → embedding → retrieval → prompt construction → LLM call) operates.
Debug vector similarity mismatches or context injection errors.
Audit Q&A reasoning trails, especially in high-risk public health or enforcement workflows.


Pre-validated JSON ingestion nodes (CDC, ER, MISP).
Escalation triggers via TheHive and Slack/Signal.
Indexing using LangChain’s VectorStore.
Dynamic Q&A endpoint—optimized for policy, law enforcement, and public health usage.

⚙️ Step-by-Step Setup
1. Enable LangSmith Tracing
python
import os
os.environ[“LANGCHAIN_TRACING_V2”] = “true”
os.environ[“LANGCHAIN_API_KEY”] = “your-langsmith-api-key”
You can set this in your [main.py](http://main.py/), Jupyter cell, or .env file.
2. Instrument Your Components
python
from langchain.chat_models import ChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

# Sample documents
docs = [
Document(page_content=”Mass overdose cluster in Kenema”, metadata={“city”: “Kenema”, “risk”: 0.92}),
Document(page_content=”FTIR lab confirmed nitazenes in Bissau”, metadata={“city”: “Bissau”, “risk”: 0.85})
]

# Text splitter + embeddings
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
embeddings = OpenAIEmbeddings()

# VectorStore
store = InMemoryVectorStore.from_documents(chunks, embeddings)
retriever = store.as_retriever()

# LLM with tracing enabled
llm = ChatOpenAI(model=”gpt-4″, temperature=0)

# Prompt chain with context injection
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_t


🧠 RAG-Ready Agent Context for Each Domain
⚖️ Legal / Policy
json
{
“query”: “What human rights violations have occurred due to Kush criminal networks?”,
“source_index”: “Kenema, Sierra Leone”,
“embedding_nodes”: [
“mass burial events”,
“cemetery desecration”,
“psychiatric infrastructure gaps”
],
“policy_traceability”: {
“documents”: [
“MOHS emergency declaration”,
“BBC Kush report”,
“FTIR toxicology metadata”
],
“langchain_index”: “PolicyLaw_KushQ&A”,
“retrieval_method”: “Cosine + prompt-injected tracing”
}


[https://lnkd.in/e9Vv2Hq9](https://lnkd.in/e9Vv2Hq9)


[https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/](https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/)


![](https://media.licdn.com/dms/image/sync/v2/D4E27AQFIZpRcCefDlA/articleshare-shrink_480/B4EZf5oo6GHsAo-/0/1752239870498?e=1752847200&v=beta&t=0u2YPkwFGFOW08RNIpNRB-AVv6X1lbpCmlIrjiRjVdY)


[https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/](https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/)


[“Kush_Crisis_GeoInt_Regional”: Orchestrated Workflow (with Node & Arrow Logic) langchain_core.vectorstores import In MemoryVectorStore{“Sierra_Leone”](https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/)


[jessrsdincyahoocom.wordpress.com](https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/)


> “Kush_Crisis_GeoInt_Regional”: Orchestrated Workflow (with Node & Arrow Logic) langchain_core.vectorstores import MemoryVectorStore{“Sierra_Leone”

[Embedded media](https://jessrsdincyahoocom.wordpress.com/2025/07/11/kush_crisis_geoint_regional-orchestrated-workflow-with-node-arrow-logic-langchain_core-vectorstores-import-in-memoryvectorstore/embed/#?secret=YPKArgO0zN#?secret=v87e9htaSy)


[Embedded media](https://www.youtube.com/embed/Eu4-bmoXG3U?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en&autohide=2&wmode=transparent)
