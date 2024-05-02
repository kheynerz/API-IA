import joblib
import numpy as np
model = joblib.load('app\ml_model\model_Ictus.pkl')

def classificate_stroke(data):
    data["id"] = 1
    data_to_predict = np.array([list(data.values())])
    classification = model.predict(data_to_predict)[0]
    
    return {"prediction" : str(classification)}