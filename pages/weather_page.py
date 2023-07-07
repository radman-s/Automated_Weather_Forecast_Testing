from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class WeatherPage(BasePage):


    url = 'https://openweathermap.org/'

    @property
    def web_title(self):
        locator = Locator(By.XPATH, '//span[text()="OpenWeather"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def current_location(self):
        locator = Locator(By.CLASS_NAME, 'icon-current-location')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[placeholder="Search city"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_button(self):
        locator = Locator(By.XPATH, '//button[text()="Search"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def city_name(self):
        locator = Locator(By.XPATH, '//h2[@data-v-3e6e9f12]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def wind_speed(self):
        locator = Locator(By.CSS_SELECTOR, 'li[data-v-3208ab85]:first-child')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pressure(self):
        locator = Locator(By.CSS_SELECTOR, 'li[data-v-3208ab85]:nth-child(2)')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def humidity(self):
        locator = Locator(By.CSS_SELECTOR, 'li[data-v-3208ab85]:nth-child(3)')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def visibility(self):
        locator = Locator(By.CSS_SELECTOR, 'li[data-v-3208ab85]:nth-child(6)')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def temperature(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="heading"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def feels_like(self):
        locator = Locator(By.XPATH, '//div[starts-with(@class, "bold") and starts-with(text(), "Feels like")]')
        return BaseElement(driver=self.driver, locator=locator)





