from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://demoqa.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login").click()

    def get_logged_user(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "userName-value"))).text
