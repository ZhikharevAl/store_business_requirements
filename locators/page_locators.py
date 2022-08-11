from selenium.webdriver.common.by import By


class Locators:
    """ Locators test_search_product """

    INPUT_BOX = (By.CSS_SELECTOR, 'input[type="text"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    CATEGORIES_BUTTON = (By.CSS_SELECTOR, 'span[class="medium"]')
    CATEGORIES_LIST = (By.CSS_SELECTOR, 'img[src="https://static.onlinetrade.ru/img/categories2/tostery_80_1622021795'
                                        '.jpg"]')

    """ Locators test_filters_product """

    QUANTITY_PRODUCTS = (By.CSS_SELECTOR, 'a[title="45"]')
    BRENDS_BUTTON = (By.CSS_SELECTOR, 'a[data-titlefalse="Показать все бренды"]')
    BREND_BUTTON = (By.CSS_SELECTOR, 'a[title="TEFAL"]')
