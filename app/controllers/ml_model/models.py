from flask import Blueprint, request, jsonify
from app.services.agents.feeling import recognize_feeling_from_image
from app.services.ml_model.predict_bitcoin import predict_bitcoin
model_routes = Blueprint('model', __name__, url_prefix='/model')

@model_routes.route('/bitcoin', methods=['POST'])
def bitcoin_prediction():
    data = request.json
    if not data or 'volume' not in data:
        return jsonify({'error': '"volume" is required in body'}), 400
    
    if 'market_cap' not in data:
        return jsonify({'error': '"market_cap" is required in body'}), 400
    
    prediction = predict_bitcoin(data["volume"], data["market_cap"])
    return jsonify(prediction)