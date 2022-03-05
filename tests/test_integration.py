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
    assert b"Toxicity Monitor" in response.data
    assert b"Write a sentence below and click on the \"Submit\" button to display the result !"


