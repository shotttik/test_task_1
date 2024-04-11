from selenium.webdriver.common.by import By


class MainLocators:
    PAGE_TITLE = (By.XPATH, "//span[@data-ui-id='page-title-wrapper']")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastname']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='email_address']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='password-confirmation']")

    CREATE_ACC_BTN = (By.XPATH, "//button[@title='Create an Account']")
