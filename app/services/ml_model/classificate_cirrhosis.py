import joblib
import numpy as np
model = joblib.load('app\ml_model\model_cirrhosis.pkl')

def classificate_cirrhosis(data):
    cholesterol = data['cholesterol']
    albumin = data['albumin']
    copper = data['copper']
    alk_phos = data['alk_phos']
    tryglicerides = data['tryglicerides']
    platelets = data['platelets']
    prothrombin = data['prothrombin']
    test_data = np.array([[cholesterol, albumin, copper, alk_phos, tryglicerides, platelets, prothrombin]])

    classification = model.predict(test_data)[0]
    print(str(classification))

    return {"prediction" : str(classification)}