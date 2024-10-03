from core.ui.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "Username")
    PASSWORD_FIELD = (By.ID, "passwordLogin")
    LOGIN_BUTTON = (By.ID, "buttonLogin") 
    
    def enter_username(self, username):
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

