from os import environ


class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    GOOGLEMAPS_KEY = environ.get("GOOGLEMAPS_KEY")
    CORS_HEADERS = environ.get("CORS_HEADERS")
