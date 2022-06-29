from selenium.webdriver.common.by import By


class AlertLocators:

    @staticmethod
    def alert_button(id):
        return (By.XPATH, f"//button[@id='{id}']")

    @staticmethod
    def alert_result(id):
        return (By.XPATH, f"//span[@id='{id}']")
