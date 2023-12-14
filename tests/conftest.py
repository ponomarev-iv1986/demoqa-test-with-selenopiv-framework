import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
import project
from selenopiv.core import Browser, Config


@pytest.fixture(scope='function')
def browser():
    if project.settings.context == 'local':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        options = Options()
        capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100',
            'selenoid:options': {
                'enableVNC': True,
                'enableVideo': False
            }
        }
        options.capabilities.update(capabilities)

        login = project.settings.selenoid_login
        password = project.settings.selenoid_password

        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )
    browser = Browser(Config(driver=driver, timeout=5, base_url='https://demoqa.com'))

    yield browser

    browser.quit()
