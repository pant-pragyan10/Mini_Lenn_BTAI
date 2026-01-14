<img width="909" height="716" alt="image" src="https://github.com/user-attachments/assets/445633a8-cc97-48b5-ac37-36d47b63d001" />
<img width="790" height="824" alt="image" src="https://github.com/user-attachments/assets/f9758ab0-49bf-4c77-b612-17857d6c3cff" />
<img width="790" height="824" alt="image" src="https://github.com/user-attachments/assets/5ebd905a-c0a5-47ec-bee7-96ba5695ad62" />
<img width="445" height="728" alt="image" src="https://github.com/user-attachments/assets/3df388f0-6bc6-41b8-9047-42bfbc563b21" />
<img width="502" height="409" alt="image" src="https://github.com/user-attachments/assets/4b5cfbe4-26b9-4885-9a7c-476396612b52" />











# 💰 Mini Lenn BTai — AI-Powered Debt Intelligence System

A **fintech-focused AI prototype** inspired by Lenn BTai, designed to demonstrate how machine learning, rule-based systems, behavioral analytics, and LLMs can be combined responsibly to support **debt risk assessment, repayment planning, and personalized financial guidance**.

This project is intentionally **minimal, explainable, and interview-ready**, focusing on *engineering judgment* rather than raw complexity.

---

## 🚀 What This Project Demonstrates

This system showcases end-to-end thinking required in modern fintech AI systems:

* ✅ Predictive analytics using classical ML
* ✅ Accuracy vs explainability trade-offs
* ✅ Deterministic financial decision logic
* ✅ Behavioral pattern discovery (unsupervised learning)
* ✅ Safe & controlled LLM usage for explanations
* ✅ Product-oriented system design

---

## 🧠 System Architecture (Conceptual)

```
User Input
   ↓
Debt Risk Prediction (Logistic / XGBoost)
   ↓
Debt Repayment Strategy (Rule-based)
   ↓
Behavioral Pattern Detection (Clustering)
   ↓
Personalized Financial Nudges (LLM-assisted)
```

Each layer has **one clear responsibility**, ensuring:

* Safety
* Explainability
* Auditability
* User trust

---

## 🧩 Core Features

### 1️⃣ Debt Risk Prediction (ML)

**Goal:** Estimate the likelihood that a user may struggle with debt repayment.

* Models used:

  * Logistic Regression (interpretable baseline)
  * XGBoost (non-linear, high-performance)
* Input features:

  * Income, expenses, total debt
  * Credit utilization
  * Derived ratios (expense ratio, debt-to-income)
* Output:

  * Risk probability
  * Risk category (Low / Medium / High)

**Why two models?**

* Logistic Regression → transparency & regulatory trust
* XGBoost → better performance on complex patterns

---

### 2️⃣ Debt Optimization & Repayment Strategy (Rules)

**Goal:** Convert risk insights into safe, actionable steps.

* Purely rule-based (no ML)
* Computes:

  * Monthly surplus
  * Conservative vs aggressive repayment targets
* Strategies:

  * Stabilization (reduce expenses first)
  * Snowball (behavior-friendly)
  * Avalanche (cost-efficient)

**Design principle:**

> Financial actions should be deterministic and auditable.

---

### 3️⃣ Behavioral Pattern Detection (Clustering)

**Goal:** Understand *how* a user behaves financially, not just their risk level.

* Unsupervised learning (KMeans)
* Behavioral proxies:

  * Impulse spending tendency
  * Saving discipline
* Output:

  * Impulsive Spender
  * Disciplined Saver

**Why clustering?**

* Behavior labels are rarely available
* Patterns emerge naturally from data

---

### 4️⃣ Personalized Financial Nudges (Product Layer)

**Goal:** Deliver small, context-aware suggestions users are likely to follow.

* Combines:

  * Risk level
  * Behavior pattern
  * Debt strategy
* Rule engine decides *what* to say
* LLM decides *how* to say it

**Important:**

> The LLM never makes financial decisions — it only explains them.

---

## 🤖 LLM Integration (Groq)

* Model: **LLaMA-3.3-70B-Versatile (Groq)**
* Used only for:

  * Explaining risk predictions
  * Explaining debt strategies
  * Generating friendly nudges

**Safety-first approach:**

* No hallucinated advice
* No guarantees
* No legal or financial commitments

---

## 🖥️ User Interface

* Built using **Streamlit**
* Allows:

  * Model comparison (Logistic vs XGBoost)
  * Live risk analysis
  * Strategy generation
  * Behavioral insights
  * Personalized nudges

Designed for **demo clarity**, not UI polish.

---

## 🧱 Project Structure

```
mini_lenn_btai/
│
├── app.py                     # Streamlit UI
├── requirements.txt
│
├── ml/
│   ├── data_generator.py      # Synthetic fintech data
│   ├── logistic_model.py      # Interpretable ML
│   ├── xgboost_model.py       # High-performance ML
│   ├── behavior_model.py      # Clustering
│   └── predictor.py           # Unified model interface
│
├── logic/
│   ├── debt_optimizer.py      # Rule-based strategy
│   └── nudge_engine.py        # Nudge policy logic
│
├── llm/
│   ├── explainer.py           # Risk explanation
│   ├── strategy_explainer.py  # Strategy explanation
│   ├── behavior_explainer.py  # Behavior explanation
│   └── nudge_explainer.py     # Personalized nudges
```

---

## ⚙️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set environment variable:

```bash
export GROQ_API_KEY=your_api_key_here
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 📌 Key Engineering Takeaways

* ML is used **only where prediction is required**
* Financial decisions are **rule-based and auditable**
* Behavioral insights improve personalization
* LLMs are used responsibly for communication, not control
* System design prioritizes trust over blind optimization

---

## 🔮 Future Improvements (Out of Scope)

* Transaction-level time series analysis
* SHAP-based explainability for XGBoost
* Loan-level interest optimization
* Model monitoring & drift detection
* Secure deployment (auth, encryption, logging)

---

## 🎯 Why This Project

This prototype was built to:

* Understand real-world fintech AI challenges
* Practice responsible AI system design
* Demonstrate end-to-end product thinking

> **Prediction is only the beginning. Trust and action are the real goals.**

---

**Author:** Pragyan Pant
**Focus:** AI/ML Systems • Fintech • Responsible LLMs
