from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from task3.Tests.singleton import Singleton
from task3.Tests.logger import CustomLogger

LOGGER = CustomLogger.get_logger(__name__)


class BasePage:
    def __init__(self, wait_time):
        self.wait_time = wait_time
        self.actions = ActionChains(Singleton.getInstance())

    def get_title(self, title):
        LOGGER.info('Getting title from current page')
        WebDriverWait(Singleton.getInstance(),
                      self.wait_time).until(EC.title_is(title))
        return Singleton.getInstance().title

    def wait_all_element_located(self, by_locator: tuple):
        LOGGER.info('Waitting specific elements to be located')
        WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_all_elements_located(by_locator))

    def wait_for_element_to_dissapear(self, by_locator: tuple):
        LOGGER.info('Waitting element to be dissapear')
        WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.invisibility_of_element_located(by_locator))

    def verify_page_by_element(self, by_locator: tuple):
        LOGGER.info('Verifing page by element ')
        element = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_all_elements_located(by_locator)
        )
        return bool(element)

    def verify_page_by_element_text(self, by_locator: tuple):
        LOGGER.info('Verifing page by element text')
        element = WebDriverWait(Singleton.getInstance(), self.wait_time).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def verify_page_by_url_params(self, filter_name):
        LOGGER.info('Verifing page by filter name')
        return f'?filter={filter_name}' in Singleton.getInstance().current_url

    def scroll(self, page_split):
        LOGGER.info('Scrolling to page split')

        Singleton.getInstance().execute_script(
            f"window.scrollTo(0, document.body.scrollHeight/{page_split});")

    def check_if_alert_exist(self):
        LOGGER.info('Checking Alert Existing')
        alert_exist = True
        try:
            WebDriverWait(Singleton.getInstance(), self.wait_time/4).until(
                EC.alert_is_present())
        except:
            alert_exist = False
        return alert_exist