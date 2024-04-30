from flask import Blueprint, request, jsonify

ml_models_routes = Blueprint('algorithms', __name__, url_prefix='/ml_model')

@ml_models_routes.route('/', methods=['GET'])
def reconocimiento_sentimientos():
    resultado = {"ml_model": "ml_model"}
    return jsonify(resultado)