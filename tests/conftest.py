import pytest

from app import create_app
from db import db


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app


@pytest.fixture
def database(app):
    db.init_app(app)
    db.drop_all()
    db.create_all()
    db.session.commit()

    yield db

    db.session.close()


@pytest.fixture
def client(app, database):
    with app.test_client() as client:
        yield client
