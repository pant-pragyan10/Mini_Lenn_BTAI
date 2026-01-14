import numpy as np
import pandas as pd

def generate_data(n=500):
    np.random.seed(42)

    income = np.random.randint(20000, 150000, n)
    expenses = income * np.random.uniform(0.3, 1.1, n)
    debt = income * np.random.uniform(0.5, 6.0, n)
    credit_util = np.random.uniform(0.1, 0.9, n)

    expense_ratio = expenses / income
    debt_to_income = debt / (income * 12)

    # Risk logic (simulated ground truth)
    risk = (
        (expense_ratio > 0.8).astype(int) +
        (debt_to_income > 0.4).astype(int) +
        (credit_util > 0.6).astype(int)
    )

    risk = (risk >= 2).astype(int)  # 1 = High risk

    df = pd.DataFrame({
        "income": income,
        "expenses": expenses,
        "debt": debt,
        "credit_util": credit_util,
        "expense_ratio": expense_ratio,
        "debt_to_income": debt_to_income,
        "risk": risk
    })

    return df
