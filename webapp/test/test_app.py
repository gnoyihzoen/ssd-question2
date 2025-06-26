import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_page(client):
    rv = client.get('/')
    assert b'Login' in rv.data

def test_invalid_password(client):
    rv = client.post('/', data={'password': '123'}, follow_redirects=True)
    assert b'Invalid password' in rv.data

def test_valid_password(client):
    rv = client.post('/', data={'password': 'StrongP@ssw0rd!'}, follow_redirects=True)
    assert b'Your password' in rv.data
