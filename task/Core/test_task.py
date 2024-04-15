import pytest

from task.Pages.MainPage import MainPage


from .logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)
# @TODO logebis gata page-bshi uketeshi ikneboda :))


@pytest.mark.usefixtures("init_driver")
class Test_Case_1:
    def main_verified(self):
        LOGGER.info("Test Case 1 Started")
        # Main Page
        LOGGER.info("Main page is open")
        self.main_page = MainPage(self.wait_time)
        assert self.main_page.verify_page(
        ) == self.testing_data["main_title"], "Main Page couldn't be verified"

    def test_case(self):
        self.main_verified()
        LOGGER.info("Filling registration form inputs.")
        self.main_page.fill_inputs()

        LOGGER.info("Verifying passwords.")
        assert self.main_page.password_input.get_element_text(
        ) == self.main_page.confirm_password_input.get_element_text()

        LOGGER.info("Submitting form.")
        self.main_page.submit_form()
