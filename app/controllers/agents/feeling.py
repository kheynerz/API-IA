from flask import Blueprint, request, jsonify
from app.services.agents.feeling import recognize_feeling_from_image
feeling_routes = Blueprint('feeling', __name__, url_prefix='/feeling')

@feeling_routes.route('/', methods=['POST'])
def feeling_recognition():
    if 'Image' not in request.files:
        return jsonify({"error": "Image is required in Form Data"}), 400
    image = request.files['Image']
    
    print("Image received")
    face_analysis = recognize_feeling_from_image(image)
    return jsonify(face_analysis)