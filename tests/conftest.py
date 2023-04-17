import pytest

from app import create_app
from config import TestConfig
from db import db as database


@pytest.fixture()
def app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app


@pytest.fixture()
def db(app):
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture()
def client(app, db):
    with app.test_client() as client:
        yield client
