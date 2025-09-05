from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BooksPage:
    URL = "https://demoqa.com/books"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def add_book_by_title(self, title: str):
        # Espera o link do livro aparecer e clica
        book_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, title)))
        book_link.click()
