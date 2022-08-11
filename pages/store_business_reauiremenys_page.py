from locators.page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


import time


class StoreBusinessRequirementsPage(BasePage):
    locators = Locators()

    def search_product(self):
        self.element_is_visible(self.locators.INPUT_BOX).send_keys('тостер')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.CATEGORIES_BUTTON).click()
        self.action_move_to_element(self.element_is_visible(self.locators.CATEGORIES_LIST))
        self.element_is_visible(self.locators.CATEGORIES_LIST).click()

    def filters_product(self):
        self.element_is_visible(self.locators.QUANTITY_PRODUCTS).click()
        self.element_is_visible(self.locators.BRENDS_BUTTON).click()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.element_is_visible(self.locators.BREND_BUTTON).click()










