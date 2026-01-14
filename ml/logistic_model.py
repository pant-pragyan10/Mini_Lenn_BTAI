import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from ml.data_generator import generate_data

# Train model
df = generate_data()

X = df.drop(columns=["risk"])
y = df["risk"]

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X, y)

def predict_logistic(user_input: dict):
    X_user = np.array([[
        user_input["income"],
        user_input["expenses"],
        user_input["debt"],
        user_input["credit_util"],
        user_input["expense_ratio"],
        user_input["debt_to_income"]
    ]])

    prob = pipeline.predict_proba(X_user)[0][1]

    if prob > 0.6:
        label = "High Risk"
    elif prob > 0.3:
        label = "Medium Risk"
    else:
        label = "Low Risk"

    return label, prob
