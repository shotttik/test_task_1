from .BaseElement import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from task3.Tests.singleton import Singleton
import logging
LOGGER = logging.getLogger(__name__)


class InputField(BaseElement):

    def send_text_to_element(self, text):
        LOGGER.info(f"Sending text to element {self.name}")
        element = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)
        )
        element.send_keys(text)
