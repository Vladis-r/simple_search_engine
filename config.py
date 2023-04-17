import os

from flask.cli import load_dotenv

load_dotenv()


class BaseConfig(object):
    FLASK_ENV = "production"
    SECRET_KEY = os.getenv('SECRET_KEY') or 'A SECRET KEY'

    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestConfig(BaseConfig):
    FLASK_ENV = "testing"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = "development"
    SQLALCHEMY_ECHO = True

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "sqlite.db")
