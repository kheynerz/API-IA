from flask import Blueprint, request, jsonify

# Blueprints
from app.controllers.agents.feeling import feeling_routes
from app.controllers.agents.speech_to_text import speech_to_text_routes

api_routes = Blueprint('api', __name__, url_prefix='/api')

api_routes.register_blueprint(feeling_routes)
api_routes.register_blueprint(speech_to_text_routes)