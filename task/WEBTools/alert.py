from task3.Tests.logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)


class Alert:
    def __init__(self, alert):
        self.alert = alert
        self.text = alert.text
        LOGGER.info(f'Alert with text "{self.text}" is open ')

    def accept_alert(self):
        LOGGER.info(f'Alert with text "{self.text}" is closed ')
        self.alert.accept()

    def confirm_box(self, accept=True):
        LOGGER.info(f'Alert with text "{self.text}" is closed ')
        if accept:
            self.alert.accept()
        else:
            self.alert.dismiss()

    def prompt_box(self, text):
        LOGGER.info(f'Alert with text "{self.text}" is closed ')
        self.alert.send_keys(text)
        self.alert.accept()
