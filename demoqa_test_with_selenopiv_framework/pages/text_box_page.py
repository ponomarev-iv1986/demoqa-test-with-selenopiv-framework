import allure

from selenopiv.core import Browser


class TextBoxPage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.output_border = browser.element('#output .border')
        self.output_values = browser.all_elements('#output .border>p')
        self.submit = browser.element('#submit')

    # ACTIONS
    @allure.step('Открываем форму регистрации')
    def open_text_box_form(self):
        self.browser.visit('/text-box')
        self.browser.driver.maximize_window()

    @allure.step('Заполняем поле Full Name')
    def fill_full_name(self, value):
        self.full_name.type(value)

    @allure.step('Заполняем поле Email')
    def fill_email(self, value):
        self.email.type(value)

    @allure.step('Заполняем поле Current Address')
    def fill_current_address(self, value):
        self.current_address.type(value)

    @allure.step('Заполняем поле Permanent Address')
    def fill_permanent_address(self, value):
        self.permanent_address.type(value)

    @allure.step('Подтверждаем регистрацию пользователя')
    def click_submit(self):
        self.submit.scroll_to_element_by_js()
        self.submit.click()

    # ASSERTS
    @allure.step(
        'Проверяем, что поле Full Name имеет атрибут '
        '{attribute} со значением {value}'
    )
    def full_name_should_have_attribute(self,
                                        attribute,
                                        value):
        self.full_name.should_have_attribute(
            attribute, value
        )

    @allure.step(
        'Проверяем, что поле Email имеет атрибут '
        '{attribute} со значением {value}'
    )
    def email_should_have_attribute(self,
                                    attribute,
                                    value):
        self.email.should_have_attribute(
            attribute, value
        )

    @allure.step(
        'Проверяем, что поле Current Address имеет атрибут '
        '{attribute} со значением {value}'
    )
    def current_address_should_have_attribute(self,
                                              attribute,
                                              value):
        self.current_address.should_have_attribute(
            attribute, value
        )

    @allure.step(
        'Проверяем, что рамка с данными пользователя '
        'видна после подтверждения регистрации'
    )
    def output_border_should_be_visible(self):
        self.output_border.should_be_visible()

    @allure.step('Проверяем регистрацию пользователя')
    def output_values_should_have_texts(self, *args):
        self.output_values.should_have_texts(*args)
