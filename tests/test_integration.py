from aiohttp import request
import pytest
from website.toxic_app import createapp
from tests.conftest import client

#code 200
def test_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

#text
def test_html(client):
    response = client.get('/')
    assert b"Toxicity Application" in response.data
    assert b"Quick and simple website to help you detect toxicity." in response.data
    assert b"Our application tells you if the piece of text you submitted contains toxicity or not." in response.data