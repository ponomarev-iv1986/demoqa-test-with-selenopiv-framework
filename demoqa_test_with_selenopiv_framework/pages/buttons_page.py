import allure

from selenopiv.core import Browser, Element


class ButtonsPage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.double_click_btn = browser.element('#doubleClickBtn')
        self.right_click_btn = browser.element('#rightClickBtn')
        self.dynamic_click_btn = browser.element(
            'div>[type=button]:not(#doubleClickBtn):not(#rightClickBtn)'
        )
        self.double_click_msg = browser.element('#doubleClickMessage')
        self.right_click_msg = browser.element('#rightClickMessage')
        self.click_msg = browser.element('#dynamicClickMessage')

    # ACTIONS
    @allure.step('Открываем форму с кнопками')
    def open_buttons_form(self):
        self.browser.visit('/buttons')
        self.browser.driver.maximize_window()

    @allure.step('Выполняем Double click')
    def activate_double_click_btn(self):
        self.double_click_btn.double_click()

    @allure.step('Выполняем Right click')
    def activate_right_click_btn(self):
        self.right_click_btn.context_click()

    @allure.step('Выполняем Click')
    def activate_dynamic_click_btn(self):
        self.dynamic_click_btn.click()

    # ASSERTS
    @allure.step('Проверяем видимость элемента {element}')
    def should_be_visible(self, element: Element):
        element.should_be_visible()

    @allure.step('Проверяем что элемент {element} содержит текст {value}')
    def should_have_exact_text(self, element: Element, value):
        element.should_have_exact_text(value)
