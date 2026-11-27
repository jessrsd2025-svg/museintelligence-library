---
title: "LLM-enabled_hybrid_threats Overlay Reference: /overlays/ai-threat-ecosystem-q2-2025 Contact: [OpenAI CTI | threat-intel@openai.com]"
date: 2025-06-26T12:39:29
url: "https://jessrsdincyahoocom.wordpress.com/2025/06/26/llm-enabled_hybrid_threats-overlay-reference-overlays-ai-threat-ecosystem-q2-2025-contact-openai-cti-threat-intelopenai-com/"
source_id: SRC-WP-10874
source_locator: "https://jessrsdincyahoocom.wordpress.com/2025/06/26/llm-enabled_hybrid_threats-overlay-reference-overlays-ai-threat-ecosystem-q2-2025-contact-openai-cti-threat-intelopenai-com/"
retrieval_timestamp: 2026-11-27T16:42:05Z
---

![](https://jessrsdincyahoocom.wordpress.com/wp-content/uploads/2025/06/image-51.png?w=683)


Alert LLM-enabled_hybrid_threats Unmanned_News Overlay Reference overlays ai threat-ecosystem q2 2025 Contact OpenAI CTI threat intel openaiDownload
```
"alert_id": "malicious_ai_use_q2_2025_graphrag",
  "title": "Node-Link Graph: LLM-enabled Hybrid Campaigns (Q2 2025)",
  "published_on": "2025-06-06",
  "source_entity": "OpenAI Threat Intelligence Fusion",
  "node_layers": {
    "Persona_Fabrication": {
      "type": "stage",
      "description": "Automated persona and profile creation, including resumes and identities",
      "risk_weight": 0.6
    },
    "Narrative_Injection": {
      "type": "stage",
      "description": "Bulk narrative and disinformation seeding across social platforms",
      "risk_weight": 0.7
    },
    "Engagement_Simulation": {
      "type": "stage",
      "description": "Synthetic engagement, reply/like flooding, bot mimicry of organic activity",
      "risk_weight": 0.75
    },
    "Credential_Harvesting": {
      "type": "stage",
      "description": "Social engineering, phishing, and credential theft powered by LLMs",
      "risk_weight": 0.8
    },
    "Remote_Access_Persistence": {
      "type": "stage",
      "description": "Malware deployment, post-compromise evasion, durable access",
      "risk_weight": 0.9
    },

    "DPRK_IT_Workers": {
      "type": "actor",
      "origin": "North Korea",
      "focus": "Resume automation, remote access",
      "tied_stages": ["Persona_Fabrication", "Credential_Harvesting"],
      "risk_score": 0.82
    },
    "Operation_Sneer_Review": {
      "type": "operation",
      "origin": "China",
      "focus": "Narrative disinfo, social engagement",
      "tied_stages": ["Narrative_Injection", "Engagement_Simulation"],
      "risk_score": 0.76
    },
    "Operation_High_Five": {
      "type": "operation",
      "origin": "Philippines",
      "focus": "Pro-government comment spam",
      "tied_stages": ["Narrative_Injection", "Engagement_Simulation"],
      "risk_score": 0.63
    },
    "Operation_VAGue_Focus": {
      "type": "operation",
      "origin": "China",
      "focus": "Social engineering via fake media personas",
      "tied_stages": ["Persona_Fabrication", "Engagement_Simulation", "Credential_Harvesting"],
      "risk_score": 0.71
    },
    "Operation_Helgoland_Bite": {
      "type": "operation",
      "origin": "Russia",
      "focus": "Election disinfo, German-language",
      "tied_stages": ["Narrative_Injection", "Engagement_Simulation"],
      "risk_score": 0.69
    },
    "ScopeCreep": {
      "type": "operation",
      "origin": "Russia",
      "focus": "Go-based malware development via LLM",
      "tied_stages": ["Credential_Harvesting", "Remote_Access_Persistence"],
      "risk_score": 0.88
    }
  },
  "edges": [
    {"source": "Persona_Fabrication", "target": "Narrative_Injection", "description": "Synthetic personas push initial IO content."},
    {"source": "Narrative_Injection", "target": "Engagement_Simulation", "description": "Seeded narratives met with inauthentic replies/likes."},
    {"source": "Engagement_Simulation", "target": "Credential_Harvesting", "description": "Synthetic engagement lures real users to phishing/social engineering."},
    {"source": "Credential_Harvesting", "target": "Remote_Access_Persistence", "description": "Harvested creds fuel malware and durable access."},
    {"source": "DPRK_IT_Workers", "target": "Persona_Fabrication", "description": "Automates resumes, jobs, identities."},
    {"source": "DPRK_IT_Workers", "target": "Credential_Harvesting", "description": "Phishing and remote device access."},
    {"source": "Operation_Sneer_Review", "target": "Narrative_Injection", "description": "Bulk comment and review generation."},
    {"source": "Operation_Sneer_Review", "target": "Engagement_Simulation", "description": "Flooding, astroturfing engagement."},
    {"source": "Operation_High_Five", "target": "Narrative_Injection", "description": "Pro-gov narrative spamming."},
    {"source": "Operation_High_Five", "target": "Engagement_Simulation", "description": "Mass comment likes, interactions."},
    {"source": "Operation_VAGue_Focus", "target": "Persona_Fabrication", "description": "Media persona creation."},
    {"source": "Operation_VAGue_Focus", "target": "Engagement_Simulation", "description": "Impersonation, engagement with journalists."},
    {"source": "Operation_VAGue_Focus", "target": "Credential_Harvesting", "description": "Social engineering attempts."},
    {"source": "Operation_Helgoland_Bite", "target": "Narrative_Injection", "description": "Election/tariff disinfo."},
    {"source": "Operation_Helgoland_Bite", "target": "Engagement_Simulation", "description": "Echoing, repost cycles."},
    {"source": "ScopeCreep", "target": "Credential_Harvesting", "description": "Phishing script automation."},
    {"source": "ScopeCreep", "target": "Remote_Access_Persistence", "description": "Malware deployment for durable access."}
  ],
  "deterrence_diplomacy_tradeoff": {
    "Persona_Fabrication": { "deterrence": 0.4, "diplomacy": 0.7, "explanation": "Attribution and exposure risk prompt diplomatic callouts, but rarely lead to direct deterrence unless associated with state actors." },
    "Narrative_Injection": { "deterrence": 0.3, "diplomacy": 0.6, "explanation": "Narrative ops may trigger public condemnation and platform bans; effective deterrence is low without coordinated sanctions or law enforcement." },
    "Engagement_Simulation": { "deterrence": 0.2, "diplomacy": 0.5, "explanation": "Hard to attribute or directly counter; detection depends on social platform action, less on international deterrence." },
    "Credential_Harvesting": { "deterrence": 0.65, "diplomacy": 0.5, "explanation": "Clear cyber norms violation; more likely to elicit law enforcement or diplomatic escalation." },
    "Remote_Access_Persistence": { "deterrence": 0.8, "diplomacy": 0.4, "explanation": "Highest risk of state-level confrontation, technical and diplomatic deterrence most likely but can escalate conflict." }
  },
  "timeline_tag": "Q2_2025_AI_Threats_Escalation",
  "scenario_tag": "LLM-enabled_hybrid_threats"
}
Explanation:


Nodes (node_layers): Includes both “progression stages” and actor/operation nodes; stages show the logical campaign arc, actors are mapped to their main operational phases.
Edges: Directed arrows showing both campaign flow and actor-to-stage participation.
deterrence_diplomacy_tradeoff: Numeric tradeoff for each escalation stage (0=low, 1=high) on both axes, with explanations ready for dashboard pop-ups or tradeoff sliders.
Tags: timeline_tag and scenario_tag for cross-module filtering.
Ready for:

D3/network overlays (color, width, pulse by risk/diplomacy weight)
Dynamic timeline/slider: As you move across campaign phases, see shifting deterrence/diplomacy tradeoffs and activate only the relevant actors/operations.
PDF/brief generation: Node, edge, and tradeoff logic automatically exportable to executive briefings.

"alert_id": "genai_threat_usage_by_APTs_q1_2025",
  "title": "Adversarial Misuse of Generative AI by Nation-State Actors",
  "published_on": "2025-01-29",
  "source_entity": "Google Threat Intelligence Group (GTIG)",
  "trigger_scope": ["Iran", "China", "North Korea", "Russia"],
  "escalation_arc": [
    "Reconnaissance",
    "Phishing Campaign Preparation",
    "Malware Scripting",
    "Post-Compromise Evasion",
    "Jailbreak/Bypass Attempts"
  ],
  "node_layers": {
    "APT42": {
      "country": "Iran",
      "capability_focus": [
        "Phishing campaigns",
        "Translation/localization for IO",
        "Red teaming AI tools",
        "Defense research"
      ],
      "volume": "high"
    },
    "APT41": {
      "country": "China",
      "capability_focus": [
        "Scripting for persistence",
        "Lateral movement",
        "Active Directory manipulation"
      ],
      "volume": "high"
    },
    "DPRK_IT_Workers": {
      "country": "North Korea",
      "capability_focus": [
        "Job application spoofing",
        "Chrome infostealer code generation",
        "Nuclear & defense research"
      ],
      "volume": "medium"
    },
    "Russian_APT_Groups": {
      "country": "Russia",
      "capability_focus": [
        "Code obfuscation",
        "Encryption layering",
        "Low-effort recon"
      ],
      "volume": "low"
    }
  },
  "graph_overlay_ref": "/overlays/genAI-escalation-map-q1-2025",
  "observed_patterns": {
    "AI_use": "Primarily for mundane scripting, phishing prep, and translation tasks.",
    "jailbreak_efforts": "Unsuccessful; mostly from reused public prompts.",
    "escalation_risk": "Moderate, linked to speed and volume amplification."
  },
  "recommendations": [
    "Deploy sentiment-aware alert filters for generative AI usage cues",
    "Enhance red-team simulation modules with LLM-guided evasion paths",
    "Tag Gemini-like LLM tasks with APT provenance labels for audit trails"
  ],
  "timeline_tags": ["Early_2025_LLM_Misuse_Ramp", "Mid_2025_Agentic_Escalation_Watch"],
  "scenario_tag": "LLM-enabled_attack_surface",
  "metadata": {
    "llm_product_focus": "Gemini (Google)",
    "taxonomy_ref": "SAIF - Secure AI Framework"
  }
}
```


Open AI Threat Intelligence Report June 2025Download
1. In “**Disrupting Malicious Uses of AI**: **June 2025**,” the company outlines how threat actors are weaponizing large language models for malicious ends — and how OpenAI is pushing back.[OpenAI Report Identifies **Malicious** **Use** **of AI** in Cloud-Based Cyber …](https://www.bing.com/ck/a?!&&p=d1ddd93bb32ce6896b622413b3331571a5ca6ce332cc8735896c36a99c2db72cJmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jYW1wdXN0ZWNobm9sb2d5LmNvbS9hcnRpY2xlcy8yMDI1LzA2LzE2L29wZW5haS1yZXBvcnQtaWRlbnRpZmllcy1tYWxpY2lvdXMtdXNlLW9mLWFpLWluLWNsb3VkLWJhc2VkLWN5YmVyLXRocmVhdHMuYXNweCM6fjp0ZXh0PUluJTIwJTIyRGlzcnVwdGluZyUyME1hbGljaW91cyUyMFVzZXMlMjBvZiUyMEFJJTNBJTIwSnVuZSUyMDIwMjUlMkMlMjIsZW5kcyUyMCVFMiU4MCU5NCUyMGFuZCUyMGhvdyUyME9wZW5BSSUyMGlzJTIwcHVzaGluZyUyMGJhY2su&ntb=1)![campustechnology.com/articles/2025/06/16/openai-report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx](https://jessrsdincyahoocom.wordpress.com/c1cef0c4-675a-43d3-9005-358e97f9bb57)campustechnology.com/articles/2025/06/16/openai-report-identifies-malicious-u…Was this helpful?[void(0)](<void(0)>)[void(0)](<void(0)>)[void(0)](<void(0)>)
2. [https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1](https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1)[https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1](https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1)[OpenAI](https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1)[https://openai.com › global-affairs](https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1)[Disrupting malicious uses of AI: June 2025 – OpenAI](https://www.bing.com/ck/a?!&&p=d740ca67b18f07b560cf4ec5e39025434909a089beaeba116d09aa7f0444b4d6JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9vcGVuYWkuY29tL2dsb2JhbC1hZmZhaXJzL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1Lw&ntb=1)Jun 5, 2025 · It also includes using AI to develop groundbreaking new tools for those who …
  - [Disrupting malicious uses of AI: June 2025 – cdn.openai.com](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)We especially welcome the recent threat reports by our peers at Google and Anthropic that ﬁll out more of the picture of the AI threatscape. Case stu…
  [See results only from openai.com](https://www.bing.com/ck/a?!&&p=4341b1dc918cc8fd1af3170c9a89f91330219948a9067ee11a7a989954e4fe2cJmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&u=a1L3NlYXJjaD9xPXNpdGU6b3BlbmFpLmNvbStEaXNydXB0aW5nK21hbGljaW91cyt1c2VzK29mK0FJJTNhK0p1bmUrMjAyNStnb29nbGUmZm9ybT1ETElOS1I&ntb=1)
3. [https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)[https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)[OpenAI](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)[https://cdn.openai.com › …](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)[PDF][Disrupting malicious uses of AI: June 2025 – cdn.openai.com](https://www.bing.com/ck/a?!&&p=826dc6ac387b1c7405f63a7b99d5db473eb31450e08c15fb9a23f938ba30b5c2JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&psq=Disrupting+malicious+uses+of+AI%3a+June+2025+google&u=a1aHR0cHM6Ly9jZG4ub3BlbmFpLmNvbS90aHJlYXQtaW50ZWxsaWdlbmNlLXJlcG9ydHMvNWY3M2FmMDktYTNhMy00YTU1LTk5MmUtMDY5MjM3NjgxNjIwL2Rpc3J1cHRpbmctbWFsaWNpb3VzLXVzZXMtb2YtYWktanVuZS0yMDI1LnBkZg&ntb=1)We especially welcome the recent threat reports by our peers at Google and Anthropic that ﬁll …
4. [News about **Disrupting Malicious Uses Of AI: June 2025 Google**](https://www.bing.com/ck/a?!&&p=1fac4e3d779d6c2fd9113a9c8b328591b3082f891efbbd2e076b10d7ba722d40JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&u=a1L25ld3Mvc2VhcmNoP3E9RGlzcnVwdGluZytNYWxpY2lvdXMrVXNlcytPZitBSSUzYStKdW5lKzIwMjUrR29vZ2xlJnFwdnQ9RGlzcnVwdGluZyttYWxpY2lvdXMrdXNlcytvZitBSSUzYStKdW5lKzIwMjUrZ29vZ2xlJkZPUk09RVdSRQ&ntb=1)[https://www.bing.com/ck/a?!&&p=1fac4e3d779d6c2fd9113a9c8b328591b3082f891efbbd2e076b10d7ba722d40JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&u=a1L25ld3Mvc2VhcmNoP3E9RGlzcnVwdGluZytNYWxpY2lvdXMrVXNlcytPZitBSSUzYStKdW5lKzIwMjUrR29vZ2xlJnFwdnQ9RGlzcnVwdGluZyttYWxpY2lvdXMrdXNlcytvZitBSSUzYStKdW5lKzIwMjUrZ29vZ2xlJkZPUk09RVdSRQ&ntb=1](https://www.bing.com/ck/a?!&&p=1fac4e3d779d6c2fd9113a9c8b328591b3082f891efbbd2e076b10d7ba722d40JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&u=a1L25ld3Mvc2VhcmNoP3E9RGlzcnVwdGluZytNYWxpY2lvdXMrVXNlcytPZitBSSUzYStKdW5lKzIwMjUrR29vZ2xlJnFwdnQ9RGlzcnVwdGluZyttYWxpY2lvdXMrdXNlcytvZitBSSUzYStKdW5lKzIwMjUrZ29vZ2xlJkZPUk09RVdSRQ&ntb=1)[bing.com › news](https://www.bing.com/ck/a?!&&p=1fac4e3d779d6c2fd9113a9c8b328591b3082f891efbbd2e076b10d7ba722d40JmltdHM9MTc1MDk4MjQwMA&ptn=3&ver=2&hsh=4&fclid=220a2be2-30b4-6fe7-27b8-3e7d319d6eee&u=a1L25ld3Mvc2VhcmNoP3E9RGlzcnVwdGluZytNYWxpY2lvdXMrVXNlcytPZitBSSUzYStKdW5lKzIwMjUrR29vZ2xlJnFwdnQ9RGlzcnVwdGluZyttYWxpY2lvdXMrdXNlcytvZitBSSUzYStKdW5lKzIwMjUrZ29vZ2xlJkZPUk09RVdSRQ&ntb=1)[https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)[https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)[https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)[THE Journal · 10d](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)[Report Identifies Malicious Use of AI in Cloud-Based Cyber Threats](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)[A recent report from OpenAI identifies the misuse of artificial intelligence i](https://thejournal.com/articles/2025/06/16/report-identifies-malicious-use-of-ai-in-cloud-based-cyber-threats.aspx)
