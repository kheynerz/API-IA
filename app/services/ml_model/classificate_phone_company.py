import joblib
import numpy as np
model = joblib.load('app\ml_model\model_telefonia.pkl')

def classificate_phone_company_churn(data):
    data["customerID"] = 1
    data_to_predict = np.array([list(data.values())])
    classification = model.predict(data_to_predict)[0]

    return {"prediction" : str(classification)}