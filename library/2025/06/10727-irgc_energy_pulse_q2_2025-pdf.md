---
title: "IRGC_Energy_Pulse_Q2_2025.pdf “energy_security_cross_theater”"
date: 2025-06-23T12:01:54
url: "https://jessrsdincyahoocom.wordpress.com/2025/06/23/irgc_energy_pulse_q2_2025-pdf/"
source_id: SRC-WP-10727
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/06/23/irgc_energy_pulse_q2_2025-pdf/"
retrieval_timestamp: 2026-11-25T18:01:10Z
---

**GraphRAG+Neo4j OSINT/alert system** to support:


- **Cognitive Triage (Analyst Triage/Alert Prioritization)**
- **Operational Wargaming (Red/Blue cell, “what if” drills)**
- **Policy Modeling (Impact forecasting, scenario testing)**


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/06/image-36.png?w=938)


IRGC_Energy_Pulse_Q2_2025Download
Jess_Unmanned_News_RSDDownload
GraphRAG+Neo4j setup functions as an **intelligence amplification layer** for geopolitical risk workflows. Based on the surrounding context, here’s a breakdown of its operational roles:


### 1. Cognitive Triage


**Purpose:** Support analysts in rapidly sorting incoming OSINT signals (like AIS hits, Treasury advisories, DOJ PDFs) by relevance, urgency, and geopolitical linkage.


**How it works:**


- Each new alert (e.g., an IRGC-linked tanker update) is embedded, mapped into the knowledge graph, and assigned a **tradeoff score** (like deterrence vs. diplomacy).
- **Timeline tags** and **node relations** help triage whether a signal is routine or indicative of escalation.


### 2. Operational Wargaming


**Purpose:** Enable “red vs. blue” scenario testing by simulating action-reaction flows in the knowledge graph.


**How it works:**


- An analyst (blue cell) can test responses like “U.S. expands ISR near IRGC lanes.”
- The system traverses graph edges (e.g., **“provokes_counterstrategy”**) to simulate IRGC or Chinese responses.
- Edge weights and timeline anchors help visualize probable escalation paths.


### 3. Policy Modeling


**Purpose:** Test the second- and third-order effects of decisions like sanctioning PLA-linked firms or rerouting naval assets.


**How it works:**


- Graph queries forecast whether new sanctions would disrupt energy flows, embolden proxies, or complicate diplomacy.
- Scenario tags like `"energy_security_cross_theater"` allow for targeted what-if modeling tied to temporal phases (e.g., mid_2025).


Altogether, the system isn’t just ingesting alerts — it’s **prioritizing them, simulating their impact, and translating policy into forecastable network effects**.


## Directory Structure


```
project/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── ingestion/
│   ├── main.py
│   ├── neo4j_ingest.py
│   ├── langchain_pipeline.py
│   └── pdf_alert_report.py
├── osint/
│   ├── ais_stream.py
│   ├── fincen_alert_parser.py
│   └── treasury_monitor.py
└── config/
    └── .env  # (Neo4j/LangChain/AIS keys & configs)
```


---


## 2. Dockerfile


```
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ingestion ./ingestion
COPY ./osint ./osint
COPY ./config/.env .env

CMD ["python", "-u", "./ingestion/main.py"]
```


---


## 3. requirements.txt (core libs)


```
langchain
neo4j
pdfkit
jinja2
schedule
openai  # or other LLM vendor
requests
python-dotenv
watchdog
flask  # (optional: REST API wrapper)
```


---


## 4. Neo4j Ingestion Script (neo4j_ingest.py)


```
from neo4j import GraphDatabase
import os

class Neo4jIngestor:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        pwd = os.getenv("NEO4J_PASSWORD", "password")
        self.driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def ingest_node(self, node_obj):
        with self.driver.session() as session:
            query = (
                "MERGE (n:Node {id: $id}) "
                "SET n += $props "
                "RETURN n"
            )
            session.run(query, id=node_obj['id'], props=node_obj['properties'])

    def ingest_edge(self, from_id, to_id, relation):
        with self.driver.session() as session:
            query = (
                "MATCH (a:Node {id: $from}), (b:Node {id: $to}) "
                "MERGE (a)-[r:" + relation + "]->(b) "
                "RETURN r"
            )
            session.run(query, from=from_id, to=to_id)

# Usage: from neo4j_ingest import Neo4jIngestor; ingestor = Neo4jIngestor(); ...
```


---


## 5. LangChain Pipeline (langchain_pipeline.py)


```
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai, os

VDB_PATH = "db/irgc_vector"
EMBEDDINGS = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

def ingest_document(doc_text):
    chunks = RecursiveCharacterTextSplitter(chunk_size=1024).split_text(doc_text)
    vectors = EMBEDDINGS.embed_documents(chunks)
    vdb = FAISS.load_local(VDB_PATH) if os.path.exists(VDB_PATH) else FAISS.from_documents([], embeddings=EMBEDDINGS)
    vdb.add_texts(chunks)
    vdb.save_local(VDB_PATH)
```


---


## 6. AIS-to-Node Automation (ais_stream.py)


```
import requests
import schedule, time
from neo4j_ingest import Neo4jIngestor

AIS_FEED_URL = "https://api.ais.example.com/irgc_tankers"
ingestor = Neo4jIngestor()

def check_shadow_fleet():
    response = requests.get(AIS_FEED_URL)
    for vessel in response.json().get('shadow_fleet', []):
        node = {
            "id": vessel['imo'],
            "properties": {
                "name": vessel['name'],
                "last_reported_position": vessel['position'],
                "last_seen": vessel['timestamp'],
                "flag": vessel['flag'],
                "irgc_link": True
            }
        }
        ingestor.ingest_node(node)

schedule.every(10).minutes.do(check_shadow_fleet)
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
```


---


## 7. FinCEN/Treasury Alert Parser (fincen_alert_parser.py)


```
import pdfplumber
from langchain_pipeline import ingest_document
from neo4j_ingest import Neo4jIngestor

ALERT_PDF_PATH = "/data/fincen_alert_q2_2025.pdf"
ingestor = Neo4jIngestor()

def parse_fincen_alert():
    with pdfplumber.open(ALERT_PDF_PATH) as pdf:
        doc_text = "\n".join(page.extract_text() for page in pdf.pages)
    ingest_document(doc_text)
    irgc_risk_node = {
        "id": "IRGC_Oil_Security_Q2_2025",
        "properties": {
            "alert_score": 0.74,
            "summary": "IRGC shadow fleet and oil financing supports proxies and evades U.S. containment; linked to rising Red Sea/Indo-Pacific volatility."
        }
    }
    ingestor.ingest_node(irgc_risk_node)

if __name__ == "__main__":
    parse_fincen_alert()
```


---


## 8. PDF Auto-Report (pdf_alert_report.py)


```
import pdfkit, jinja2

def create_alert_pdf(context, output_path="alert_2page.pdf"):
    template_str = """
    <h1>{{ title }}</h1>
    <b>Trigger Event:</b> {{ event }}<br>
    <b>Alert Score:</b> {{ score }}<br>
    <b>Summary:</b> {{ summary }}<br>
    <b>Recommendations:</b>
    <ul>{% for rec in recommendations %}
        <li>{{ rec }}</li>
    {% endfor %}</ul>
    <h2>Temporal Graph & Escalation</h2>
    <b>Chain:</b> {{ graph_chain }}
    """
    template = jinja2.Template(template_str)
    html = template.render(**context)
    pdfkit.from_string(html, output_path)
```


---


## 9. Continuous/Scheduled Pipeline (main.py)


```
import schedule, time
from osint.ais_stream import check_shadow_fleet
from osint.fincen_alert_parser import parse_fincen_alert

def run_pipeline():
    check_shadow_fleet()
    parse_fincen_alert()
    # Add other sources/streams

schedule.every(15).minutes.do(run_pipeline)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
```


---


**To run everything:**


- Fill in `.env` with your secrets and endpoints.
- `docker-compose up` launches the periodic ingestion, graph/node creation, vector DB update, and report generation.


---


### 🛠️


**Extending:**


- Add Flask endpoints for ad-hoc alert search.
- Plug in real Treasury/DOJ/AIS endpoints and automate PDF alert feeds into your dashboard or S3.
- Use `neo4j_admin import` or Cypher for bulk node/edge batch ingestion.


---


**Example:**


jessrsd IRGC_Energy_PulseDownload
- When an AIS anomaly or FinCEN PDF comes in, your pipeline tags the shadow fleet, scores risk, updates the graph, and generates a PDF—optionally emailing or pushing a dashboard notification.


FinCEN Advisory on the Iranian Regimes Illicit OilDownload
