from ml.logistic_model import predict_logistic
from ml.xgboost_model import predict_xgboost

def predict_risk(user_input, model_type="logistic"):
    if model_type == "logistic":
        return predict_logistic(user_input)
    elif model_type == "xgboost":
        return predict_xgboost(user_input)
    else:
        raise ValueError("Invalid model type")
