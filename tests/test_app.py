import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_root(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.data.decode() == 'Hello, Docker!'


def test_test_endpoint_success(client):
    resp = client.get('/test', query_string={'num': 42, 'text': 'olá'})
    assert resp.status_code == 200
    body = resp.data.decode()
    assert 'Recebido número: 42' in body
    assert 'texto: "olá"' in body or 'texto: "olá"' in body


def test_test_endpoint_missing_params(client):
    resp = client.get('/test')
    assert resp.status_code == 400


def test_cadastro_success(client):
    resp = client.post('/cadastro', json={'nome': 'João', 'email': 'joao@example.com'})
    assert resp.status_code == 200
    assert 'Nome "João"' in resp.data.decode()


def test_cadastro_missing_fields(client):
    resp = client.post('/cadastro', json={'nome': ''})
    assert resp.status_code == 400
