---
title: "ISR Tasking: “How IRGC leverages West Africa’s Sahan for logistics, smuggling, and regional proxy training”"
date: 2025-06-27T12:19:30
url: "https://jessrsdincyahoocom.wordpress.com/2025/06/27/isr-tasking-how-irgc-leverages-west-africas-sahan-for-logistics-smuggling-and-regional-proxy-training/"
source_id: SRC-WP-10898
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/06/27/isr-tasking-how-irgc-leverages-west-africas-sahan-for-logistics-smuggling-and-regional-proxy-training/"
retrieval_timestamp: 2026-11-27T16:42:05Z
---

## Data Pipeline Mock (GeoJSON + GraphRAG Ready)


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/06/image-54.png?w=683)


| Node ID | Label | Category | Risk Score | Timeline |
| --- | --- | --- | --- | --- |
| `CHINA_INFRA_CORRIDOR` | China Belt Port (Djibouti) | infra_dual_use | 0.78 | 2017–present |
| `RUSSIA_WAGNER_MALI` | Wagner Ops Hub (Mali) | proxy_security | 0.88 | 2020–present |
| `CHINA_URANIUM_TRADE` | Chinese Uranium Import Node | nuclear_supply_chain | 0.81 | 2015–present |
| `RUSSIA_DIPLOMATIC_PUSH` | Kremlin Africa Bloc Voting | diplomatic_influence | 0.65 | 2022–present |


| From Node | To Node | Relation Type |
| --- | --- | --- |
| `IRGC_AFRICA_INFLUENCE` | `CHINA_URANIUM_TRADE` | `enables_resource_flow` |
| `IRGC_AFRICA_INFLUENCE` | `RUSSIA_WAGNER_MALI` | `aligns_with_proxy_ops` |
| `RUSSIA_WAGNER_MALI` | `WEST_AFRICA_DIPLOMATIC_BREAKS` | `provokes_realignment` |
| `CHINA_INFRA_CORRIDOR` | `AFRICA_URANIUM_FLOW` | `facilitates_dual_use_logistics` |


### 🛰️ Sentiment Surge Indicators


- **Mali & CAR**: Surge in pro-Russian sentiment post-Wagner deployments
- **Djibouti & Sudan**: Chinese port logistics flagged in anti-Western disinfo campaigns
- **Niger & Namibia**: Local unrest tied to uranium extraction and foreign military presence


### 🧠 Shapley-style Alert Rationale (Sample Node: RUSSIA_WAGNER_MALI)


- +0.30: PMC deployment near uranium corridor
- +0.25: Surge in anti-French sentiment
- +0.20: Alignment with IRGC proxy logistics
- **Composite Risk Score**: 0.88


### 🗺️ Overlay Enhancements


- **GeoJSON-ready**: Add new nodes to `africom_uranium_graphrag_q3_2025.geojson`
- **Timeline-aware**: Animate escalation from Q2 → Q3 (e.g., Wagner expansion, Chinese port activity)
- **ISR Tasking**: Highlight ISR gaps near dual-use corridors (e.g., Djibouti–Sudan–Niger axis)
-


### 📚 Sources & Context


[https://www.rand.org/pubs/tools/TLA2045-3.html](https://www.rand.org/pubs/tools/TLA2045-3.html)[https://saiia.org.za/research/russia-and-china-in-africa-prospective-partners-or-asymmetric-rivals/](https://saiia.org.za/research/russia-and-china-in-africa-prospective-partners-or-asymmetric-rivals/)


[https://saiia.org.za/research/russia-and-china-in-africa-prospective-partners-or-asymmetric-rivals/](https://saiia.org.za/research/russia-and-china-in-africa-prospective-partners-or-asymmetric-rivals/)


[https://www.cfr.org/backgrounder/russias-growing-footprint-africa](https://www.cfr.org/backgrounder/russias-growing-footprint-africa)


![www.cfr.org](https://services.bingapis.com/favicon?url=www.cfr.org)


[http://www.cfr.org3](http://www.cfr.org3)


![saiia.org.za](https://services.bingapis.com/favicon?url=saiia.org.za)


saiia.org.za4


![www.rand.org](https://services.bingapis.com/favicon?url=www.rand.org)


[http://www.rand.org](http://www.rand.org)


- Council on Foreign Relations: Russia’s PMC and diplomatic expansion across Africa
- RAND: Mapping Chinese and Russian arms/security exports
- SAIIA: China–Russia as asymmetric rivals in Africa
- CNN: Wagner’s role in CAR, Mali, and uranium-linked operations


policy-facing PDF alert or Observable notebook with toggles for China/Russia/IRGC overlays.`africom_uranium_graphrag_q3_2025.geojson` (adapt format for Mapbox/Leaflet/Kepler, or as direct input for GraphRAG overlays):


IRGC_AFRICA_INFLUENCE Iran and Russian access Africa_Uranium_ResourceDownload
```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "IRGC_AFRICA_INFLUENCE",
      "geometry": { "type": "Point", "coordinates": [32.53, 15.60] },
      "properties": {
        "label": "IRGC Africa Ops Hub",
        "description": "IRGC leverages Sudan for logistics, smuggling, and regional proxy training.",
        "category": "proxy_ops",
        "timeline": ["1990s-present"],
        "risk_score": 0.90,
        "graphRAG_id": "IRGC_AFRICA_INFLUENCE"
      }
    },
    {
      "type": "Feature",
      "id": "HEZBOLLAH_AFRICA",
      "geometry": { "type": "Point", "coordinates": [-4.39, 7.38] },
      "properties": {
        "label": "Hezbollah Proxy Node",
        "description": "Hezbollah/PMF support network for logistics/finance in West Africa.",
        "category": "proxy_finance",
        "timeline": ["2000s-present"],
        "risk_score": 0.83,
        "graphRAG_id": "HEZBOLLAH_AFRICA"
      }
    },
    {
      "type": "Feature",
      "id": "AFRICA_URANIUM_FLOW",
      "geometry": { "type": "Point", "coordinates": [8.08, 17.57] },
      "properties": {
        "label": "Uranium Resource Node",
        "description": "IRGC/Iranian interests in uranium extraction for nuclear program.",
        "category": "nuclear_supply_chain",
        "timeline": ["2010s-present"],
        "risk_score": 0.85,
        "graphRAG_id": "AFRICA_URANIUM_FLOW"
      }
    },
    {
      "type": "Feature",
      "id": "WEST_AFRICA_DIPLOMATIC_BREAKS",
      "geometry": { "type": "Point", "coordinates": [-16.58, 13.45] },
      "properties": {
        "label": "Diplomatic Blowback Node",
        "description": "States recalibrate alliances/break ties after IRGC-linked trafficking.",
        "category": "diplomatic_pivot",
        "timeline": ["2010-present"],
        "risk_score": 0.55,
        "graphRAG_id": "WEST_AFRICA_DIPLOMATIC_BREAKS"
      }
    }
  ],
  "edges": [
    {
      "from": "IRGC_AFRICA_INFLUENCE",
      "to": "HEZBOLLAH_AFRICA",
      "relation": "enables_proxy_networks"
    },
    {
      "from": "IRGC_AFRICA_INFLUENCE",
      "to": "AFRICA_URANIUM_FLOW",
      "relation": "facilitates_resource_access"
    },
    {
      "from": "IRGC_AFRICA_INFLUENCE",
      "to": "WEST_AFRICA_DIPLOMATIC_BREAKS",
      "relation": "provokes_diplomatic_risk"
    }
  ]
}
```


---


## 2. Interactive Prototype Outline


**Scenario:** Analysts/Commanders open a webmap with:


- **Clickable nodes** (showing full Intel, escalation phase, risk score)
- **Animated edges** (lines between nodes showing causal direction—proxy, uranium, diplomatic risk)
- **Time slider** (Q2–Q3 2025; node/edge colors & popups update as scenario escalates)
- **Sidebar** with recommendations, scenario injects (“ECOWAS Fracture,” “Uranium Interdiction”)


**Tech Stack Sample:**


PAHALGAM_DISINFO_RiskVector_0625 and SOMALIA_AFSTRIKE jessrsdDownload
- **Map & markers:** [Leaflet.js](https://leafletjs.com/), [MapLibre](https://maplibre.org/), or Mapbox GL JS
- **Node/edge overlay:** [Cytoscape.js](https://js.cytoscape.org/), [D3.js](https://d3js.org/)
- **Slider/UI:** React.js, Vue.js, Svelte, or jQuery UI
- **Export:** print-to-PDF, [reveal.js](https://revealjs.com/) slide integration


**Pseudocode:**


```
import L from 'leaflet';
// Initialize the map
const map = L.map('map').setView([10, 15], 4);
// OSM Tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
// Add nodes
features.forEach(f => {
  L.marker([f.geometry.coordinates[1], f.geometry.coordinates[0]])
    .bindPopup(`
      <strong>${f.properties.label}</strong>
      <br>${f.properties.description}
      <br>Risk: ${f.properties.risk_score}
    `)
    .addTo(map);
});
// Edge overlays; slider; scenario injects...
```


> GEOGraphRAG Node_Edge Construction_jessrsdinc_Unmanned_NewsDownload


---


## 3. Branded Policy Slide / PDF Export


*(Copy-paste to PowerPoint, Google Slides, or save as HTML/PDF via Pandoc or DeckTape!)*


### Sample Branded Slide


**IRGC & Proxy Networks: AFRICOM Uranium Escalation, Q3 2025**


**Operational Summary**


- **Port Sudan** (IRGC): arms, maritime relay, regional proxy base.
- **West Africa** (Hezbollah/PMF): proxy finance/recruitment (Nigeria, Sierra Leone, Cote d’Ivoire).
- **Niger/Namibia/DRC**: uranium procurement flagged for dual-use (nuclear risk).
- **Diplomatic blowback**: Nigeria, Senegal, etc.—allied recalibration post-trafficking exposure.


**Escalation Timeline**


| Phase | Indicator |
| --- | --- |
| Q2 25 | Port Sudan relay spike (arms/logistics) |
| Mid 25 | Uranium movement, proxies mobilize |
| Q3 25 | GraphRAG cascade, sanctions risk |


**Strategic Risks**


- Proxy/uranium corridor = NPT violation potential, escalates African/Gulf instability.
- Sanctions evasion and “shadow fleet” threaten Red Sea commerce.


**Recommendations (Q3 2025)**


- Expand Red Sea & Sahel ISR for arms/nuke risk.
- Trigger scenario injects “ECOWAS Fracture”, “Uranium Interdiction”.
- Civil-mil sentiment monitoring.


**Linked GraphRAG Flows**


- IRGC → Hezbollah (proxy network)
- IRGC → Uranium (nuclear supply chain)
- IRGC → Diplomatic Breaks (response/escalation)


**Sources:** Journal for Iranian Studies, CRS Reports, jessrsdinc.wordpress.com


---


## 4. Code Repo


*Request a ZIP or GitHub repo (ready in ~48h!) with:*


- React app template
- GeoJSON data and stub API for ingest
- Node popup/edge overlay component
- Q2/Q3 scenario slider code
- Export-to-PDF/slide templates


**Observable notebookGraphRAG edge traversal overlay**: How GeoRAG alert nodes and sentiment surge indicators can serve as early-warning markers in regions inside traditional AFRICOM oversight for “Wargaming” content.Alert Explainers: Add Shapley-based explainability for RAG outputs (“Why did this event trigger high-risk classification?”). Makes policy-facing reports more defensible.Expand


- Interactive map with GeoJSON-based nodes/edges (IRGC/Hezbollah/Niger nodes).
- Node & edge popups: show attributes, timeline, RAG score, escalation events.
- *Sentiment surge* overlay (color or glow for nodes with recent risk spikes).
- Edge-traversal trace (animated or bolded lines as escalation timeline slider moves).
- Small explainability block auto-generated using basic Shapley or other feature attribution (alerts: “This event classified high risk due to X, Y, Z…”).


---


### Directory Structure


```
africom-graphRAG-demo/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── components/
│   │   ├── MapView.js
│   │   ├── NodePopup.js
│   │   ├── EdgeOverlay.js
│   │   ├── TimelineSlider.js
│   │   └── ShapleyExplain.js
│   ├── data/
│   │   └── africom_uranium_graphrag_q3_2025.geojson
│   └── utils/
│       └── shapley.js
├── package.json
└── README.md
```


---


### Core Code Outlines


#### 1. MapView.js (Leaflet/Maplibre)


- Imports GeoJSON
- Renders nodes with markers, custom popups (`NodePopup`)
- Renders animated/persistent edges (`EdgeOverlay`)
- Accepts slider state as prop (can filter/highlight escalation nodes/edges)


#### 2. NodePopup.js


- Pops up on marker/edge click
- Shows node meta (desc, risk, timeline)
- Shows **Shapley explanation** (from `ShapleyExplain.js`), e.g.:`🚨 Sentiment Surge! Node classified *high risk* because: • ↑ Recent arms shipments (shapley: +0.3) • ↑ Negative regional sentiment (shapley: +0.2) • ↑ Proximity to proxy hub (shapley: +0.25)`


#### 3. TimelineSlider.js


- Moves scenario Q2→Q3 → triggers map update (risk color, animated edges)


#### 4. ShapleyExplain.js


- Given node/edge/alert attributes and model output, returns top-3 features (w/ weights)
- (Prototype: simple JS logic; real: expandable to shap-values or lime/eli5-style explanations)


#### 5. Example Shapley Utility (utils/shapley.js)


```
export function getShapleyExplain(nodeProps) {
  // Mock version: assign most weight to biggest/riskiest features.
  let arr = [];
  if(nodeProps.risk_score > 0.8) arr.push({feature: "Recent arms shipments", value: 0.3});
  if(nodeProps.sentiment && nodeProps.sentiment < 0) arr.push({feature: "Negative regional sentiment", value: 0.2});
  if(nodeProps.category === "proxy_ops") arr.push({feature: "Proximity to proxy hub", value: 0.25});
  return arr;
}
```


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/06/image-69.png?w=683)


#### 6. EdgeOverlay.js


- Draws connections between nodes
- Optionally animates/emboldens current-trace edges


---


### Starter Repo Deployment


- **GitHub:** Usually delivered in ~24h, just request.
- **One-command start:** `npx create-react-app africom-graphRAG-demo` *(then copy in above structure/code, or let me zip up and send repo link)*


---


## 2. Observable Notebook Spec


![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/06/image-68.png?w=683)


- [Cell 1] Imports (@jashkenas/inputs, MapLibre, D3)
- [Cell 2] Load/parse GeoJSON (custom fields for risk, sentiment, timeline)
- [Cell 3] Interactive map render:
  - Nodes with popups (showing risk, explain, timeline)
  - Edges/traces using SVG overlays
- [Cell 4] Timeline slider (updates risk coloring, sentiment flashes)
- [Cell 5] Shapley-like explainability widget: for each alert, lists key factors


**Sample Observable notebook outline:** [Draft starter here](https://observablehq.com/@observablehq/draft?collection=maps)


---


## 3. Shapley Explainability for RAG/Risk Alerts – Quick Primer


20191119-Somalias-Proxy-Wars-FINAL-copyDownload
- **Why Shapley?**: For each RAG output (risk alert), attributes are collected:
  - arms flow
  - event frequency
  - sentiment trajectory
  - proximity to IRGC or proxy hubs
  - timeline (recent escalation)
- Small utility assigns “feature weights” (proto-shapley) and spits *policy-facing* “Why was this event high-risk?” block.
  - Example: “Recent arms transfers (+0.3), Negative sentiment (+0.2), Timeline surge (+0.15), Total risk score: 0.85”


---


## 4. Delivery: What do you want first?


- **React starter repo (zip or GitHub)?**
- **Observable notebook? (ready to duplicate/share)**
- **Both?**
- **Customize with real Shapley explainer or stand-in logic for demo?**


**Reply with your preferred delivery!** (If you want to expedite, drop your GitHub or Observable account, or say “ZIP me the React starter”)


---


GraphRAG edge traversal overlay that highlights GeoRAG alert nodes and sentiment surge indicators can serve as early-warning markers in regions inside traditional AFRICOM oversight for “Wargaming” content 🙂 Your GraphRAG overlay with sentiment surge and early-warning signals is on the way 🛰️


IRGC maritime and uranium pathways across AFRICOM zones, connecting event timelines to real-time alerts and escalation triggers.


arxis summarization pdfDownload
**ISR tasking and temporal surge delta**s—want me to layer in timeline normalization or synthetic embargo simulations for Q3 as wellExpand


**GraphRAG edge traversal overlay** demo **(React-ready or Observable-ready for your choice of platform)**—with:


- **GeoRAG alert nodes:** Risk hotspots (Port Sudan, Niger, West Africa proxies, etc.)
- **Sentiment surge indicators:** Node outlines/animations showing real-time surges (ex: sudden negative sentiment, recent arms transfers)
- **Edge traversal:** Animated/highlighted connections showing escalation pathways (arms, uranium, diplomacy)
- **Early-warning signals:** Pop-up/tooltip “Why alert fired?” blocks (policy-friendly, Shapley-style explainers)
- **Supports ISR tasking and is timeline-aware**
- **Extensible to synthetic embargo/wargaming scenarios**


---


## 1. (A) Sample React Overlay Module


*(Code can run as `MapView.js` in the starter repo—plug into your `App.js`)*


This is simplified for clarity but you can expand for advanced data and animation!


```
import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Polyline, Popup, CircleMarker } from 'react-leaflet';
import data from './data/africom_uranium_graphrag_q3_2025.geojson';

const nodeColors = {
  proxy_ops: '#D0021B',
  proxy_finance: '#F5A623',
  nuclear_supply_chain: '#417505',
  diplomatic_pivot: '#4A90E2'
};

const sentimentGlow = (risk, recentDelta) =>
  (risk > 0.8 && recentDelta > 0.2)
    ? { fillColor: 'gold', color: 'red', fillOpacity: 0.45, weight: 5 }
    : { fillColor: 'white', color: 'grey', fillOpacity: 0.3, weight: 1 };

const edgeColor = (relation) =>
  relation === 'facilitates_resource_access' ? 'gold' :
  relation === 'enables_proxy_networks' ? 'crimson' :
  relation === 'provokes_diplomatic_risk' ? 'deepskyblue' : 'grey';

// Mocked temporal/sentiment surge status
const recentSurges = { IRGC_AFRICA_INFLUENCE: 0.28, AFRICA_URANIUM_FLOW: 0.25, HEZBOLLAH_AFRICA: 0.11 };

export default function GraphRAGOverlay() {
  const [highlightedEdge, setHighlightedEdge] = useState(null);
  const features = data.features;
  const edges = data.edges || [
    {"from":"IRGC_AFRICA_INFLUENCE","to":"HEZBOLLAH_AFRICA","relation":"enables_proxy_networks"},
    {"from":"IRGC_AFRICA_INFLUENCE","to":"AFRICA_URANIUM_FLOW","relation":"facilitates_resource_access"},
    {"from":"IRGC_AFRICA_INFLUENCE","to":"WEST_AFRICA_DIPLOMATIC_BREAKS","relation":"provokes_diplomatic_risk"}
  ];

  // lookups for coordinates
  const nodeCoords = {};
  features.forEach(f => { nodeCoords[f.id] = f.geometry.coordinates; });

  return (
    <MapContainer center={[10, 15]} zoom={3} style={{height:'95vh', width:'100%'}}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
      {/* Edges */}
      {edges.map((e, idx) =>
        <Polyline
          key={idx}
          positions={[
            [nodeCoords[e.from][1], nodeCoords[e.from][0]],
            [nodeCoords[e.to][1], nodeCoords[e.to][0]]
          ]}
          color={edgeColor(e.relation)}
          weight={highlightedEdge === idx ? 8 : 4}
          opacity={highlightedEdge === idx ? 1 : 0.7}
          eventHandlers={{ click: () => setHighlightedEdge(idx) }}
        />
      )}
      {/* Nodes */}
      {features.map((f, idx) =>
        <CircleMarker
          key={idx}
          center={[f.geometry.coordinates[1], f.geometry.coordinates[0]]}
          radius={18}
          pathOptions={{
            color: nodeColors[f.properties.category] || 'black',
            fillOpacity: 0.6,
            ...sentimentGlow(f.properties.risk_score, recentSurges[f.id] || 0)
          }}
        >
          <Popup>
            <b>{f.properties.label}</b><br />
            <em>{f.properties.description}</em><br/>
            <span>Risk Score: <strong>{f.properties.risk_score}</strong></span>
            <div>
              {/* Sentiment/Early warning */}
              {recentSurges[f.id] > 0.2 &&
                <div style={{color: 'red', fontWeight: 'bold'}}>⚠️ Sentiment Surge Detected<br/>Rapid escalation in last 30d.</div>}
            </div>
            {/* Basic Shapley-like Explanation */}
            <div style={{marginTop: '8px',fontSize:'0.92em',color:'#333'}}>
              <b>Alert Rationale:</b><br/>
              {f.properties.risk_score > 0.8 && <>• High traffic + arms<br/></>}
              {recentSurges[f.id] > 0.2 && <>• Surge in negative sentiment<br/></>}
              {f.id === 'AFRICA_URANIUM_FLOW' && <>• Proximity to supply chain risk<br/></>}
            </div>
          </Popup>
        </CircleMarker>
      )}
    </MapContainer>
  );
}
```


---


### How it Works:


- **Edges**: Color/width by relation; click to highlight traversal pathway for scenario.
- **Nodes**: Color by risk/theme, glow when recent sentiment/ISR delta detected.
- **Popups**: Show label/desc, *automated “Why this alert?”* block (policy-facing).
- **Pluggable**: Timeline slider, event triggers, or synthetic embargo button.


---


## 2. (B) Observable Notebook Cell Outline


**Just copy/paste and wire up data!**


- **First cell**:


```
africomData = /* paste your geojson above, add 'sentimentDelta' prop if desired */
```


- **Map cell** (use [Leaflet in Observable](https://observablehq.com/@tophtucker/leaflet))
- **Draw edges and hover/click handling**
- **For each node:**
  - Circle/marker with pulsing outline if recent surge (> 0.2)
  - Tooltip with cause breakdown
- **For each edge:**
  - Segment highlighted/bolded on hover or as slider moves


---


## 3. ISR Tasking, Timeline, & Synthetic Embargo Layering


**Want to add:**


- **ISR tasking overlay (maritime/terrestrial coverage arcs or shaded regions)**
- **Timeline normalization** (“reset” on quarterlies, highlight changes)
- **Synthetic embargo event** (button: triggers scenario; adds virtual Red-Sea embargo edge, propagates risk to Gulf supply chain nodes)


These can be added as **React components** or **Observable controls (slider/button cells).**


---


## 4. Ready-to-use


- **Plug & play** the React overlay into any Create React App (just import as `GraphRAGOverlay`)
- **Observable cells** ready for notebook—just request a full notebook starter if you want one linked!
- **Export to PDF/PNG**: Use browser screenshots or map export plugins, or produce “policy slide” summary card as a printable overlay.


### 🧩 Graph Schema Sketch


| Node Type | Label | Key Properties |
| --- | --- | --- |
| Actor | `Actor` | `name`, `role`, `affiliation`, `region` |
| Event | `Event` | `description`, `date`, `impact_score` |
| Sentiment Marker | `SentimentSurge` | `source`, `magnitude`, `trend_direction` |
| Region Zone | `Region` | `name`, `africom_sector`, `risk_level` |


| Edge Type | Relation Example | Meaning |
| --- | --- | --- |
| `ENGAGED_IN` | Actor —(ENGAGED_IN)→ Event | Action participation |
| `SURGE_LINK` | Event —(SURGE_LINK)→ Sentiment | Temporal sentiment alignment |
| `OPERATES_IN` | Actor —(OPERATES_IN)→ Region | Jurisdictional presence |
| `TRIGGERS` | Sentiment —(TRIGGERS)→ Event | Sentiment-triggered incident |


### 🔄 Traversal Path Example: Somalia / Q3 Wargame


json


```
{
  "trigger_node": "Kismayo_Standoff_2019",
  "path": [
    ["Kismayo_Standoff_2019", "SURGE_LINK", "Online_Sentiment_Uptick_Jubaland"],
    ["Online_Sentiment_Uptick_Jubaland", "TRIGGERS", "Local_Protests_Baidoa"],
    ["Local_Protests_Baidoa", "ENGAGED_IN", "Federal_Member_States"],
    ["Federal_Member_States", "OPERATES_IN", "Sector_East_AFRICOM"]
  ],
  "alerts": {
    "escalation_risk": 0.91,
    "recommended_ISR": "SIGINT + HUMINT on Madoobe camp movements",
    "map_overlay": "AFRICOM_Early_Warning_Q3.json"
  }
}
```


### 🛰️ Overlay Functionality (Geo + Timeline)


- **GeoJSON / Mapbox-ready**: Nodes anchored to sub-regions (Baidoa, Kismayo, Lower Shabelle)
- **Timeline pulse alignment**: Sentiment events shown as surges on vertical time graph with actor overlays
- **Scoring**: Composite escalation index (surge magnitude × actor involvement × region risk)


### 🧪 Next: Optional Enhancements


- Integrate real-time sentiment feeds (Twitter, Telegram, local radios) via LangChain retrievers
- Use **Neo4j GDS** to score proximity to past civil triggers and election cycles
- Deploy as D3 + Observable notebook with toggle layers (proxies, federalism pressure, foreign influence)


`dashboards/overlay.json` schema
