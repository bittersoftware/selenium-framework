from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SeleniumExtended:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        return el.text

    def wait_presence_of_all_elements_located(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_visibility_of_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def scroll_to_top(self, delay=0.5):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        self.driver.implicitly_wait(delay)

    def hover_and_click(self, locator1, locator2, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        actions = ActionChains(self.driver)

        el1 = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator1)
        )

        # Hover element 1
        actions.move_to_element(el1).perform()

        # Click element 2
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator2)
        ).click()

    def move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_pixels(self, x, y):
        self.driver.execute_script(f"window.scrollBy({str(x)}, {str(y)});")
