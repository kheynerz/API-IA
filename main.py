from flask import Flask
from app.controllers.routes import api_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register main blueprint
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)