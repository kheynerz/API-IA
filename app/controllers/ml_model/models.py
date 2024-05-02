from flask import Blueprint, request, jsonify
from app.services.ml_model.classificate_cirrhosis import classificate_cirrhosis
from app.services.ml_model.classificate_hepatitis import classificate_hepatitis
from app.services.ml_model.classificate_phone_company import classificate_phone_company_churn
from app.services.ml_model.classificate_stroke import classificate_stroke
from app.services.ml_model.classificate_wine_quality import classificate_wine_quality
from app.services.ml_model.predict_avocado_price import predict_avocado_price
from app.services.ml_model.predict_bitcoin import predict_bitcoin
from app.services.ml_model.predict_bmi import predict_bmi
from app.services.ml_model.predict_car_price import predict_car_price
from app.services.ml_model.predict_covid_recovered import predict_covid_recovered
from app.utils.validate_body import validate_body

model_routes = Blueprint('model', __name__, url_prefix='/model')

@model_routes.route('/bitcoin', methods=['POST'])
def bitcoin_prediction():
    data = request.json
    errors = validate_body(data, ['volume', 'market_cap'])
    if errors: return jsonify(errors)

    prediction = predict_bitcoin(data["volume"], data["market_cap"])
    return jsonify(prediction)

@model_routes.route('/cirrhosis', methods=['POST'])
def cirrhosis_classification():
    data = request.json
    required_values = ['cholesterol', 'albumin', 'copper', 'alk_phos', 'tryglicerides', 'platelets', 'prothrombin']
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)
    classification = classificate_cirrhosis(data, required_values)
    return jsonify(classification)


@model_routes.route('/wine', methods=['POST'])
def wine_quality_classification():
    data = request.json
    required_values = ['fixed_acidity','volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density','pH','sulphates','alcohol']
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    classification = classificate_wine_quality(data, required_values)
    return jsonify(classification)


@model_routes.route('/stroke', methods=['POST'])
def stroke_classification():
    data = request.json
    required_values = [
        "age",
        "hypertension",
        "heart_disease",
        "avg_glucose_level",
        "bmi",
        "gender_Male",
        "gender_Other",
        "ever_married_Yes",
        "work_type_Never_worked",
        "work_type_Private",
        "work_type_Self-employed",
        "work_type_children",
        "Residence_type_Urban",
        "smoking_status_formerly_smoked",
        "smoking_status_never_smoked",
        "smoking_status_smokes"
    ]
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    classification = classificate_stroke(data, required_values)
    return jsonify(classification)

@model_routes.route('/phone_company_churn', methods=['POST'])
def phone_company_churn_classification():
    data = request.json
    required_values = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
]
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    classification = classificate_phone_company_churn(data, required_values)
    return jsonify(classification)

@model_routes.route('/covid', methods=['POST'])
def covid_classification():
    data = request.json
    required_values = ["SNo", "ObservationDate", "Province/State", "Country/Region", "Last Update", "Confirmed", "Deaths"]
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    prediction = predict_covid_recovered(data, required_values)
    return jsonify(prediction)


@model_routes.route('/bmi', methods=['POST'])
def bmi_prediction():
    data = request.json
    required_values = ["density", "age", "weight", "height", "neck", "chest", "abdomen", "hip", "thigh", "knee", "ankle", "biceps", "forearm", "wrist"]

    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    prediction = predict_bmi(data, required_values)
    return jsonify(prediction)



@model_routes.route('/car_price', methods=['POST'])
def car_price_prediction():
    data = request.json
    required_values = ["year", "selling_price", "kms_driven", "fuel_type", "seller_type", "transmission", "owner"]

    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    prediction = predict_car_price(data, required_values)
    return jsonify(prediction)


@model_routes.route('/avocado_price', methods=['POST'])
def avocado_price_prediction():
    data = request.json
    required_values = [
        "total_volume",
        "4046",
        "4225",
        "4770",
        "total_bags",
        "small_bags",
        "large_bags",
        "xlarge_bags",
        "type",
        "year",
        "month",
        "spring",
        "summer",
        "fall"
    ]
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    prediction = predict_avocado_price(data, required_values)
    return jsonify(prediction)



@model_routes.route('/hepatitis', methods=['POST'])
def hepatitis_classification():
    data = request.json
    required_values = ["AST", "BIL", "GGT"]

    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    classification = classificate_hepatitis(data, required_values)
    return jsonify(classification)