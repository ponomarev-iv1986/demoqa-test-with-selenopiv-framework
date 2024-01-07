from demoqa_test_with_selenopiv_framework.pages.student_registration_page import \
    StudentRegistrationPage


def test_login_with_student_registration_form(browser):
    # GIVEN
    page = StudentRegistrationPage(browser)
    page.open_student_registration_form()

    # WHEN
    page.fill_first_name('Bill')
    page.fill_last_name('Gates')
    page.fill_email('BillGates@gmail.com')
    page.select_gender('male')
    page.fill_mobile_number('0123456789')
    page.fill_date_of_birth('28', 'October', '1955')
    page.fill_subject('English')
    page.select_hobbies('Sports', 'Reading', 'Music')
    page.load_picture('car.jpeg')
    page.fill_address('Microsoft Campus')
    page.fill_state('NCR')
    page.fill_city('Noida')
    page.click_submit()

    # THEN
    page.should_have_registered(
        'Bill Gates',
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


def test_first_name_have_placeholder(browser):
    page = StudentRegistrationPage(browser)
    page.open_student_registration_form()

    page.first_name_should_have_attribute_placeholder()


def test_fail():
    assert False
