import pytest

from selenopiv.core import Browser, Config


@pytest.fixture(scope='function')
def browser():
    browser = Browser(Config(timeout=5, base_url='https://demoqa.com'))

    yield browser

    browser.quit()
