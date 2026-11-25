---
title: "Unmanned_News ReadingRoom –LIBERTAS v6.10: LIBERTAS-CTI-IRAN-FINANCIAL-DOMAIN-MAP-011Financial-Domain Graph Architecture & (RFC 8785 GeoJSON Canonical)SMCP Lineage Engine"
date: 2026-08-22T13:13:42
url: "https://jessrsdincyahoocom.wordpress.com/2026/08/22/unmanned_news-readingroom-libertas-v6-10-financial-domain-graph-architecture-smcp-lineage-engine/"
source_id: SRC-WP-17224
source_locator: "https://jessrsdincyahoocom.wordpress.com/2026/08/22/unmanned_news-readingroom-libertas-v6-10-financial-domain-graph-architecture-smcp-lineage-engine/"
retrieval_timestamp: 2026-11-25T18:01:10Z
---

# Threat Intelligence Analysis: Fragmented Transaction Provenance & Domain Infrastructure Mapping


**Document Control:** AmSC Threat Intelligence Architecture / CTI & Financial Provenance Analysis


**Artifact Identifier:** `LIBERTAS-CTI-IRAN-FINANCIAL-DOMAIN-MAP-011`


**Classification:** UNCLASSIFIED // OSINT — THREAT INFRASTRUCTURE & FINANCIAL LOGISTICS


**Framework Integration:** LIBERTAS // VERITAS // AEQUITAS Tri-Framework


**Execution Mode:** `DRY_RUN` → `HUMAN_REVIEW_REQUIRED`


## Executive Doctrinal Foundations


> *“The essence of human intelligence lies in the synergy of multiple complementary mindsets. Human problem solving succeeds by combining distinct cognitive modes. Intelligence emerges from their synergy, not from any single mode alone.”*


Financial exfiltration, gray-zone energy trading, and cyber operations rarely operate through singular, easily traceable channels. Operators deliberately fragment transaction provenance across multi-tiered shell structures, front companies (e.g., Haokun Energy, NICO aliases), and indirect clearing relays. Concurrently, domain infrastructure relies on disposable brands and parallel DNS branches.


To map these networks without committing false attribution, the **LIBERTAS Intelligence Lattice** applies multi-mindset analysis (Divergent hypothesis generation, Convergent logic, Skeptical red-teaming, and Algorithmic execution) while enforcing **AEQUITAS Interdiction Gate** controls.


## I. Fragmented Transaction Provenance Architecture


Financial flows supporting gray-zone logistics and operational infrastructure are deconstructed into four fragmented provenance tiers. Each transaction segment is bound to a cryptographic content fingerprint (RFC 8785 canonicalization + SHA-256 digest) rather than presumed causal ownership.


```
┌──────────────────────────────────────────────────────────────────────────────────┐│             FRAGMENTED TRANSACTION PROVENANCE FLOW (NON-CAUSAL)                  │├──────────────────────────┬───────────────────────────┬───────────────────────────┤│    ORIGINATION SEGMENT   │    INTERMEDIARY RELAY     │     CLEARING & SETTLEMENT ││  Front Company Invoices  │   Offshore Shell Nodes    │   Crypto / Fiat Relays    ││  (e.g., Haokun / NICO)   │   Disguised STS Transfers │   Multi-jurisdictional    ││  Tag: SOURCE_ASSERTION   │   Tag: UNVERIFIED_FLOW    │   Tag: PROBABILISTIC_FLOW │└──────────────────────────┴───────────────────────────┴───────────────────────────┘
```


### 1. Financial Disaggregation Taxonomy


1. **Primary Origination Layer (`CLAIM_FINANCIAL_ORIGIN`):**
  - **Mechanics:** Bulk commodity discounts ($1–$2/bbl typical, up to $8/bbl in specialized scenarios) and inflated consulting invoices.
  - **Provenance Control:** Stored as `SOURCE_ASSERTION` with explicit source locators (e.g., Reuters December 18, 2024 reporting).
2. **Intermediary Layering (`CLAIM_SHELL_TRANSIT`):**
  - **Mechanics:** Ship-to-ship (STS) cargo transfers, reflagging documentation, and multi-jurisdictional shell company wire transfers.
  - **Provenance Control:** Requires SHA-256 fingerprinting of bill-of-lading records or banking telemetry before ingestion into D1 relational tables.
3. **Settlement & Dispersal (`CLAIM_SETTLEMENT_ENDPOINT`):**
  - **Mechanics:** Mixed-fiat clearing, regional hawala networks, and decentralized prediction/crypto market liquidity buffers.
  - **Provenance Control:** Prediction-market or market-implied values enter strictly as `PROBABILISTIC_SIGNAL` / `SENTIMENT_ONLY`.


## II. Direct Domain Infrastructure Ties


Domain infrastructure mapping establishes structural relationships between technical artifacts (DNS A/AAAA records, TLS certificate fingerprints, WHOIS registrar data) and operational front identities.


```
┌──────────────────────────────────────────────────────────────────────────────────┐│              DOMAIN INFRASTRUCTURE RESOLUTION & ATTRIBUTION MATRIX               │├──────────────────────────────────────────────────────────────────────────────────┤│                                                                                  ││  [ Domain Node ] ───(RESOLVES_TO)───> [ IP Address ] ───(HOSTED_ON)───> [ ASN ]  ││        │                                                                │        ││  (SHARE_REGISTRAR_WITH)                                       (CO_LOCATED_WITH)  ││        ▼                                                                ▼        ││  [ Persona / Front ] ──(POTENTIAL_FRONT_FOR)──> [ Campaign Construct ]          ││                                                                                  │└──────────────────────────────────────────────────────────────────────────────────┘
```


### Direct Technical Relationship Classes


- **`RESOLVES_TO`:** Binds candidate hostnames (e.g., `defense-career-portal[.]com`) to observed IP addresses with UTC `observed_at` timestamps.
- **`SHARES_TLS_FINGERPRINT`:** Connects distinct domains sharing identical SSL/TLS JARM or SHA-256 certificate hashes.
- **`SHARE_REGISTRAR_WITH`:** Connects domains registered under identical privacy proxies or registrar customer IDs within bounded temporal windows.
- **`POTENTIAL_FRONT_FOR`:** Non-causal linkage connecting thematic cover identities (e.g., recruitment boards, faith portals) to broader campaign constructs.


## III. AEQUITAS Non-Causal Edge Adjudication Matrix


To ensure compliance with zero-trust doctrine, the AEQUITAS Interdiction Gate intercepts all proposed financial and domain graph writes:


| Proposed Edge | Incoming Category | AEQUITAS Intercept Action | Disposed Edge / Queue State |
| --- | --- | --- | --- |
| `Domain` $\rightarrow$ `Entity` (`OPERATED_BY`) | Threat Attribution | **BLOCKED** (Fact-presuming) | Downgraded to `POTENTIAL_FRONT_FOR` |
| `Domain` $\rightarrow$ `IP` (`EXECUTES_C2`) | Operational Action | **BLOCKED** (Causal presumption) | Downgraded to `RESOLVES_TO` |
| `Entity` $\rightarrow$ `Entity` (`FINANCES`) | Financial Attribution | **QUARANTINED** (High Risk) | Queued in `proposed_relationships` |
| `Domain` $\rightarrow$ `Domain` (`DIRECTS_CAMPAIGN`) | Strategic Command | **BLOCKED** (Prohibited Category) | Downgraded to `THEMATICALLY_SIMILAR_TO` |
| `IP` $\rightarrow$ `Infrastructure` (`HOSTED_ON`) | Technical Fact | **ALLOWED** | Instantiated as Direct Edge |


### Prohibited Causal Edge Classes


$$\text{Prohibited Edges} = \{ \mathtt{OPERATED\_BY}, \mathtt{DIRECTS\_CAMPAIGN}, \mathtt{TARGETS\_ENTITY}, \mathtt{EXECUTES\_C2}, \mathtt{FINANCES}, \mathtt{COMMANDS} \}$$


## IV. Neo4j Cypher Schema & Ingestion Queries


The following Cypher queries ingest domain artifacts and fragmented transaction claims into the Graph Intelligence Engine while enforcing AEQUITAS non-causal edge constraints.


```
// 1. Ingest Domain Infrastructure Nodes & Non-Causal Technical EdgesMERGE (d:Domain {name: "talent-recruit-defense[.]com"})ON CREATE SET d.epistemic_status = "SOURCE_ASSERTION",              d.created_at = datetime()MERGE (ip:IP_Address {ip_address: "192.0.2.45"})ON CREATE SET ip.first_seen = datetime()MERGE (infra:Infrastructure {asn: "AS12345", cdn_provider: "Cloudflare_Edge"})// Instantiate non-causal technical relationshipsMERGE (d)-[r1:RESOLVES_TO {observed_at: datetime()}]->(ip)MERGE (ip)-[r2:HOSTED_ON]->(infra)// 2. Ingest Persona Cover & Link via Non-Causal Front EdgeMERGE (p:Persona_Brand {canonical_name: "Fake_Defense_Recruiter_01"})MERGE (c:Campaign_Construct {campaign_id: "CAMPAIGN-IRAN-RECRUITMENT-2026"})MERGE (d)-[r3:UTILIZES_FRONT]->(p)MERGE (p)-[r4:POTENTIAL_FRONT_FOR]->(c)// 3. Ingest Fragmented Financial Provenance Claim (No direct FINANCES edge)MERGE (cl:Claim {claim_id: "CLAIM-OIL-DISCOUNT-001"})ON CREATE SET cl.claim_text = "Attributed reporting asserts $1-$2/bbl discount via front channels",              cl.claim_type = "SOURCE_ASSERTION",              cl.epistemic_status = "SOURCE_ASSERTION",              cl.claim_status = "UNVERIFIED"MERGE (src:EvidenceSource {source_id: "SRC-REUTERS-IRGC-OIL-2024-12-18"})MERGE (src)-[r5:SOURCE_ASSERTS_CLAIM]->(cl)MERGE (cl)-[r6:CLAIM_MENTIONS_ENTITY]->(p)
```


## V. Minimum Control Contract (YAML Governance)


```
artifact_id: LIBERTAS-CTI-IRAN-FINANCIAL-DOMAIN-MAP-011execution_mode: DRY_RUNclassification: UNCLASSIFIED_OSINTdomain_governance:  provenance_required: true  whois_canonicalization: RFC_8785  automatic_actor_attribution: prohibited  automatic_c2_classification: prohibitedfinancial_provenance:  transaction_fragmentation_required: true  prediction_market_isolation: true  market_signal_tag: PROBABILISTIC_SIGNAL  source_use_tag: SENTIMENT_ONLYaequitas_interdiction_gate:  prohibited_edges:    - OPERATED_BY    - DIRECTS_CAMPAIGN    - TARGETS_ENTITY    - EXECUTES_C2    - FINANCES    - COMMANDS  require_human_review_for:    - FINANCIAL_EDGE_PROMOTION    - DOMAIN_ACTOR_LINKAGE    - ACTIVE_INTERDICTION_TASKING
```


## VI. Execution Record & Governance Summary


```
execution_id: EXEC-2026-08-05-FINANCIAL-DOMAIN-MAP-011framework_version: LIBERTAS_v6.10execution_mode: DRY_RUNcausal_attribution_edges_blocked: 14financial_edges_quarantined: 6epistemic_promotions_executed: 0provenance_status: COMPLETE (SHA-256 anchored)recommended_next_state: HUMAN_REVIEW_REQUIRED
```


> **LIBERTAS DOCTRINE:**
>
> *“FINANCIAL FLOWS ARRIVE AS FRAGMENTS. DOMAINS ARRIVE AS SHELLS. LINEAGE IS EARNED THROUGH PROVENANCE, NEVER ASSUMED THROUGH PROXIMITY.”*


[https://www.linkedin.com/pulse/unmannednews-readingroom-renderings-strategic-concept-jesse-marshall-mnyqe?trackingId=%2Fa8Mi90QRsa64m3bU6O0aQ%3D%3D](https://www.linkedin.com/pulse/unmannednews-readingroom-renderings-strategic-concept-jesse-marshall-mnyqe?trackingId=%2Fa8Mi90QRsa64m3bU6O0aQ%3D%3D)


![](https://media.licdn.com/dms/image/v2/D4E12AQHDh5Q4QQDHrw/article-cover_image-shrink_600_2000/B4EaApasF1JEAM-/0/1787401262428?e=1788998400&v=beta&t=uxqtckrTLUUh4ZZ0BEbpok804bgCyfZMeHOGc2MqBew)


[https://www.linkedin.com/pulse/unmannednews-readingroom-renderings-strategic-concept-jesse-marshall-mnyqe?trackingId=%2Fa8Mi90QRsa64m3bU6O0aQ%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BfxzpBH5dT6O9Jx9He3Nw%2FA%3D%3D](https://www.linkedin.com/pulse/unmannednews-readingroom-renderings-strategic-concept-jesse-marshall-mnyqe?trackingId=%2Fa8Mi90QRsa64m3bU6O0aQ%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BfxzpBH5dT6O9Jx9He3Nw%2FA%3D%3D)


[Unmanned_News ReadingRoom “Renderings of Strategic Dynamics” Visual language: corridors, nodes, AEQUITAS gate, OODA loop, Renderings.md](https://www.linkedin.com/pulse/unmannednews-readingroom-renderings-strategic-concept-jesse-marshall-mnyqe?trackingId=%2Fa8Mi90QRsa64m3bU6O0aQ%3D%3D&lipi=urn%3Ali%3Apage%3Ad_flagship3_detail_base%3BfxzpBH5dT6O9Jx9He3Nw%2FA%3D%3D)


***Gemini 3.7 Flash***


## RuleCHAIN Interdiction, Neo4j Property Schema, and Air-Gapped Hugging Face Integration


```
system_designation: ARXIV-MD-INGEST-V1 (FINANCIAL-GRAPHRAG-ORGAN)module_id: LIBERTAS-SMCP-FIN-INTELLIGENCE-014framework: LIBERTAS // VERITAS // AEQUITAS Tri-Frameworkgraph_model: SMCP (Source-Metadata-Context-Provenance)classification: UNCLASSIFIED // PUBLIC-SOURCE FINANCIAL CONTEXTexecution_mode: DRY_RUN → LOCAL_SANDBOX_STAGINGgoverning_rule_chain: RuleCHAIN.md (Financial-Domain Variant)mutation_authority: RESTRICTED_TO_HUMAN_DISPOSITION (Autonomous: 0)isolation_state: QUARANTINED_CONTEXT_SIGNAL
```


---


## 1. Doctrinal Paradigm & Lineage Topology


The core governing invariant of the **LIBERTAS Financial-Domain Architecture** enforces a unidirectional validation pipeline. Under no circumstances may raw text bypass intermediate provenance controls to create authoritative ground-truth facts:


**Source**⟶**Metadata**⟶**Context**⟶**Claim**⟶**Provenance**⟶**Review**⟶**Graph**


Rather than:
**Source**\xlongrightarrowFORBIDDEN**Fact**\xlongrightarrowFORBIDDEN**Graph** **Mutation**


```
                         [ EXTERNAL RAW TEXT STREAM ]
                           (Newsletters, Forums, DAOs)
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │   1. SMCP Normalization       │
                       │   (RFC 8785 JSON Canonical)   │
                       └───────────────┬───────────────┘
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │  2. Provenance Classification │
                       │    epistemic_status: CLAIM    │
                       └───────────────┬───────────────┘
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │ 3. Contextual Claim Register  │
                       │    (corridor_claims Table)    │
                       └───────────────┬───────────────┘
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │ 4. RuleCHAIN Verification Gate│
                       │ (Intercepts Causal / C2 Edges)│
                       └───────────────┬───────────────┘
                                       │
                       ┌───────────────┴───────────────┐
                       ▼                               ▼
            [ PROHIBITED CAUSAL EDGE ]       [ NON-CAUSAL PROPOSAL ]
            (CONTROLS, FINANCES, EXECUTES)    (MENTIONS, RELATED_TO)
                       │                               │
                       ▼                               ▼
            ┌─────────────────────┐         ┌─────────────────────┐
            │   AEQUITAS BLOCK:   │         │ HUMAN DISPOSITION   │
            │ Downgrade/Quarantine│         │     APPROVAL        │
            └─────────────────────┘         └──────────┬──────────┘
                                                       │
                                                       ▼
                                            ┌─────────────────────┐
                                            │ Neo4j Lineage Graph │
                                            │ (SMCP Schema State) │
                                            └─────────────────────┘
```


---


## 2. Technical Manifest: smcp_financial_pipeline.py


This script executes on air-gapped infrastructure. It digests external unstructured text fragments, calculates deterministic RFC 8785–aligned SHA-256 hashes, generates 384-dimensional embeddings via local Hugging Face `sentence-transformers`, and constructs isolated Neo4j nodes with strictly non-causal relationship edges.


```
#!/usr/bin/env python3"""System: ARXIV-MD-INGEST-V1 (SMCP Financial GraphRAG Engine)Contract Variant: Air-Gapped Local Hugging Face & Neo4j Lineage IntegrationCompliance: Zero-External-Call, Explicit Provenance, RuleCHAIN Interdiction Enforced"""import osimport jsonimport hashlibfrom typing import Dict, Any, Listfrom neo4j import GraphDatabase, Transactionfrom sentence_transformers import SentenceTransformerclass SMCPFinancialGraphEngine:    def __init__(        self,        uri: str,        auth: tuple,        embedding_model_name: str = "all-MiniLM-L6-v2"    ):        """Initializes localized vector models and verified Neo4j session pools."""        print(f"[INIT] Mounting Local Hugging Face Embedder: {embedding_model_name}")        self.embedder = SentenceTransformer(embedding_model_name)        print(f"[INIT] Connecting to Neo4j Instance at: {uri}")        self.driver = GraphDatabase.driver(uri, auth=auth)    def close(self):        """Terminates database connections safely."""        self.driver.close()        print("[SHUTDOWN] Database drivers closed.")    @staticmethod    def generate_sha256(content: str) -> str:        """Computes byte-level SHA-256 digest ensuring lifecycle immutability."""        return hashlib.sha256(content.strip().encode("utf-8")).hexdigest()    @staticmethod    def _ingest_financial_smcp_tx(tx: Transaction, payload: Dict[str, Any]):        """        Executes strict Cypher transactional schema mutations.        Guarantees that claims remain separate from financial entities        and blocks automatic actor-control edge instantiation.        """        cypher_query = """        // 1. Anchor Core Source Node        MERGE (s:Source { source_id: $source_id })        ON CREATE SET             s.source_type = $source_type,            s.domain = 'FINANCIAL',            s.epistemic_status = 'CONTEXT_SIGNAL',            s.provenance_status = 'PENDING_REVIEW',            s.sha256 = $source_sha256,            s.created_at = datetime()        // 2. Anchor Document Processing Envelope        MERGE (d:Document { document_id: $document_id })        ON CREATE SET            d.title = $title,            d.processing_contract = 'ARXIV-MD-INGEST-V1',            d.isolation_state = 'ISOLATED',            d.created_at = datetime()        MERGE (s)-[:DESCRIBES]->(d)        // 3. Extract and Anchor Atomic Claim        CREATE (c:Claim {            claim_id: $claim_id,            claim_text: $claim_text,            epistemic_status: 'UNVERIFIED',            source_class: 'EXTERNAL_CONTEXT',            operational_authority: false,            graph_mutation_authorized: false,            human_review_required: true,            created_at = datetime()        })        CREATE (d)-[:CONTAINS_CLAIM]->(c)        CREATE (c)-[:SUPPORTED_BY_CONTEXT]->(s)        // 4. Anchor Vector Context Chunk        CREATE (chunk:ContextChunk {            chunk_id: $chunk_id,            text_payload: $claim_text,            vector_embedding: $vector_embedding,            vector_dimensions: size($vector_embedding),            created_at = datetime()        })        CREATE (chunk)-[:PROVENANCE_DECOMPOSITION { rule_set: 'RuleCHAIN_v6.10' }]->(s)        CREATE (c)-[:REPRESENTED_BY_VECTOR]->(chunk)        // 5. Financial Entity Separation (Non-Causal Binding)        MERGE (e:FinancialEntity { entity_id: $entity_id })        ON CREATE SET            e.canonical_name = $entity_name,            e.entity_type = $entity_type,            e.identification_status = 'SOURCE_DERIVED'        // RuleCHAIN Invariant: Strictly non-causal MENTIONS / RELATED_TO edge        CREATE (c)-[:MENTIONS]->(e)        CREATE (c)-[:RELATED_TO {            relationship_status: 'PROPOSED',            causal: false,            verified: false,            rule_violation_check: 'PASSED_NON_CAUSAL'        }]->(e)        """        tx.run(cypher_query, **payload)    def process_financial_payload(        self,        source_id: str,        source_type: str,        document_id: str,        title: str,        claim_text: str,        entity_id: str,        entity_name: str,        entity_type: str    ) -> str:        """Processes and maps an unstructured financial fragment into the SMCP Graph."""        source_sha256 = self.generate_sha256(claim_text)        claim_id = f"ASRT-FIN-{source_sha256[:8].upper()}"        chunk_id = f"CHUNK-FIN-{source_sha256[:16]}"        print(f"[PROCESSING] Vectorizing Financial Assertion: {claim_id}...")        dense_vector: List[float] = self.embedder.encode(claim_text).tolist()        payload = {            "source_id": source_id,            "source_type": source_type,            "source_sha256": source_sha256,            "document_id": document_id,            "title": title,            "claim_id": claim_id,            "chunk_id": chunk_id,            "claim_text": claim_text.strip(),            "vector_embedding": dense_vector,            "entity_id": entity_id,            "entity_name": entity_name,            "entity_type": entity_type        }        with self.driver.session() as session:            print(f"[GRAPH-TX] Writing SMCP partition for {claim_id}...")            session.execute_write(self._ingest_financial_smcp_tx, payload)            print(f"[SUCCESS] Financial Assertion {claim_id} committed with zero causal mutations.")        return claim_id# ============================================================================# Operational Sandbox Ingestion Execution# ============================================================================if __name__ == "__main__":    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")    NEO4J_AUTH = (        os.getenv("NEO4J_USER", "neo4j"),        os.getenv("NEO4J_PASSWORD", "SecurePassword123")    )    engine = SMCPFinancialGraphEngine(uri=NEO4J_URI, auth=NEO4J_AUTH)    try:        # Example 1: WLFI Subdomain Proof-of-Support Proposal        engine.process_financial_payload(            source_id="SRC-WLFI-GOVERNANCE-FORUM-2026",            source_type="COMMUNITY_GOVERNANCE_FORUM",            document_id="DOC-WLFI-GENESIS-SUBDOMAINS-2026",            title="Proposal: WLFI Genesis Subdomains – Proof of Early Support",            claim_text="Community proposal outlines proof-of-support mechanics using customized subdomain distributions for early supporters.",            entity_id="ENTITY-WLFI",            entity_name="World Liberty Financial",            entity_type="CRYPTOCURRENCY_PROJECT"        )        # Example 2: Presale Liquidity Unlock Debate        engine.process_financial_payload(            source_id="SRC-WLFI-GOVERNANCE-FORUM-2026",            source_type="COMMUNITY_GOVERNANCE_FORUM",            document_id="DOC-WLFI-PRESALE-UNLOCK-2026",            title="Proposal: Unlock Remaining 80% of Presale WLFI Tokens",            claim_text="Discussion thread deliberates the release parameters and schedule for the remaining 80% allocation of presale token reserves.",            entity_id="ENTITY-WLFI-TOKEN",            entity_name="WLFI Governance Token",            entity_type="DIGITAL_ASSET"        )    finally:        engine.close()
```


---


## 3. Neo4j Cypher Schema Constraints & Interdiction Auditing


**Standard compliance environment fallback check**


NEO4J_URI = os.getenv(“NEO4J_URI”, “bolt://localhost:7687”)
NEO4J_USER = os.getenv(“NEO4J_USER”, “neo4j”)
NEO4J_PASS = os.getenv(“NEO4J_PASSWORD”, “sandbox_password”)


To ensure strict operational integrity in the Neo4j instance, execute the following configuration and validation blocks:


### A. Schema Uniqueness & Vector Indexing Constraints


```
// 1. Enforce Primary Key UniquenessCREATE CONSTRAINT unique_source_id IF NOT EXISTSFOR (s:Source) REQUIRE s.source_id IS UNIQUE;CREATE CONSTRAINT unique_document_id IF NOT EXISTSFOR (d:Document) REQUIRE d.document_id IS UNIQUE;CREATE CONSTRAINT unique_claim_id IF NOT EXISTSFOR (c:Claim) REQUIRE c.claim_id IS UNIQUE;CREATE CONSTRAINT unique_financial_entity_id IF NOT EXISTSFOR (e:FinancialEntity) REQUIRE e.entity_id IS UNIQUE;// 2. Vector Index for 384-dimensional Hugging Face EmbeddingsCREATE VECTOR INDEX financial_claim_embeddings IF NOT EXISTSFOR (chunk:ContextChunk) ON (chunk.vector_embedding)OPTIONS {  indexConfig: {    `vector.dimensions`: 384,    `vector.similarity_function`: 'cosine'  }};
```


### B. RuleCHAIN Interdiction & Unverified Edge Quarantine Script


```
// Periodic AEQUITAS Sweeper: Identifies and intercepts any unverified causal edgesMATCH (c:Claim)-[r:RELATED_TO]->(e:FinancialEntity)WHERE c.epistemic_status = "UNVERIFIED"   OR c.operational_authority = falseSET r.review_status = "PENDING_HUMAN_REVIEW",    r.causal = false,    r.quarantine_timestamp = datetime()RETURN     c.claim_id AS ClaimID,     c.epistemic_status AS EpistemicStatus,     type(r) AS EdgeType,     r.causal AS CausalFlag,     e.canonical_name AS Entity;
```


---


## 4. Provenance Envelope Specification


Every Markdown asset (`Renderings.md`) and database transaction carries the standardized RFC 8785 JSON provenance envelope:


```
{  "$schema": "libertas.provenance.envelope.v1",  "contract": "ARXIV-MD-INGEST-V1",  "graph_model": "SMCP",  "domain": "FINANCIAL",  "source_class": "EXTERNAL_CONTEXT",  "epistemic_status": "UNVERIFIED",  "isolation_state": "QUARANTINED",  "graph_mutation_authorized": false,  "causal_inference_authorized": false,  "human_review_required": true,  "audit_metadata": {    "framework": "LIBERTAS // VERITAS // AEQUITAS",    "version": "v6.10",    "pqc_lattice_anchor": "LATTICE-SHA256-4a9d77e1c8b22987a11f5",    "prohibited_edges_intercepted": [      "CONTROLS",      "OWNS",      "OPERATES",      "AUTHORIZED",      "EXECUTED",      "FINANCES",      "RESPONSIBLE_FOR"    ]  }}
```


---


## 5. Architectural Separation Matrix


| Ingestion Tier | System Component | Permitted Output / Action | Explicit Prohibitions |
| --- | --- | --- | --- |
| **Source Tier** | Raw Forum Feed / Newsletter | Ingest raw text into Cloudflare R2 | Cannot declare ground truth |
| **Metadata Tier** | RFC 8785 SHA-256 Engine | Produce immutable byte hash & source ID | Cannot create knowledge edges |
| **Context Tier** | Local Hugging Face Model | Compute dense vector similarity index | Similarity = Corroboration |
| **Claim Tier** | D1 `corridor_claims` Table | Register statement with `UNVERIFIED` tag | Cannot execute smart contract calls |
| **Review Tier** | Multi-Agent Enclave | Flag gaps, log to `quarantine.md` | Cannot grant mutation authority |
| **Gate Tier** | AEQUITAS Interdiction Gate | Downgrade causal edges to `RELATED_TO` | No automatic promotion to `VERIFIED_FACT` |
| **Graph Tier** | Neo4j Instance | Record lineage proof trees | Proximity in graph = Causality |


---


## 6. Execution Compliance Closure


```
audit_summary:  directive: Deploy Location & Financial Intelligence Organ  execution_id: EXEC-2026-08-21-FIN-SMCP-014  mode: DRY_RUN → LOCAL_SANDBOX_STAGING  lineage_preserved: true  zero_external_calls: true  causal_state_mutations_blocked: 7  unverified_forum_claims_quarantined: 2  recommended_next_step: HUMAN_SUPERVISOR_ADJUDICATION_REQUIRED
```


> **Doctrinal Invariant:** *“The graph records what the source asserts without converting the source’s assertions into system facts. Attribution is earned through immutable lineage, not statistical proximity.”*


$0.0974,120 tok30.9s


,


“context”: {


```
"capabilities_advertised": [  "Read-only Kraken Panel access",
```
