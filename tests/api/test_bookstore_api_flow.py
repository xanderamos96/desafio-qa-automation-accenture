import uuid
import requests
import pytest

BASE_URL = "https://demoqa.com"


def _gen_credentials():
    """
    Gera credenciais válidas segundo as regras do DemoQA:
    - Mínimo 8 caracteres
    - Letras maiúsculas e minúsculas
    - Números
    - Caractere especial
    """
    suffix = uuid.uuid4().hex[:8]
    username = f"user_{suffix}"
    password = f"Qa@{suffix}9!"
    return username, password


def _create_user(username: str, password: str) -> str:
    url = f"{BASE_URL}/Account/v1/User"
    payload = {"userName": username, "password": password}
    resp = requests.post(url, json=payload, timeout=30)
    assert resp.status_code == 201, f"Falha ao criar usuário: {resp.status_code} - {resp.text}"
    data = resp.json()
    assert data.get("username") == username, f"Username divergente: {data}"
    assert "userID" in data, f"userID ausente: {data}"
    return data["userID"]


def _generate_token(username: str, password: str) -> str:
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    payload = {"userName": username, "password": password}
    resp = requests.post(url, json=payload, timeout=30)
    assert resp.status_code == 200, f"Falha ao gerar token: {resp.status_code} - {resp.text}"
    data = resp.json()
    assert data.get("status") == "Success", f"Status inesperado: {data}"
    token = data.get("token")
    assert token, f"Token ausente na resposta: {data}"
    return token


def _is_authorized(username: str, password: str) -> bool:
    url = f"{BASE_URL}/Account/v1/Authorized"
    payload = {"userName": username, "password": password}
    resp = requests.post(url, json=payload, timeout=30)
    assert resp.status_code == 200, f"Falha ao verificar autorização: {resp.status_code} - {resp.text}"
    data = resp.json()
    assert isinstance(data, bool), f"Resposta não-booleana: {data}"
    return data


def _list_books() -> list[dict]:
    url = f"{BASE_URL}/BookStore/v1/Books"
    resp = requests.get(url, timeout=30)
    assert resp.status_code == 200, f"Falha ao listar livros: {resp.status_code} - {resp.text}"
    data = resp.json()
    books = data.get("books", [])
    assert isinstance(books, list) and len(books) >= 2, f"Lista de livros inválida ou insuficiente: {data}"
    for bk in books:
        assert "isbn" in bk and "title" in bk, f"Livro com campos ausentes: {bk}"
    return books


@pytest.mark.e2e
def test_bookstore_api_flow():
    #Criar usuário
    username, password = _gen_credentials()
    user_id = _create_user(username, password)

    #Gera token
    token = _generate_token(username, password)

    #Verifica autorização
    assert _is_authorized(username, password) is True, "Usuário não autorizado"

    #Lista livros
    books = _list_books()

    #Selecionar livros
    selected_isbns = [books[0]["isbn"], books[1]["isbn"]]

