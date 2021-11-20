from flask import Flask
from flask_cors import CORS
import config


def create_app():
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object(config.ProdConfig)
    else:
        app.config.from_object(config.DevConfig)
    CORS(app)

    return app
