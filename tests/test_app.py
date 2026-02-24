import pytest
from app import app  # importa aplicação Flask

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello_docker(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello, Docker!"

def test_dados_recebidos(client):
    response = client.get("/test?num=123&text=ola")
    assert response.status_code == 200
    body = response.data.decode()
    assert "Recebido número: 123" in body
    assert 'texto: "ola"' in body

def test_erro_dados_faltando(client):
    response = client.get("/test")
    assert response.status_code == 400
    assert "Erro" in response.data.decode()

def test_cadastro(client):
    response = client.post("/cadastro", json={"nome": "Ju", "email": "ju@email.com"})
    assert response.status_code == 200
    body = response.data.decode()
    assert 'Nome "Ju"' in body
    assert 'Email "ju@email.com"' in body

def test_erro_cadastro(client):
    response = client.post("/cadastro", json={"nome": ""})
    assert response.status_code == 400
    assert "Erro" in response.data.decode()
