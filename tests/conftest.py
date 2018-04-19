import pytest

from motd import app


@pytest.fixture()
def client():
    app.testing = True
    return app.test_client()


@pytest.fixture()
def quote():
    return 'single quote'


@pytest.fixture()
def double_quote():
    return "double quotes"
