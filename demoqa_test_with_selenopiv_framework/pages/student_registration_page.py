import os

from selenopiv.core import Browser
from project import BASE_DIR


class StudentRegistrationPage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender_male = browser.element('//div[@id="genterWrapper"]//*[contains(text(), "Male")]')
        self.gender_female = browser.element('//div[@id="genterWrapper"]//*[contains(text(), "Female")]')
        self.gender_other = browser.element('//div[@id="genterWrapper"]//*[contains(text(), "Other")]')
        self.mobile_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsWrapper #subjectsInput')
        self.subjects_option = browser.element('#subjectsWrapper #react-select-2-option-0')
        self.hobby_sports = browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Sports")]')
        self.hobby_reading = browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Reading")]')
        self.hobby_music = browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Music")]')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state #react-select-3-input')
        self.state_option = browser.element('#state [id^=react-select-3-option]')
        self.city = browser.element('#city #react-select-4-input')
        self.city_option = browser.element('#city [id^=react-select-4-option]')
        self.submit = browser.element('#submit')
        self.table_responsive = browser.all_elements('.table-responsive td:nth-of-type(2)')

    # HELPERS

    def _select_month(self, month):
        return self.browser.element(
            f'//select[contains(concat(" ", normalize-space(@class), " "), " react-datepicker__month-select ")]'
            f'/option[contains(text(), "{month}")]'
        )

    def _select_year(self, year):
        return self.browser.element(
            f'//select[contains(concat(" ", normalize-space(@class), " "), " react-datepicker__year-select ")]'
            f'/option[contains(text(), "{year}")]'
        )

    def _select_day(self, day):
        return self.browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        )

    # ACTIONS

    def open_student_registration_form(self):
        self.browser.visit('/automation-practice-form')
        self.browser.driver.maximize_window()

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def select_gender(self, gender: str):
        gender = gender.title()
        if gender == 'Male':
            self.gender_male.click()
        elif gender == 'Female':
            self.gender_female.click()
        elif gender == 'Other':
            self.gender_other.click()
        else:
            raise ValueError('gender must be male, female, or other')

    def fill_mobile_number(self, value):
        self.mobile_number.type(value)

    def fill_date_of_birth(self, day, month, year):
        """
        Only for MacOS:
        self.date_of_birth.type(Keys.COMMAND + 'a' + Keys.NULL + f'{day} {month} {year}')
        """
        self.date_of_birth.click()
        self._select_month(month).click()
        self._select_year(year).click()
        self._select_day(day).click()

    def fill_subject(self, value):
        self.subjects.type(value)
        self.subjects_option.click()

    def select_hobbies(self, *args):
        hobbies_list = [hobby.title() for hobby in args]
        if 'Sports' in hobbies_list:
            self.hobby_sports.click()
        if 'Reading' in hobbies_list:
            self.hobby_reading.click()
        if 'Music' in hobbies_list:
            self.hobby_music.click()

    def load_picture(self, value):
        path = os.path.join(BASE_DIR, 'tests', 'resources', value)
        self.picture.type(path)

    def fill_address(self, value):
        self.address.type(value)

    def fill_state(self, value):
        self.state.type(value)
        self.state_option.click_by_js()

    def fill_city(self, value):
        self.city.type(value)
        self.city_option.click_by_js()

    def click_submit(self):
        self.submit.press_enter()

    # SHOULDS

    def should_have_registered(self, *args):
        self.table_responsive.should_have_texts(*args)

    def first_name_should_have_attribute_placeholder(self):
        self.first_name.should_have_attribute('placeholder', 'First Name')
