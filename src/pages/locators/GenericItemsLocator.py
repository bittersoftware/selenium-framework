from selenium.webdriver.common.by import By


class GenericItemsLocator:

    COOKIE_BTN = (By.CSS_SELECTOR, "a.cookie-accept")
    CLOSE_MODAL = (By.CSS_SELECTOR, "button.modal-close-btn")
