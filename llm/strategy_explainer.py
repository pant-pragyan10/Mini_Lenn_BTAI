import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_strategy_with_llm(
    strategy_output: dict,
    income: float,
    expenses: float,
    debt: float,
    risk_label: str
):
    prompt = f"""
You are a responsible financial AI assistant.

User profile:
- Income: {income}
- Expenses: {expenses}
- Total Debt: {debt}
- Risk Level: {risk_label}

System-selected strategy:
- Strategy: {strategy_output['strategy']}
- Monthly repayment target: {strategy_output['monthly_target']}
- Reason: {strategy_output['reason']}

Explain:
1. Why this strategy fits the user's situation
2. Why a more aggressive approach might be risky
3. Give 2 practical, safe improvement suggestions

Avoid guarantees or legal/financial commitments.
Use simple, supportive language.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content



