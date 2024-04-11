import pytest
import json
from .webdriver import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope='session')
def config():
    with open('task3/Resources/config.json') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in ['chrome', 'firefox']:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config


@pytest.fixture(scope="session")
def test_data():
    with open('task3/Resources/data.json') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture(scope="class")
def init_driver(request, config_browser, test_data):
    browser = Browser(config_browser)
    request.cls.wait_time = browser.wait_time
    request.cls.testing_data = test_data["testing_data"]
    # WebDriverWait(browser.driver, browser.wait_time).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    # )

    browser.driver.implicitly_wait(c.wait_time)
    yield browser.driver
    browser.driver.quit()
