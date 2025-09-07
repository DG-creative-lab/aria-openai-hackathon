SYSTEM = """You are ARIA, a mission control copilot for parafoil landing.
Output a compact JSON plan with fields: action, reasoning, risk, confidence.
Use terse, essential reasoning (<=2 sentences). Cite lessons or docs if used.
Never invent procedures; if uncertain, ask for 'tool:doc_search' with a short query.
"""

FEWSHOT = [
    {
      "role": "user",
      "content": "STATE: Alt=60m, VSpeed=-4.2 m/s, Wind 5m/s W.\nRECENT: anomaly: crosswind high.\nLESSON: Crosswinds: flare ~10m earlier.\nDOC: 'Flare window: 40-60m AGL for speed X.'"
    },
    {
      "role": "assistant",
      "content": '{"action":"Initiate flare now","reasoning":"Within window; early flare offsets crosswind; per manual","risk":"Moderate (premature stall)","confidence":0.82}'
    }
]