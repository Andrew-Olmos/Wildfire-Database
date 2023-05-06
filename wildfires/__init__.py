from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wildfires.config import Config
from flask_googlemaps import GoogleMaps
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_login import login_user, LoginManager

csrf = CSRFProtect()
cors = CORS()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wildfires.db'
    app.config['SECRET_KEY'] = 'secret_key_here'
    # app.config['DEVELOPMENT'] = True
    csrf.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    GoogleMaps(app)

    #db = SQLAlchemy(app)

    #login_manager = LoginManager()
    #login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    with app.app_context():
        db.create_all()
        #db.init_app(app)

    from wildfires.errors.handlers import errors
    from wildfires.main.routes import main

    app.register_blueprint(errors)
    app.register_blueprint(main)

    return app