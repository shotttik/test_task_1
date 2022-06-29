import pytest
from task3.Locators.FrameLocators import FrameLocators
from task3.Locators.WebTablesLocators import WebTablesLocators
from task3.Pages.ElementsPage import ElementsPage
from task3.Pages.NestedFramesPage import NestedFamesPage
from task3.Pages.MainPage import MainPage
from task3.Pages.AlertsPage import AlertsPage
from task3.Locators.AlertLocators import AlertLocators
from task3.Pages.WebTablesPage import WebTablesPage
from task3.utils import Utils
from .logger import CustomLogger
from task3.WEBTools.alert import Alert
from task3.Tests.singleton import Singleton
from task3.Pages.FramesPage import FamesPage

LOGGER = CustomLogger.get_logger(__name__)


class BaseTestCase:
    def main_verified(self):
        LOGGER.info("Test Case 1 Started")
        # Main Page
        LOGGER.info("Main page is open")
        self.main_page = MainPage(self.wait_time)
        assert self.main_page.verify_page(), "Main Page couldn't be verified"

    def go_to_AlertsWindows_page(self):
        self.main_verified()
        self.main_page.go_to_alertsWindows()
        LOGGER.info("Alerts form has appeared on page")
        # Alerts Page
        self.alerts_page = AlertsPage(self.wait_time)
        assert self.alerts_page.verify_page_by_name(
        ) == 'Alerts, Frame & Windows', "Alerts, Frame & Windows Page couldn't be verified"


# @pytest.mark.usefixtures("init_driver")
# class Test_Case_1(BaseTestCase):
#     def solve_alerts(self, result_id, enter_text):
#         alert = Alert(Singleton.getInstance().switch_to.alert)
#         # PROMPT BOX ENTER TEXT
#         if enter_text:
#             random_text = Utils.get_random_string(10)
#             alert.prompt_box(random_text)
#             result_text = self.alerts_page.get_alert_result_text(result_id)
#             clean_result_text = result_text.replace('You entered ', '')
#             assert clean_result_text == random_text, "Appeared text isn't equals to the one you've entered before"
#         # CONFIRM BOX
#         elif result_id and not enter_text:
#             alert.confirm_box(accept=True)
#             self.alerts_page.get_alert_result_text(result_id)
#         # ALERT ACCEPT
#         else:
#             alert.accept_alert()

#     def test_case(self):
#         self.go_to_AlertsWindows_page()
#         # ALERT TEST DATA
#         self.alerts_page.go_to_alerts()
#         assert self.alerts_page.verify_page_by_name(
#         ) == 'Alerts', "Alerts Page couldn't be verified"
#         for item in self.alert_items:
#             btn_id = item.get('btn_id', None)
#             if btn_id is None:
#                 continue
#             result_id = item.get('result_id', None)
#             # True or None ex. for prompt
#             enter_text = item.get('enter_text', None)

#             alert_btn_locator = AlertLocators.alert_button(btn_id)
#             self.alerts_page.open_alert(alert_btn_locator)
#             assert self.alerts_page.check_if_alert_exist(), "Alert coudn't open"
#             self.solve_alerts(result_id, enter_text)
#             assert not self.alerts_page.check_if_alert_exist(), "Alert coudn't close"


# @pytest.mark.usefixtures("init_driver")
# class Test_Case_2(BaseTestCase):
#     def test_case(self):
#         self.go_to_AlertsWindows_page()
#         self.alerts_page.go_to_nested_frames()
#         # NESTED FRAMES PAGE
#         self.nested_frames_page = NestedFamesPage(self.wait_time)
#         assert self.nested_frames_page.verify_page_by_name(
#         ) == 'Nested Frames', "Nested Frames Page couldn't be verified"

#         parent_text, child_text = self.nested_frames_page.text_from_nested_frames(
#             self.nested_frame_item['id'])
#         LOGGER.info(
#             f'There are messages "{parent_text}" & "{child_text}" present on page')
#         self.nested_frames_page.go_to_frames_page()
#         # Frames Page
#         self.frames_page = FamesPage(self.wait_time)
#         assert self.frames_page.verify_page_by_name(
#         ) == 'Frames', "Frames Page couldn't be verified"
#         LOGGER.info(
#             'Message from upper frame is equal to the message from lower frame')
#         first_iframe, second_iframe = self.frames_page.text_from_located_iframes(
#             self.frames)
#         assert first_iframe == second_iframe, 'Message from upper frame isn`t equal to the message from lower frame'


@pytest.mark.usefixtures("init_driver")
class Test_Case_3(BaseTestCase):
    def test_case(self):
        # Main Page
        self.main_verified()
        self.main_page.go_to_elementsWindows()
        # Elements Page
        self.elements_page = ElementsPage(self.wait_time, 'Elements')
        assert self.elements_page.verify_page_by_name(
        ) == self.elements_page.name, "Elements  Page couldn't be verified"
        self.elements_page.go_to_webtablesPage()
        # WebTables Page
        self.webtables_page = WebTablesPage(self.wait_time, 'Web Tables')
        LOGGER.info("Page with Web Tables form is open")
        assert self.webtables_page.verify_page_by_name(
        ) == self.webtables_page.name, "Web Tables page couldn't be verified"

        # REGISTRATION FORM
        data_csv_table = Utils.data_from_csv_table('tables')
        for data in data_csv_table:
            LOGGER.info("Registration Form has appeared on page")
            self.webtables_page.open_registration_form()
            LOGGER.info("Registration Form has closed")
            self.webtables_page.fill_modal_form(self.webtable_inputs, data)
            LOGGER.info(
                f"Data of User №{data['User#']} has appeared in a table")
            # I chose email because its unique value
            locator_row_by_email = WebTablesLocators.item_in_table(
                data['Email'])
            self.webtables_page.wait_all_element_located(
                locator_row_by_email)
            LOGGER.info("Number of records in table has changed")
            LOGGER.info(
                f"Data of User №{data['User#']} has been deleted from table")
            self.webtables_page.delete_specifiy_row(data["Email"])
            self.webtables_page.wait_for_element_to_dissapear(
                locator_row_by_email)
