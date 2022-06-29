from task3.Locators.BaseLocators import BaseLocators
from .BasePage import BasePage
from task3.Locators.AlertLocators import AlertLocators
from task3.Locators.AlertLocators import AlertLocators
from task3.Tests.logger import CustomLogger
from task3.Elements.TextField import TextField
from task3.Elements.Button import Button
LOGGER = CustomLogger.get_logger(__name__)


class AlertsPage(BasePage):
    def __init__(self, wait_time):
        super().__init__(wait_time)
        self.menu_alert_btn = Button(
            BaseLocators.element_list('Alerts'), 'Menu Alerts BTN', wait_time)
        self.menu_nested_frames_btn = Button(BaseLocators.element_list(
            'Nested Frames'), 'Menu Alerts BTN', wait_time)

    def verify_page_by_name(self):
        return self.verify_page_by_element_text(BaseLocators.UNIQUE_HEADER)

    def open_alert(self, locator):
        alert_btn = Button(locator, 'Alert Button', self.wait_time)
        alert_btn.do_click()

    def get_alert_result_text(self, result_id):
        result_locator = AlertLocators.alert_result(result_id)
        result_field = TextField(
            result_locator, 'Alert Result Text Field', self.wait_time)
        result_text = result_field.get_element_text()
        LOGGER.info(f'Text "{result_text}" has appeared on page')
        return result_text

    def go_to_alerts(self):
        self.menu_alert_btn.do_click()

    def go_to_nested_frames(self):
        self.menu_nested_frames_btn.do_click()
