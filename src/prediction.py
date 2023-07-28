import joblib
def predict_new_data(X):

    loaded_model = joblib.load("models\XGB.joblib")
    y_pred = loaded_model.predict(X)
    return y_pred[0]
