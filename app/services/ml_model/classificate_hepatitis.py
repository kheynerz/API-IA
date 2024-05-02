import joblib
import numpy as np
model = joblib.load('app\ml_model\model_hepatitis.pkl')

def classificate_hepatitis(data, required_values):
    data_to_predict = np.array([[data[key] for key in required_values]])
    classification = model.predict(data_to_predict)[0]

    return {"prediction" : str(classification)}