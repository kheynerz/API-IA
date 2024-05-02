import joblib
import numpy as np
model = joblib.load('app\ml_model\model_telefonia.pkl')

def classificate_phone_company_churn(data, required_values):
    data_to_predict = np.array([[1] + [data[key] for key in required_values]])
    classification = model.predict(data_to_predict)[0]

    return {"prediction" : str(classification)}