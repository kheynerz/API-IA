import joblib
import numpy as np
model = joblib.load('app\ml_model\model_bitcoin.pkl')

def predict_bitcoin(volume, market_cap):
    prediction = model.predict([[1, volume, market_cap]])
    print(prediction[0], type(prediction[0]))
    return {"prediction" : prediction[0]}