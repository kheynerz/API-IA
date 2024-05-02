import joblib
import numpy as np
model = joblib.load('app\ml_model\model_car_price.pkl')

def predict_car_price(data, required_values):
    data_to_predict = np.array([[data[key] for key in required_values]])
    prediction = model.predict(data_to_predict)[0][0]
    return {"prediction" : str(prediction)}