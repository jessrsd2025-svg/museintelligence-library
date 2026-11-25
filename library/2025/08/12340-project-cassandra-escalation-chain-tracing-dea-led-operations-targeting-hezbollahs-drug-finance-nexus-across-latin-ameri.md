---
title: "Project Cassandra escalation chain: Tracing DEA-led operations targeting Hezbollah’s drug-finance nexus across Latin America, West Africa, and the Middle East"
date: 2025-08-12T15:56:34
url: "https://jessrsdincyahoocom.wordpress.com/2025/08/12/project-cassandra-escalation-chain-tracing-dea-led-operations-targeting-hezbollahs-drug-finance-nexus-across-latin-america-west-africa-and-the-middle-east/"
source_id: SRC-WP-12340
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/08/12/project-cassandra-escalation-chain-tracing-dea-led-operations-targeting-hezbollahs-drug-finance-nexus-across-latin-america-west-africa-and-the-middle-east/"
retrieval_timestamp: 2026-11-25T18:01:10Z
---

![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/08/image-15.png?w=938)


> **DEA’s Project Cassandra Escalation Chain**
> The operation targeted Hezbollah’s Latin American drug-finance nexus, employing “Cocaine-for-cash” pipelines and “Crypto laundering” channels [File: Hezbollah_Drug_Finance.pdf, DocID: d12345]. Treasury escalated via **OFAC Sanctions** on key hawala operators [File: OFAC_Designation_Jan2025.pdf, DocID: d67890], culminating in asset freezes and interagency prosecutions.
>
> *Quote Evidence:* “HFNT’s forensic tracing linked Tron-based USDT wallets to Venezuelan oil-collateralized trades” [File: DOJ_HFNT_CryptoOps.pdf, DocID: d11223]…
>
> Cypher queries scaffold Project Cassandra DEA-led operation targeting Hezbollah’s drug-finance nexus across Latin America, West Africa, and the Middle East.
>
> Project Cassandra escalation chain Hezbollah Drug Finance Nexus Mapping.pdf
>
> **Cypher query scaffolds** for **Project Cassandra** and its evolution, with an eye towards production-level **Neo4j graph intelligence/forensic workflows**. This includes a clear **schema rationale** and concrete extraction logic for insight into Hezbollah’s narco-financing via crypto and oil trades, compliant with your context.
>
> ---
>
> ### 1. Project Cassandra Escalation Chain (DEA-Led: 2015–2018)
>
> ```
> // Project Cassandra: DEA-led Hezbollah Drug-Finance Nexus Mapping
> MATCH (dea:Agency {name:"DEA"})-[:LED]->(op:Operation {name:"Project Cassandra"})
> MATCH (op)-[:TARGETED]->(network:Hezbollah_Network)
> MATCH (network)-[:OPERATES_IN]->(region:Region)
> MATCH (network)-[:USES]->(method:Finance_Method)
> MATCH (method)-[:FACILITATES]->(activity:Illicit_Activity)
> MATCH (activity)-[:TRIGGERS]->(response:US_Treasury_Action)
> WHERE region.name IN ["Latin America", "West Africa", "Middle East"]
>   AND method.type IN ["Cocaine-for-cash", "Crypto laundering", "Hawala"]
>   AND response.type IN ["OFAC_Sanction", "SDGT_Designation"]
> RETURN op.name AS Operation,
>  region.name AS Region,
>  method.type AS Finance_Method,
>  activity.name AS Illicit_Activity,
>  response.type AS Treasury_Response,
>  response.date AS Action_Date
> ORDER BY response.date DESC;
> ```
>
> **Schema Highlights:**
>
> Project Cassandra escalation chain Hezbollah Drug Finance Nexus Mapping (1)Download- Tracks *DEA* leadership, operation targeting, geographic footprint, and financial typologies (drugs/crypto/hawala).
> - Surfaces *US Treasury* intervention points (e.g., OFAC sanctions).
>
> ---
>
> ### 2. DOJ-HFNT Revival (2020–2025): Crypto Escalation & Interagency Forensics
>
> ```
> // DOJ-led HFNT Task Force: Reviving Project Cassandra
> MATCH (doj:Agency {name:"DOJ"})-[:CREATED]->(hfnt:TaskForce {name:"HFNT"})
> MATCH (hfnt)-[:REVIVES]->(op:Operation {name:"Project Cassandra"})
> MATCH (hfnt)-[:COORDINATES_WITH]->(partner:Agency)
> MATCH (hfnt)-[:PROSECUTES]->(target:Entity)-[:AFFILIATED_WITH]->(hez:Network {name:"Hezbollah"})
> MATCH (target)-[:USES]->(wallet:CryptoWallet)-[:ON_CHAIN]->(chain:Blockchain)
> MATCH (wallet)-[:LINKED_TO]->(dto:DTO)
> MATCH (dto)-[:OPERATES_IN]->(region:Region)
> WHERE chain.name = "Tron"
>   AND wallet.asset = "USDT"
>   AND wallet.sanctioned = true
>   AND region.name IN ["Venezuela", "Tri-Border Area", "Syria"]
>   AND partner.name IN ["DEA", "FBI", "HSI", "Treasury"]
> RETURN hfnt.name AS Task_Force,
>  partner.name AS Interagency_Partner,
>  target.name AS Prosecuted_Entity,
>  wallet.address AS Sanctioned_Wallet,
>  dto.name AS DTO,
>  region.name AS Region,
>  chain.name AS Blockchain,
>  wallet.asset AS Asset,
>  wallet.sanctioned_date AS OFAC_Designation_Date
> ORDER BY wallet.sanctioned_date DESC;
> ```
>
> **Key Enhancements:**
>
> - Shows DOJ/OFAC’s targeting of Hezbollah crypto wallets (USDT on Tron).
> - Extends operational intelligence to **DTOs** sharing laundering rails, and the precise interagency workflow.
>
> ---
>
> ### 3. IRGC–Venezuela–Hezbollah: Crypto-Oil-Narco Nexus
>
> ```
> // Core Entities
> MATCH (ven:State {name:"Venezuela"})-[:EXPORTS_OIL_TO]->(iran:State {name:"Iran"})
> MATCH (iran)-[:SECURES_TRADE_VIA]->(irgc:Entity {name:"IRGC_Oil_Security"})
> MATCH (ven)-[:COLLATERALIZES]->(wallet:CryptoWallet)-[:ON_CHAIN]->(chain:Blockchain)
> MATCH (wallet)-[:ISSUES]->(asset:Stablecoin {name:"USDT"})
> MATCH (wallet)-[:LINKED_TO]->(hez:Network {name:"Hezbollah"})
> MATCH (hez)-[:USES]->(broker:OTC_Broker)
> MATCH (broker)-[:FACILITATES]->(dto:DTO)
> MATCH (dto)-[:OPERATES_IN]->(region:Region)
> MATCH (wallet)-[:FLAGGED_IN]->(dash:Dashboard {name:"wallet_watch"})
> WHERE chain.name IN ["Tron","Ethereum"]
>   AND asset.name = "USDT"
>   AND region.name IN ["Tri-Border Area", "West Africa", "Lebanon"]
> RETURN ven.name AS Oil_Exporter,
>  iran.name AS Oil_Recipient,
>  irgc.name AS Trade_Security,
>  wallet.address AS Wallet_Address,
>  chain.name AS Blockchain,
>  asset.name AS Stablecoin,
>  hez.name AS Terror_Network,
>  broker.name AS OTC_Broker,
>  dto.name AS DTO,
>  region.name AS DTO_Region,
>  dash.name AS Dashboard
> ORDER BY wallet.address;
> ```
>
> #### Schema/Context Table Recap:
>
> | Component | Role in Narco-Terrorism Financing |
> | --- | --- |
> | Venezuela Oil Receivables | Collateral for bulk USDT issuance via Tron/Ethereum |
> | IRGC_Oil_Security | Secures oil shipments, enabling crypto-backed trade |
> | Hezbollah OTC Brokers | Bridge DTO cash flows into crypto rails |
> | DTO Wallets | Launder proceeds via pseudonymous chains (Tron, Ethereum) |
> | wallet_watch Dashboard | Tracks flagged wallets across TRM, OFAC, and SDGT designations |
>
> ---
>
> ### Scalable Application
>
> - **Interdiction simulation overlays:** Can add nodes for maritime swaps, precursor volatility modeling, counterfactual projections (e.g., `:Counterfactual_Op`).
> - **Real Time Compliance**: Integrate with Graph-RAG or TRM Labs dashboards for wallet analytics, sanctions, and real-world entity flagging.
>
> ---
>
> **Summary**: The Cypher scaffolds allow a multi-layered, compliance-ready model of Hezbollah, IRGC, and DTO crypto-narco-oil finance flows, supporting real-world operational tracking, prosecution cases, and proactive interdiction simulation.


**Venezuela–Iran–Hezbollah crypto-oil nexus**, converging on shared laundering infrastructure and DTO-linked wallet flows across **Tron** and **Ethereum**. It also reflects how **crypto assists narco-terrorism financing** through oil-backed stablecoin issuance and Hezbollah-linked OTC brokers.


## 🔗 Cypher Query: Venezuela–Iran–Hezbollah Crypto-Oil Nexus


cypher


```
// Core Entities
MATCH (ven:State {name:"Venezuela"})-[:EXPORTS_OIL_TO]->(iran:State {name:"Iran"})
MATCH (iran)-[:SECURES_TRADE_VIA]->(irgc:Entity {name:"IRGC_Oil_Security"})
MATCH (ven)-[:COLLATERALIZES]->(wallet:CryptoWallet)-[:ON_CHAIN]->(chain:Blockchain)
MATCH (wallet)-[:ISSUES]->(asset:Stablecoin {name:"USDT"})
MATCH (wallet)-[:LINKED_TO]->(hez:Network {name:"Hezbollah"})
MATCH (hez)-[:USES]->(broker:OTC_Broker)
MATCH (broker)-[:FACILITATES]->(dto:DTO)
MATCH (dto)-[:OPERATES_IN]->(region:Region)
MATCH (wallet)-[:FLAGGED_IN]->(dash:Dashboard {name:"wallet_watch"})
WHERE chain.name IN ["Tron", "Ethereum"]
  AND asset.name = "USDT"
  AND region.name IN ["Tri-Border Area", "West Africa", "Lebanon"]
RETURN ven.name AS Oil_Exporter,
       iran.name AS Oil_Recipient,
       irgc.name AS Trade_Security,
       wallet.address AS Wallet_Address,
       chain.name AS Blockchain,
       asset.name AS Stablecoin,
       hez.name AS Terror_Network,
       broker.name AS OTC_Broker,
       dto.name AS DTO,
       region.name AS DTO_Region,
       dash.name AS Dashboard
ORDER BY wallet.address;
```


## Step 1 – Run 1_escalation_chain_primary


- Pulls the **Project Cassandra escalation chain** with filters for your regions, finance methods, and Treasury action types.
- Returns up to 25 recent actions sorted by Treasury action date.
- Captures `op_id` for linking to evidence.


**Step 2 – Run `2_supporting_quotes`**


- Pass `op_id` from Step 1 as `$opId`.
- Retrieves the **top 5 most confident Quote nodes** from the ingested PDFs that directly support that operation node.
- Includes file name, document title, and document ID for citation.


**Step 3 – Feed both results into `3_formatted_narrative_prompt`**


LLM formats into an analyst-grade narrative with inline `[File: ..., DocID: ...]` references


Insert Step 1 JSON into `{escalation_chain_json}` and Step 2 JSON into `{quotes_json}`.


1. Run the escalation-chain retrieval.
2. Use the returned node IDs to pull evidence quotes + PDF source metadata.
3. Format it as an analyst-friendly narrative with embedded provenance.


---


## JSON Package – GraphRAG Prompt Templates


```
{
  "graphRAG_templates": {
    "1_escalation_chain_primary": {
      "description": "Retrieve Project Cassandra escalation chain details filtered by region, finance method, and Treasury response type.",
      "cypher": "MATCH (dea:Agency {name:'DEA'})-[:LED]->(op:Operation {name:'Project Cassandra'})\nOPTIONAL MATCH (op)-[:TARGETED]->(network)\nOPTIONAL MATCH (network)-[:OPERATES_IN]->(region:Region)\nOPTIONAL MATCH (network)-[:USES]->(method:Finance_Method)\nOPTIONAL MATCH (method)-[:FACILITATES]->(activity:Illicit_Activity)\nOPTIONAL MATCH (activity)-[:TRIGGERS]->(response:US_Treasury_Action)\nWHERE region.name IN $regions\n  AND method.type IN $methods\n  AND response.type IN $responseTypes\nWITH op, region, method, activity, response\nORDER BY response.date DESC\nRETURN op.name AS operation,\n       region.name AS region,\n       method.type AS finance_method,\n       activity.name AS illicit_activity,\n       response.type AS treasury_response,\n       response.date AS action_date,\n       id(op) AS op_id\nLIMIT 25;",
      "params": {
        "regions": ["Latin America","West Africa","Middle East"],
        "methods": ["Cocaine-for-cash","Crypto laundering","Hawala"],
        "responseTypes": ["OFAC_Sanction","SDGT_Designation"]
      },
      "output_fields": ["operation","region","finance_method","illicit_activity","treasury_response","action_date","op_id"]
    },
    "2_supporting_quotes": {
      "description": "For a given Operation ID, retrieve top 5 supporting quotes with file citations from ingested documents.",
      "cypher": "MATCH (op:Operation) WHERE id(op) = $opId\nMATCH (op)<-[:SUPPORTS]-(q:Quote)<-[:CONTAINS_QUOTE]-(d:Document)\nWITH q, d ORDER BY q.confidence DESC, q.start_offset ASC\nRETURN q.text AS quote_text,\n       q.confidence AS confidence,\n       d.file_name AS file_name,\n       d.title AS document_title,\n       d.id AS document_id\nLIMIT 5;",
      "params": {
        "opId": "<replace_with_op_id_from_previous_step>"
      },
      "output_fields": ["quote_text","confidence","file_name","document_title","document_id"]
    },
    "3_formatted_narrative_prompt": {
      "description": "LLM prompt template for merging escalation chain data with supporting quotes into a coherent, evidence-backed narrative.",
      "prompt": "You are an intelligence analyst producing a chrono-geospatial escalation report on DEA's Project Cassandra. Below is the escalation chain output and its top 5 supporting quotes with file citations.\\n\\nEscalation Chain Data:\\n{escalation_chain_json}\\n\\nSupporting Quotes:\\n{quotes_json}\\n\\nWrite a concise but detailed narrative that: (1) explains the DEA-led escalation chain in clear operational terms; (2) cites the supporting quotes inline with [File: file_name, DocID: document_id]; (3) preserves key factual details from the escalation chain and quotes; (4) maintains original context without speculation. Output as Markdown."
    }
  }
}
```


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/08/image-13.png?w=374)


GraphRAG Prompt Templates for Escalation Chain Queries Structure^J Quote Node Retrieval and File Citation IntegrationDownload
2501.00309v2Download
[https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s](https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s)


![](https://media.licdn.com/dms/image/sync/v2/D5627AQElI3qaHHO8TQ/articleshare-shrink_480/B56ZX67nRwGUAo-/0/1743671686697?e=1755622800&v=beta&t=rhT1dh1bUJRA-5UL4bGcKMzQP3bAkhBafL3Q9peEM4A)


[https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s](https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s)


[Hezbollah’s Network on America’s Southern Doorstep](https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s)


[rand.org](https://www.rand.org/pubs/commentary/2025/04/hezbollahs-network-on-americas-southern-doorstep.html#:~:text=Proven%20Capability%2C%20Persistent%20Intent,region%20since%20the%20early%201980s)
