import pytest
import Website.toxic_app as ta

@pytest.fixture
def client():
    app = ta.final_function()
    with app.test_client() as client:
        yield client
