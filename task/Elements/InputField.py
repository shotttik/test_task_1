from task.Core.webdriver import Browser
from .BaseElement import BaseElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
LOGGER = logging.getLogger(__name__)


class InputField(BaseElement):

    def send_text_to_element(self, text):
        LOGGER.info(f"Sending text to element {self.name}")
        element = WebDriverWait(Browser.driver, self.wait_time).until(
            EC.visibility_of_element_located(self.by_locator)
        )
        element.send_keys(text)
