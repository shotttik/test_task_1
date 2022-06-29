from task3.Locators.BaseLocators import BaseLocators
from .BasePage import BasePage
from task3.Locators.MainLocators import MainLocators
from task3.Elements.Button import Button
from task3.WEBTools.iframes import Iframe
from task3.Locators.FrameLocators import FrameLocators


class NestedFamesPage(BasePage):

    def __init__(self, wait_time):
        super().__init__(wait_time)
        self.menu_frames_btn = Button(
            BaseLocators.element_list('Frames'), 'Menu Frames BTN', wait_time)

    def verify_page_by_name(self):
        return self.verify_page_by_element_text(BaseLocators.UNIQUE_HEADER)

    def go_to_frames_page(self):
        self.menu_frames_btn.do_click()

    def text_from_nested_frames(self, frame_id):
        frame_loc = FrameLocators.get_frame_locator(frame_id)
        self.iframe = Iframe(self.wait_time, frame_loc)
        self.iframe.switch_to_iframe()
        parent_text, child_text = self.iframe.get_bodytext_parent_and_child()
        self.iframe.switch_to_default()
        return parent_text, child_text
