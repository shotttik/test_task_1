from .BasePage import BasePage
from task3.Locators.MainLocators import MainLocators
from task3.Elements.Button import Button


class MainPage(BasePage):

    def __init__(self, wait_time):
        super().__init__(wait_time)
        self.card_alert_btn = Button(
            MainLocators.CARD_BODY_ALERTS, 'Alerts, Frame & Windows', wait_time)
        self.card_elements_btn = Button(
            MainLocators.CARD_BODY_ALERTS, 'Elements', wait_time)

    def verify_page(self):
        return self.verify_page_by_element(MainLocators.HOME_BANNER)

    def go_to_alertsWindows(self):
        self.card_alert_btn.click_element_find_by_el_name()

    def go_to_elementsWindows(self):
        self.card_elements_btn.click_element_find_by_el_name()
