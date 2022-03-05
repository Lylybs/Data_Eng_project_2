import pytest
from website.toxic_app import createapp

@pytest.fixture
def client():
    app = createapp()
    with app.test_client() as client:
        yield client
