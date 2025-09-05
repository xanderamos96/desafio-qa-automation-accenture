import pytest
from utils.selenium_driver import get_driver
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.books_page import BooksPage
from tests.api.test_bookstore_api_flow import _gen_credentials, _create_user, _generate_token, _list_books

@pytest.mark.ui
def test_ui_flow():
    username, password = _gen_credentials()
    user_id = _create_user(username, password)
    token = _generate_token(username, password)

    driver = get_driver(headless=False)
    
    #Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    logged_user = login_page.get_logged_user()
    assert logged_user == username, f"Usuário logado esperado {username}, mas foi {logged_user}"

    books = _list_books()
    #Lista de livros
    books_page = BooksPage(driver)
    books_page.open()
    books_page.add_book_by_title(books[0]["title"])

    driver.quit()
