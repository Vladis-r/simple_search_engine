import os

from flask.cli import load_dotenv

load_dotenv()


class BaseConfig(object):
    FLASK_ENV = "production"
    SECRET_KEY = os.getenv('SECRET_KEY') or 'A SECRET KEY'

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "sqlite.db")

    JSON_AS_ASCII = False
