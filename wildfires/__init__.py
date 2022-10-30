from flask import Flask
from wildfires.config import Config
from flask_googlemaps import GoogleMaps
from flask_cors import CORS, cross_origin


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors = CORS(app)
    GoogleMaps(app)

    from wildfires.products.routes import products
    from wildfires.main.routes import main
    from wildfires.errors.handlers import errors

    app.register_blueprint(products)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
