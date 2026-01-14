import numpy as np
import xgboost as xgb
from ml.data_generator import generate_data

# Train model
df = generate_data()

X = df.drop(columns=["risk"])
y = df["risk"]

model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss"
)

model.fit(X, y)

def predict_xgboost(user_input: dict):
    X_user = np.array([[
        user_input["income"],
        user_input["expenses"],
        user_input["debt"],
        user_input["credit_util"],
        user_input["expense_ratio"],
        user_input["debt_to_income"]
    ]])

    prob = model.predict_proba(X_user)[0][1]

    if prob > 0.6:
        label = "High Risk"
    elif prob > 0.3:
        label = "Medium Risk"
    else:
        label = "Low Risk"

    return label, prob





