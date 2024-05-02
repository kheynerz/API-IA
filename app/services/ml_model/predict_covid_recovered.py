import joblib
import numpy as np
model = joblib.load('app\ml_model\model_covid.pkl')

def predict_covid_recovered(data):
    data_to_predict = np.array([list(data.values())])
    prediction = model.predict(data_to_predict)[0]
    return {"prediction" : str(prediction)}