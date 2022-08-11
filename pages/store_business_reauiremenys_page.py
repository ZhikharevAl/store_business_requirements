from locators.page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import time


class StoreBusinessRequirementsPage(BasePage):
    locators = Locators()

    def search_input(self):
        self.element_is_visible(self.locators.INPUT_BOX).send_keys('тостер')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()






