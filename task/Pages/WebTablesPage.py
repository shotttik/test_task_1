from requests import delete
from task3.Elements.Button import Button
from task3.Elements.InputField import InputField
from task3.Locators.WebTablesLocators import WebTablesLocators
from task3.Tests.logger import CustomLogger
from .BasePage import BasePage
from task3.Locators.BaseLocators import BaseLocators
LOGGER = CustomLogger.get_logger(__name__)


class WebTablesPage(BasePage):
    def __init__(self, wait_time, name):
        super().__init__(wait_time)
        self.name = name
        self.add_rec_button = Button(
            WebTablesLocators.ADD_REC_BUTTON, 'Add', self.wait_time)
        self.submit_form_button = Button(
            WebTablesLocators.SUBMIT_FORM_BUTTON, 'Submit', self.wait_time)

    def verify_page_by_name(self):
        return self.verify_page_by_element_text(BaseLocators.UNIQUE_HEADER)

    def open_registration_form(self):
        self.add_rec_button.do_click()
        self.wait_all_element_located(WebTablesLocators.USERFORM_IN_MODAL)

    def __fill_modal_form_input(self, name, id, data):
        input_locator = WebTablesLocators.modal_form_input(id)
        input_field = InputField(input_locator, name, self.wait_time)
        input_field.send_text_to_element(data)

    def __submit_modal_form(self):
        self.submit_form_button.do_click()

    def fill_modal_form(self, inputs: list, data):
        for td in inputs:
            self.__fill_modal_form_input(
                name=td["label"],
                id=td["id"],
                data=data[td["label"]]
            )
        self.__submit_modal_form()

    def delete_specifiy_row(self, text):
        self.delete_button = Button(
            WebTablesLocators.item_in_table(text, delete_button=True), "Delete", self.wait_time)
        self.delete_button.do_click()
