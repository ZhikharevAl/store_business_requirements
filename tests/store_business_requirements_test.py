import time
from pages.store_business_reauiremenys_page import StoreBusinessRequirementsPage
from pages.base_page import BasePage

link1 = 'https://www.onlinetrade.ru/catalogue/tostery-c80/'
link2 = "https://www.onlinetrade.ru/catalogue/tostery-c80/?selling[]=1&producer[]=TEFAL&price1=2490&price2=4190&advanced_search=1&rating_active=0&special_active=1&selling_active=1&producer_active=1&price_active=1&type_upravleniya_active=1&power_active=1&kol_otdelin_active=1&cat_id=80"

""" Дымовое тестирование магазина """


class TestStore:
    """ Проверка поиска продукта магазина """
    class TestSearchProduct:

        def test_search_product(self, driver):
            test_search_product = StoreBusinessRequirementsPage(driver, 'https://www.onlinetrade.ru/')
            test_search_product.open()
            test_search_product.search_product()
            url_now = driver.current_url
            print(url_now)
            assert url_now == link1
            print('Test search product is passed')

    """" Проверка фильтров продукта магазина """

    class TestFiltersProduct:
        def test_filters_product(self, driver):
            test_filters_product = StoreBusinessRequirementsPage(driver, link1)
            test_filters_product.open()
            test_filters_product.filters_product()
            url_now = driver.current_url
            print(url_now)
            assert url_now == link2
            print('Test filters product is passed')

    """ Проверка оформления покупки """

    class TestDesignProduct:
        def test_design_product(self, driver):
            test_design_product = StoreBusinessRequirementsPage(driver, link2)
            test_design_product.open()
            test_design_product.design_product()
            test_design_product.design_product()
            url_now = driver.current_url
            print(url_now)
            assert url_now == link2
            print('Test design product is passed')




