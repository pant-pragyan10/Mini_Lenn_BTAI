import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_behavior_with_llm(
    behavior_label: str,
    impulse_score: float,
    saving_score: float
):
    prompt = f"""
You are a financial behavior assistant.

User behavior classification:
- Behavior type: {behavior_label}
- Impulse score: {impulse_score}
- Saving discipline score: {saving_score}

Explain:
1. What this behavior means in simple terms
2. How it impacts financial health
3. 2 gentle suggestions to improve behavior (no judgement)

Keep the tone supportive and non-alarming.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
