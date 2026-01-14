# FEATURE 1


import streamlit as st

from ml.predictor import predict_risk
from llm.risk_explainer import explain_risk_with_llm

st.set_page_config(page_title="Mini Lenn BTai", layout="centered")

st.title("Mini Lenn BTai – Debt Risk Intelligence")



# Feature 1

st.header("1. Debt Risk Prediction")

st.markdown(
"""
This feature demonstrates:
- Interpretable ML (Logistic Regression)
- High-performance ML (XGBoost)
- Responsible LLM explanations using Groq
"""
)

income = st.number_input("Monthly Income", min_value=10000, value=50000, step=1000)
expenses = st.number_input("Monthly Expenses", min_value=5000, value=30000, step=1000)
debt = st.number_input("Total Outstanding Debt", min_value=0, value=200000, step=5000)
credit_util = st.slider("Credit Utilization Ratio", 0.0, 1.0, 0.4)

expense_ratio = expenses / income if income > 0 else 0
debt_to_income = debt / (income * 12) if income > 0 else 0

user_input = {
    "income": income,
    "expenses": expenses,
    "debt": debt,
    "credit_util": credit_util,
    "expense_ratio": expense_ratio,
    "debt_to_income": debt_to_income
}

model_choice = st.selectbox(
    "Select Risk Model",
    ["logistic", "xgboost"]
)

# ---------------- PREDICTION ----------------

if st.button("Analyze Debt Risk"):
    label, prob = predict_risk(user_input, model_choice)
    st.session_state['risk_label'] = label
    st.session_state['risk_prob'] = prob
    
    with st.spinner("Generating explanation..."):
        explanation = explain_risk_with_llm(
            model_name=model_choice,
            risk_label=label,
            risk_prob=prob,
            user_features=user_input
        )
    st.session_state['risk_explanation'] = explanation

if 'risk_label' in st.session_state:
    st.subheader("📊 Risk Assessment")
    st.write(f"**Model Used:** {model_choice.capitalize()}")
    st.write(f"**Risk Level:** {st.session_state['risk_label']}")
    st.write(f"**Risk Probability:** {st.session_state['risk_prob']:.2f}")

    st.divider()

    st.subheader("🤖 AI Explanation (Groq LLaMA 3.3)")
    st.write(st.session_state['risk_explanation'])







# FEATURE 2

from logic.debt_optimizer import optimize_debt
from llm.strategy_explainer import explain_strategy_with_llm

st.divider()
st.header("📉 2.Debt Repayment Strategy")


st.markdown(
"""
This feature demonstrates:
- Debt Repayment Strategy
- Responsible LLM explanations using Groq
"""
)


if st.button("Generate Debt Strategy"):
    if 'risk_label' not in st.session_state:
        st.error("Please run the Risk Analysis (Feature 1) first!")
    else:
        label = st.session_state['risk_label']
        strategy = optimize_debt(
            income=income,
            expenses=expenses,
            total_debt=debt,
            risk_label=label  # from Feature 1
        )
        st.session_state['strategy'] = strategy
        
        with st.spinner("Explaining strategy..."):
            explanation = explain_strategy_with_llm(
                strategy_output=strategy,
                income=income,
                expenses=expenses,
                debt=debt,
                risk_label=label
            )
        st.session_state['strategy_explanation'] = explanation

if 'strategy' in st.session_state:
    strategy = st.session_state['strategy']
    st.subheader("Recommended Strategy")
    st.write(f"**Strategy:** {strategy['strategy']}")
    st.write(f"**Monthly Target:** ₹{strategy['monthly_target']}")
    st.write(f"**Reason:** {strategy['reason']}")

    st.subheader("🤖 AI Explanation (Groq)")
    st.write(st.session_state['strategy_explanation'])




# FEATURE 3

from ml.behavior_model import classify_behavior
from llm.behavior_explainer import explain_behavior_with_llm

st.divider()
st.header("🧠 3. Financial Behavior Analysis")

st.markdown(
"""
This feature demonstrates:
- Financial Behavior Analysis
- Responsible LLM explanations using Groq
"""
)

impulse_score = st.slider(
    "Impulse Spending Tendency",
    0.0, 1.0, 0.5,
    help="Higher means more unplanned spending"
)

saving_score = st.slider(
    "Saving Discipline",
    0.0, 1.0, 0.5,
    help="Higher means consistent saving habits"
)

if st.button("Analyze Financial Behavior"):
    behavior = classify_behavior(impulse_score, saving_score)
    st.session_state['behavior'] = behavior

    with st.spinner("Analyzing behavior..."):
        explanation = explain_behavior_with_llm(
            behavior_label=behavior,
            impulse_score=impulse_score,
            saving_score=saving_score
        )
    st.session_state['behavior_explanation'] = explanation

if 'behavior' in st.session_state:
    st.subheader("Behavior Profile")
    st.write(f"**Detected Pattern:** {st.session_state['behavior']}")

    st.subheader("🤖 AI Explanation (Groq)")
    st.write(st.session_state['behavior_explanation'])




# FEATURE 4

from logic.nudge_engine import generate_nudge_context
from llm.nudge_explainer import explain_nudges_with_llm

st.divider()
st.header("🎯 4. Personalized Financial Nudges")

st.markdown(
"""
This feature demonstrates:
- Personalized Financial Nudges
- Responsible LLM explanations using Groq
"""
)

if st.button("Generate Personalized Nudges"):
    if 'risk_label' not in st.session_state:
        st.error("Please run the Risk Analysis (Feature 1) first!")
    elif 'behavior' not in st.session_state:
        st.error("Please run the Behavior Analysis (Feature 3) first!")
    elif 'strategy' not in st.session_state:
        st.error("Please run the Debt Strategy (Feature 2) first!")
    else:
        label = st.session_state['risk_label']
        behavior = st.session_state['behavior']
        strategy = st.session_state['strategy']

        nudge_points = generate_nudge_context(
            risk_label=label,
            behavior_label=behavior,
            strategy=strategy["strategy"]
        )

        user_profile = {
            "income": income,
            "expenses": expenses,
            "debt": debt,
            "risk_label": label,
            "behavior_label": behavior,
            "strategy": strategy["strategy"]
        }

        with st.spinner("Personalizing guidance..."):
            nudges = explain_nudges_with_llm(
                nudge_points=nudge_points,
                user_profile=user_profile
            )
        st.session_state['nudges'] = nudges

if 'nudges' in st.session_state:
    st.subheader("🤖 AI Nudges (Groq)")
    st.write(st.session_state['nudges'])

  