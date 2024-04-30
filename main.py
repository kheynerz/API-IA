from flask import Flask
from app.controllers.routes import api_routes

app = Flask(__name__)

# Register main blueprint
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)