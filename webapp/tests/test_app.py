import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_page(client):
    rv = client.get('/')
    assert b'Login' in rv.data

test_password_invalid = "123"
def test_invalid_password(client):
    rv = client.post('/', data={'password': test_password_invalid}, follow_redirects=True)
    assert b'Invalid password' in rv.data

test_password_valid = "StrongP@ssw0rd!"
def test_valid_password(client):
    rv = client.post('/', data={'password': test_password_valid}, follow_redirects=True)
    assert b'Your password' in rv.data
