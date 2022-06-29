from selenium.webdriver.common.by import By


class FrameLocators:

    FRAMES_WRAPPER = (By.XPATH, "//div[@id='framesWrapper']")

    @staticmethod
    def get_frame_locator(id):
        return (By.XPATH, f"//iframe[@id='{id}']")
