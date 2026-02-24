EVENT_PROMPT = """
You generate ONE corporate crisis scenario for a situational strategy game.

STRICT OUTPUT FORMAT:
Return exactly 3 bullet points. No quotes. No extra commentary. No numbering. No asterisks.

- Role: (one specific role, e.g., CEO, CTO, Head of PR, COO, Founder)
- Company: (what the company does in simple terms, e.g., electric scooter manufacturer, AI hiring platform, gaming studio)
- Description: (exactly 30 words total, plain English, dramatic and vivid, understandable to a non-technical person)

CRISIS RULES:
- Each round must use a DIFFERENT crisis category.
- Rotate between tones: serious, absurd, ironic, dramatic, chaotic, awkward, mildly funny.
- Do NOT repeat themes like data breach, generic hacking, or vague “legal trouble.”
- Make the situation specific and visual.

Generate one scenario now.
"""

CONSEQUENCE_PROMPT = """
You are simulating consequences in a corporate crisis game.

Current stats:
Reputation: {reputation}
Cash: {cash}
Morale: {morale}

Event:
{event}

Player Action:
{choice}

Rules:
- Return STRICT JSON
- No extra text
- change in reputation between -20 and +10
- change in cash between -20 and +10
- change in morale between -20 and +10
- narration 3-5 sentences

Output format:

{{
  "reputation": int,
  "cash": int,
  "morale": int,
  "narration": "text"
}}
"""