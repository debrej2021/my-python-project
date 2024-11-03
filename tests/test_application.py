import pytest
from application import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.data == b"Welcome to my Flask web app!"
