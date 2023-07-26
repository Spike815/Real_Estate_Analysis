import joblib
def predict_new_data(X):
    loaded_model = joblib.load("models\XGBmodel.joblib")
    y_pred = loaded_model.predict(X)
    return {
        "prediction":y_pred,
        "status_code":200
    }
