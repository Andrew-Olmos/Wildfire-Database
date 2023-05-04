from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wildfires.config import Config
from flask_googlemaps import GoogleMaps
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wildfires.db'
    app.config['SECRET_KEY'] = 'secret_key_here'
    csrf = CSRFProtect(app)

    cors = CORS(app)
    GoogleMaps(app)

    with app.app_context():
        db.init_app(app)

    from wildfires.errors.handlers import errors
    from wildfires.main.routes import main

    app.register_blueprint(errors)
    app.register_blueprint(main)

    return app
