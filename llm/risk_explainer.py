import os
from dotenv import load_dotenv

load_dotenv()
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_risk_with_llm(
    model_name,
    risk_label,
    risk_prob,
    user_features
):
    prompt = f"""
You are a responsible financial AI assistant.

Model used: {model_name}
Predicted Risk Level: {risk_label}
Risk Probability: {risk_prob:.2f}

User financial profile:
- Monthly income: {user_features['income']}
- Monthly expenses: {user_features['expenses']}
- Total debt: {user_features['debt']}
- Credit utilization: {user_features['credit_util']}
- Expense ratio: {user_features['expense_ratio']:.2f}
- Debt-to-income ratio: {user_features['debt_to_income']:.2f}

Task:
1. Explain WHY this risk level was predicted
2. Highlight the most important contributing factors
3. Suggest 2 realistic improvements
4. Do NOT give legal or guaranteed financial advice
5. Keep the explanation simple and human-friendly
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
