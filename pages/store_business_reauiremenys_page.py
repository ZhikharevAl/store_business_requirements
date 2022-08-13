from locators.page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utilites.logger import Logger
from generator.generator import generated_person
import random
import time
from selenium.common.exceptions import TimeoutException


class StoreBusinessRequirementsPage(BasePage):
    locators = Locators()

    """ Поиск продукта"""

    def search_product(self):
        Logger.add_start_step(method='search_product')
        self.element_is_visible(self.locators.INPUT_BOX).send_keys('тостер')
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()
        self.element_is_visible(self.locators.CATEGORIES_BUTTON).click()
        self.action_move_to_element(self.element_is_visible(self.locators.CATEGORIES_LIST))
        self.element_is_visible(self.locators.CATEGORIES_LIST).click()
        Logger.add_end_step(url=self.driver.current_url, method='search_product')

        """ Применение фильтров к продукту"""

    def filters_product(self):
        Logger.add_start_step(method='filters_product')
        self.element_is_visible(self.locators.QUANTITY_PRODUCTS).click()
        self.element_is_visible(self.locators.BRENDS_BUTTON).click()
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.element_is_visible(self.locators.BREND_BUTTON).click()
        self.element_is_visible(self.locators.AVAILABILITY_CHECKBOX).click()
        self.element_is_visible(self.locators.PICK_BY_PRICE).click()
        self.action_move_to_element(self.element_is_visible(self.locators.CURRENT_PRICES))
        self.action_drag_and_drop_to_element(self.element_is_visible(self.locators.CURRENT_PRICES),
                                             self.element_is_visible(self.locators.CURRENT_PRICES))
        self.element_is_visible(self.locators.CONTACT).click()
        Logger.add_end_step(url=self.driver.current_url, method='filters_product')

        """ Оформление заказа"""

    def design_product(self):
        Logger.add_start_step(method='design_product')
        self.element_is_visible(self.locators.DESIGN_PRODUCT).click()
        self.element_is_visible(self.locators.PLACE_ON_ORDER).click()
        self.element_is_visible(self.locators.CONTINUE_WITHOUT_REGISTERING).click()
        self.driver.execute_script("window.scrollTo(0, 10000)")
        self.element_is_visible(self.locators.ORDER).click()

        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        mobile_phone = person_info.mobile

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERSON).send_keys(full_name)
        self.element_is_visible(self.locators.PHONE).send_keys(mobile_phone)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        # нажать клавишу enter
        # self.element_is_visible(self.locators.EMAIL).send_keys(Keys.ENTER)
        self.driver.execute_script("window.history.go(-3)")
        #self.driver.back()
        time.sleep(2)
        self.quit()
        Logger.add_end_step(url=self.driver.current_url, method='design_product')
