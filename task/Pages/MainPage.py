
from task.Elements.Button import Button
from task.Elements.InputField import InputField
from task.Elements.TextField import TextField
from task.Locators.MainLocators import MainLocators
from task.Utils.AccountUtils import AccountUtils
from .BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, wait_time):
        super().__init__(wait_time)
        self.title_span = TextField(
            MainLocators.PAGE_TITLE, "Page Title", wait_time)
        self.first_name_input = InputField(
            MainLocators.FIRST_NAME_INPUT, 'First Name Input Element', wait_time)
        self.last_name_input = InputField(
            MainLocators.LAST_NAME_INPUT, 'Last Name Input Element', wait_time)
        self.email_input = InputField(
            MainLocators.EMAIL_INPUT, 'Email Address Input Element', wait_time)
        self.password_input = InputField(
            MainLocators.PASSWORD_INPUT, 'Password Input Element', wait_time)
        self.confirm_password_input = InputField(
            MainLocators.CONFIRM_PASSWORD_INPUT, 'Confirm Password Input Element', wait_time)
        self.submit_btn = Button(
            MainLocators.CREATE_ACC_BTN, "Submit button on the Create Account page", wait_time)

    def verify_page(self) -> str:
        return self.verify_page_by_element_text(self.submit_btn.by_locator)

    def fill_inputs(self):
        account = AccountUtils.generate_account()

        self.first_name_input.send_text_to_element(account.first_name)
        self.last_name_input.send_text_to_element(account.last_name)
        self.email_input.send_text_to_element(account.email)
        self.password_input.send_text_to_element(account.password)
        self.confirm_password_input.send_text_to_element(account.password)

    def submit_form(self):
        self.submit_btn.do_click_with_action()
