from dotenv import load_dotenv
load_dotenv()
from os import environ


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")
    GOOGLEMAPS_KEY = environ.get("GOOGLEMAPS_KEY")
    CORS_HEADERS = environ.get("CORS_HEADERS")
