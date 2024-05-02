import joblib
import numpy as np
model = joblib.load('app\ml_model\model_body_fat.pkl')

def predict_bmi(data, required_values):
    data_to_predict = np.array([[data[key] for key in required_values]])
    prediction = model.predict(data_to_predict)[0][0]
    return {"prediction" : str(prediction)}