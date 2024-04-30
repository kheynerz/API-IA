from flask import Blueprint, request, jsonify

from app.services.agents.speech_to_text import speech_recognition
speech_to_text_routes = Blueprint('speech-to-text', __name__, url_prefix='/speech-to-text')

@speech_to_text_routes.route('/', methods=['POST'])
def speech_to_text():
    if 'Audio' not in request.files:
        return jsonify({"error": "Audio is required in Form Data"}), 400
    audio = request.files['Audio']
    
    response, code = speech_recognition(audio)
    return jsonify(response), code