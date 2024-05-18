from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base_page import BasePage
from config.urls import Urls



class LoginPage(BasePage):
    PAGE_URL = Urls.LOGIN_URL

    USERNAME_FIELD = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")


    @allure.step('Enter login')
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Click "Submit" button')
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
