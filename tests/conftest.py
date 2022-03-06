import pytest
import website.toxic_app as ta
from website.toxic_app import createapp

@pytest.fixture
def client():
    app = ta.createapp()
    with app.test_client() as client:
        yield client
