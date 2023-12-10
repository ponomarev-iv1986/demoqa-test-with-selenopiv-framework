from selenium.webdriver import Keys

from selenopiv.core import Browser


class StudentRegistrationPage:
    def __init__(self, browser: Browser):
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
        self.date_of_birth.type(Keys.COMMAND + 'a' + Keys.NULL + f'{day} {month} {year}')



