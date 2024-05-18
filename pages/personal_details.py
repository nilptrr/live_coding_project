from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import allure

from base.base_page import BasePage
from config.urls import Urls



class PersonalDetailsPage(BasePage):
    PAGE_URL = Urls.PERSONAL_DETAILS_URL
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[name='firstName']")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    SPINNER_LOADER = (By.CSS_SELECTOR, '.oxd-loading-spinner')

    def change_name(self, new_name):
        with allure.step(f'Change name on "{new_name}"'):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            # first_name_field.clear()
            first_name_field.send_keys(Keys.CONTROL +'A')
            first_name_field.send_keys(Keys.DELETE)
            # assert first_name_field.get_attribute('value') == '', 'There is text'
            first_name_field.send_keys(new_name)
            self.new_name = new_name
    
    @allure.step('Save changes')
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes has been saved successfully')
    def is_changes_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.SPINNER_LOADER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.new_name))
