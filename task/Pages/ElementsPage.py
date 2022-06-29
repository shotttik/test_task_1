from task3.Elements.Button import Button
from task3.Tests.logger import CustomLogger
from .BasePage import BasePage
from task3.Locators.BaseLocators import BaseLocators
LOGGER = CustomLogger.get_logger(__name__)


class ElementsPage(BasePage):
    def __init__(self, wait_time, name):
        super().__init__(wait_time)
        self.name = name
        self.menu_webtables_btn = Button(
            BaseLocators.element_list('Web Tables'), 'Menu Web Tables BTN', wait_time)

    def verify_page_by_name(self):
        return self.verify_page_by_element_text(BaseLocators.UNIQUE_HEADER)

    def go_to_webtablesPage(self):
        self.menu_webtables_btn.do_click()
