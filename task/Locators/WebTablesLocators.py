from selenium.webdriver.common.by import By


class WebTablesLocators:
    ADD_REC_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")

    USERFORM_IN_MODAL = (
        By.XPATH, "//div[@class='modal-body']//form[@id='userForm']")

    SUBMIT_FORM_BUTTON = (
        By.XPATH, "//div[@class='modal-body']//button[@id='submit']")

    @staticmethod
    def modal_form_input(id):
        return (
            By.XPATH, f"//div[@class='modal-body']//form[@id='userForm']//input[@id='{id}']")

    @staticmethod
    def item_in_table(text, delete_button=False):
        item_loc = f"//div[@class='rt-tbody']//div[contains(@class, 'rt-td') and contains(text(), '{text}')]"

        return (By.XPATH, item_loc) if not delete_button else (By.XPATH, item_loc + "/..//span[contains(@id, 'delete-record')]")
