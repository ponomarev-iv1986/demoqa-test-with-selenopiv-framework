from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenopiv.core import Browser, Config

browser = Browser(Config(timeout=3, base_url='https://demoqa.com'))

browser.visit('/automation-practice-form')
browser.driver.maximize_window()

# fill personal info
browser.element('#firstName').type('Bill')
browser.element('#lastName').type('Gates')
browser.element('#userEmail').type('BillGates@gmail.com')
browser.element('//div[@id="genterWrapper"]//*[contains(text(), "Male")]').click()
browser.element('#userNumber').type('0123456789')

# fill date of birth
browser.element('#dateOfBirthInput').type(Keys.COMMAND + 'a' + Keys.NULL + '28 Oct 1955')

# fill subject
browser.element('#subjectsWrapper #subjectsInput').type('English')
browser.element('#subjectsWrapper #react-select-2-option-0').click()

# fill hobbies
browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Sports")]').click()
browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Reading")]').click()
browser.element('//div[@id="hobbiesWrapper"]//*[contains(text(), "Music")]').click()

# load picture
browser.element('#uploadPicture').type(
    '/Users/ivanponomarev/PycharmProjects/demoqa-test-with-selenopiv-framework/tests/resourcer/car.jpeg')

# address
browser.element('#currentAddress').type('Microsoft Campus')

# fill state
browser.element('#state #react-select-3-input').type('NCR')
browser.element('#state [id^=react-select-3-option]').click()

# fill City
browser.element('#city #react-select-4-input').type('Noida')
browser.element('#city [id^=react-select-4-option]').click()

browser.element('#submit').press_enter()

browser.all_elements('.table-responsive td:nth-of-type(2)').should_have_texts(
    'Bill Gate',
    'BillGates@gmail.com',
    'Male',
    '0123456789',
    '28 October,1955',
    'English',
    'Sports, Reading, Music',
    'car.jpeg',
    'Microsoft Campus',
    'NCR Noida'
)
# elements = browser.driver.find_elements(By.CSS_SELECTOR, '.table-responsive td')
# text_list = [el.text for el in elements]
# browser.element('#genterWrapper').should_have_text('Male')
