import pytest

from motd import app


@pytest.fixture()
def motd_app():
    app.testing = True
    return app


@pytest.fixture()
def client(motd_app):
    return app.test_client()


@pytest.fixture()
def quote():
    return 'single quote'


@pytest.fixture()
def double_quote():
    return "double quotes"
