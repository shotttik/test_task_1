from re import S
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from task.Core.logger import CustomLogger
from task.Core.webdriver import Browser
LOGGER = CustomLogger.get_logger(__name__)

# @TODO need to logging


class Iframe:
    def __init__(self, wait_time, locator):
        self.locator = locator
        self.wait_time = wait_time

    def __get_iframe_element_by_locator(self):
        el = WebDriverWait(Browser.driver, self.wait_time).until(
            EC.visibility_of_element_located(self.locator)
        )
        return el

    def __get_child_iframe_element(self):
        el = WebDriverWait(Browser.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe'))
        )
        return el

    def get_text_from_body(self):
        el = WebDriverWait(Browser.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        return el.text

    def switch_to_iframe(self):
        Browser.driver.switch_to.frame(self.__get_iframe_element_by_locator())

    def switch_to_child_iframe(self):
        Browser.driver.switch_to.frame(self.__get_child_iframe_element())

    @staticmethod
    def switch_to_default():
        Browser.driver.switch_to.default_content()

    def get_bodytext_parent_and_child(self) -> tuple:
        parent_text = self.get_text_from_body()
        self.switch_to_child_iframe()
        child_text = self.get_text_from_body()
        return parent_text, child_text
