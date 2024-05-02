import joblib
import numpy as np
model = joblib.load('app\ml_model\model_avocado.pkl')

def predict_avocado_price(data, required_values):
    data_to_predict = np.array([[1123]+[data[key] for key in required_values]])
    prediction = model.predict(data_to_predict)[0][0]
    return {"prediction" : str(prediction)}