from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


from base.base_page import BasePage
from config.urls import Urls



class DashboardPage(BasePage):
    PAGE_URL = Urls.DASHBOARD_URL

    MY_INFO_BUTTON = (By.XPATH, "//span[text()='My Info']")

    @allure.step('Click on "My Info" link')
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

