from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def is_displayed(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return self.web_element.is_displayed()

    def click_wait(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def click(self):
        self.web_element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    def text(self):
        text = self.web_element.text
        return text

    def select_dropdown(self, val):
        element = Select(self.web_element)
        element.select_by_value(val)
        return None

    def clic_intercepted(self):
        element = ActionChains(self.driver)
        element.move_to_element_with_offset(self.web_element, 5, 0)
        element.click().perform()

    def enter(self):
        element = ActionChains(self.driver)
        element.send_keys(Keys.ENTER).perform()
        return None