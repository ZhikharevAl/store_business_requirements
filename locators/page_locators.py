from selenium.webdriver.common.by import By


class Locators:
    INPUT_BOX = (By.CSS_SELECTOR, 'input[type="text"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
