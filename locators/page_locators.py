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
    AVAILABILITY_CHECKBOX = (By.CSS_SELECTOR, 'label[id="l5950a4a1de00bc24202c5f78a0a726be"]')
    PICK_BY_PRICE = (By.CSS_SELECTOR, 'div[data-spoiledcontent="price_active"]')
    CURRENT_PRICES = (By.CSS_SELECTOR, 'span[class="ui-slider-handle ui-corner-all ui-state-default"]')
    CONTACT = (By.CSS_SELECTOR, 'a[class="button button__blue js__filterResult_link"]')



    """ Locators test_design_product """

    DESIGN_PRODUCT = (By.CSS_SELECTOR, 'a[data-handler="buy"]')
    PLACE_ON_ORDER = (By.CSS_SELECTOR, 'a[class="button button__clearGray active "]')
    CONTINUE_WITHOUT_REGISTERING = (By.CSS_SELECTOR, 'a[href="/basket.html"]')
    ORDER = (By.CSS_SELECTOR, 'input[class="button button__orange semibold js__formBoxMainButton floatRight"]')

