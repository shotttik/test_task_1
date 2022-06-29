from selenium.webdriver.common.by import By


class BaseLocators:
    UNIQUE_HEADER = (By.XPATH, "//div[@class='main-header']")

    @staticmethod
    def element_list(text):
        return (
            By.XPATH, f"//div[contains(@class, 'element-list')]//span[text()='{text}']")
