import pytest

from motd import app


@pytest.fixture()
def client():
    app.testing = True
    return app.test_client()
