import pytest
import json
from .singleton import Singleton
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
    with open('task3/Resources/testing_data.json') as f:
        data = json.load(f)
        f.close()
    return data


@pytest.fixture(scope="class")
def init_driver(request, config_browser, test_data):
    singleton_i = Singleton(config_browser)
    request.cls.wait_time = singleton_i.wait_time
    request.cls.alert_items = test_data["alerts"]
    request.cls.nested_frame_item = test_data["nested_frames"]
    request.cls.frames = test_data["frames"]
    request.cls.webtable_inputs = test_data["webtable_inputs"]
    WebDriverWait(singleton_i.driver, singleton_i.wait_time).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    yield singleton_i.driver
    singleton_i.driver.quit()
