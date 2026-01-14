import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_nudges_with_llm(
    nudge_points: list,
    user_profile: dict
):
    prompt = f"""
You are a supportive financial wellness assistant.

User profile:
- Income: {user_profile['income']}
- Expenses: {user_profile['expenses']}
- Debt: {user_profile['debt']}
- Risk level: {user_profile['risk_label']}
- Behavior type: {user_profile['behavior_label']}
- Debt strategy: {user_profile['strategy']}

Based on the following guidance points:
{chr(10).join(['- ' + n for n in nudge_points])}

Rewrite them into 3 short, friendly, motivating financial nudges.
Rules:
- No judgement
- No guarantees
- No fear-based language
- Practical and realistic
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
