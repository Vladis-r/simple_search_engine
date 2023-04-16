import pytest

from app import create_app
from db import db as database


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    db.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client
