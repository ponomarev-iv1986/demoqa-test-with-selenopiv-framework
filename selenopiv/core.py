from dataclasses import dataclass

from selenium.common import WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from selenopiv.selector import to_locator
from selenopiv.wait import CustomWait


@dataclass
class Config:
    driver: WebDriver
    timeout: float = 3.0
    base_url: str = ''


class Browser:
    def __init__(self, config: Config):
        self.config = config
        self.driver: WebDriver = config.driver
        self.wait = CustomWait(
            driver=config.driver, timeout=config.timeout, ignored_exceptions=(WebDriverException,)
        )

    def visit(self, url):
        self.driver.get(self.config.base_url + url)

    def quit(self):
        self.driver.quit()

    def element(self, selector):
        return Element(selector, self)

    def all_elements(self, selector):
        return Collection(selector, self)


class Element:
    def __init__(self, selector, browser: Browser):
        self.selector = selector
        self.driver = browser.driver
        self.wait = browser.wait

    # COMMANDS

    def press_enter(self):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            webelement.send_keys(Keys.ENTER)
            return True

        self.wait.until(command)
        return self

    def type(self, text):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            webelement.send_keys(text)
            return True

        self.wait.until(command)
        return self

    def click(self):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            webelement.click()
            return True

        self.wait.until(command)
        return self

    def click_by_action(self):
        def command(driver: WebDriver):
            action = ActionChains(driver)
            webelement = driver.find_element(*to_locator(self.selector))
            action.click(webelement).perform()
            return True

        self.wait.until(command)
        return self

    def click_by_js(self):
        def command(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            driver.execute_script('arguments[0].click();', webelement)
            return True

        self.wait.until(command)
        return self

    # CONDITIONS

    def should_have_text(self, value):
        def condition(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            actual_value = webelement.text
            if actual_value != value:
                raise AssertionError(f'text of element is not "{value}"\nactual value: "{actual_value}"')
            return True

        self.wait.until(condition)
        return self

    def should_have_attribute(self, attribute, value):
        def condition(driver: WebDriver):
            webelement = driver.find_element(*to_locator(self.selector))
            actual_value = webelement.get_attribute(attribute)
            if actual_value != value:
                raise AssertionError(f'attribute "{attribute}" is not "{value}"\nactual value: "{actual_value}"')
            return True

        self.wait.until(condition)
        return self


class Collection:
    def __init__(self, selector, browser: Browser):
        self.selector = selector
        self.driver = browser.driver
        self.wait = browser.wait

    # CONDITIONS

    def should_have_texts(self, *args):
        def condition(driver: WebDriver):
            webelements = driver.find_elements(*to_locator(self.selector))
            actual_values = tuple([webelement.text for webelement in webelements])
            if actual_values != args:
                raise AssertionError(f'text of elements is not {args}\nactual text: {actual_values}')
            return True

        self.wait.until(condition)
        return self
