from flask import Blueprint, request, jsonify
from app.services.ml_model.classificate_cirrhosis import classificate_cirrhosis
from app.services.ml_model.classificate_wine_quality import classificate_wine_quality
from app.services.ml_model.predict_bitcoin import predict_bitcoin
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
    classification = classificate_cirrhosis(data)
    return jsonify(classification)


@model_routes.route('/wine', methods=['POST'])
def wine_quality_classification():
    data = request.json
    required_values = ['fixed_acidity','volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density','pH','sulphates','alcohol']
    errors = validate_body(data, required_values)
    if errors: return jsonify(errors)

    classification = classificate_wine_quality(data)
    return jsonify(classification)