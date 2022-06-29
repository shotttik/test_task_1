from task3.Locators.BaseLocators import BaseLocators
from .BasePage import BasePage
from task3.Locators.MainLocators import MainLocators
from task3.Elements.Button import Button
from task3.WEBTools.iframes import Iframe
from task3.Locators.FrameLocators import FrameLocators


class FamesPage(BasePage):

    def __init__(self, wait_time):
        super().__init__(wait_time)

    def verify_page_by_name(self):
        return self.verify_page_by_element_text(BaseLocators.UNIQUE_HEADER)

    def text_from_located_iframes(self, frames: list) -> list:
        frames_texts = []
        for frame in frames:
            frame_loc = FrameLocators.get_frame_locator(frame["id"])
            self.iframe = Iframe(self.wait_time, frame_loc)
            self.iframe.switch_to_iframe()
            frames_texts.append(self.iframe.get_text_from_body())
            self.iframe.switch_to_default()
        return frames_texts
