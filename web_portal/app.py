from flask import Flask
from api.routes import api_blueprint   # import the blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/api")

app.config["BASE_URL"] = "http://localhost:5000/api"
