from locators.page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utilites.logger import Logger


import time


class StoreBusinessRequirementsPage(BasePage):
    locators = Locators()

    def search_product(self):
        Logger.add_start_step(method='search_product')
        self.element_is_visible(self.locators.INPUT_BOX).send_keys('тостер')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.CATEGORIES_BUTTON).click()
        self.action_move_to_element(self.element_is_visible(self.locators.CATEGORIES_LIST))
        self.element_is_visible(self.locators.CATEGORIES_LIST).click()
        Logger.add_end_step(url=self.driver.current_url, method='search_product')

    def filters_product(self):
        Logger.add_start_step(method='filters_product')
        self.element_is_visible(self.locators.QUANTITY_PRODUCTS).click()
        self.element_is_visible(self.locators.BRENDS_BUTTON).click()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.element_is_visible(self.locators.BREND_BUTTON).click()
        self.element_is_visible(self.locators.AVAILABILITY_CHECKBOX).click()
        self.element_is_visible(self.locators.PICK_BY_PRICE).click()
        # передвинуть ползунок цены в право
        self.action_move_to_element(self.element_is_visible(self.locators.CURRENT_PRICES))
        self.action_drag_and_drop_to_element(self.element_is_visible(self.locators.CURRENT_PRICES), self.element_is_visible(self.locators.CURRENT_PRICES))
        self.element_is_visible(self.locators.CONTACT).click()
        Logger.add_end_step(url=self.driver.current_url, method='filters_product')

    def design_product(self):
        Logger.add_start_step(method='design_product')
        self.element_is_visible(self.locators.DESIGN_PRODUCT).click()
        self.element_is_visible(self.locators.PLACE_ON_ORDER).click()
        self.element_is_visible(self.locators.CONTINUE_WITHOUT_REGISTERING).click()
        self.driver.execute_script("window.scrollTo(0, 10000)")
        self.element_is_visible(self.locators.ORDER).click()




        Logger.add_end_step(url=self.driver.current_url, method='design_product')










