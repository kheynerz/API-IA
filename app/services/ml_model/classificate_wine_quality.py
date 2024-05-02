import joblib
import numpy as np
model = joblib.load('app\ml_model\model_wine.pkl')

def classificate_wine_quality(data):
    fixed_acidity = data['fixed_acidity']
    volatile_acidity = data['volatile_acidity']
    citric_acid = data['citric_acid']
    residual_sugar = data['residual_sugar']
    chlorides = data['chlorides']
    free_sulfur_dioxide = data['free_sulfur_dioxide']
    total_sulfur_dioxide = data['total_sulfur_dioxide']
    density = data['density']
    pH = data['pH']
    sulphates = data['sulphates']
    alcohol = data['alcohol']
    test_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])

    classification = model.predict(test_data)[0]

    return {"prediction" : str(classification)}