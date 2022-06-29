from re import S
from task3.Tests.logger import CustomLogger
from task3.Tests.singleton import Singleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
LOGGER = CustomLogger.get_logger(__name__)

# @TODO need to logging


class Iframe:
    def __init__(self, wait_time, locator):
        self.locator = locator
        self.wait_time = wait_time

    def __get_iframe_element_by_locator(self):
        el = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.locator)
        )
        return el

    def __get_child_iframe_element(self):
        el = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe'))
        )
        return el

    def get_text_from_body(self):
        el = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body'))
        )
        return el.text

    def switch_to_iframe(self):
        Singleton.getInstance().switch_to.frame(self.__get_iframe_element_by_locator())

    def switch_to_child_iframe(self):
        Singleton.getInstance().switch_to.frame(self.__get_child_iframe_element())

    @staticmethod
    def switch_to_default():
        Singleton.getInstance().switch_to.default_content()

    def get_bodytext_parent_and_child(self) -> tuple:
        parent_text = self.get_text_from_body()
        self.switch_to_child_iframe()
        child_text = self.get_text_from_body()
        return parent_text, child_text
