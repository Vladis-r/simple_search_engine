from config import TestConfig


def test_pytest():
    assert True


def test_client(app):
    assert app.test_client(TestConfig)
