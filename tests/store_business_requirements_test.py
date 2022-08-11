import time
from pages.store_business_reauiremenys_page import StoreBusinessRequirementsPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestStore:
    class TestSearchBox:
        def test_search_input(self, driver):
            test_search_input = StoreBusinessRequirementsPage(driver, 'https://www.onlinetrade.ru/')
            test_search_input.open()
            test_search_input.search_input()
            time.sleep(5)





