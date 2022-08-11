import time
from pages.store_business_reauiremenys_page import StoreBusinessRequirementsPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestStore:
    class TestSearchProduct:
        def test_search_product(self, driver):
            test_search_product = StoreBusinessRequirementsPage(driver, 'https://www.onlinetrade.ru/')
            test_search_product.open()
            test_search_product.search_product()
            time.sleep(5)

    class TestFiltersProduct:
        def test_filters_product(self, driver):
            test_filters_product = StoreBusinessRequirementsPage(driver, 'https://www.onlinetrade.ru/catalogue/tostery-c80/')
            test_filters_product.open()
            test_filters_product.filters_product()
            time.sleep(5)

