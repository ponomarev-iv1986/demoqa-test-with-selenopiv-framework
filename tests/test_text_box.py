from demoqa_test_with_selenopiv_framework.pages.text_box_page import \
    TextBoxPage


def test_placeholders(browser):
    # GIVEN
    page = TextBoxPage(browser)
    page.open_text_box_form()

    # THEN
    page.full_name_should_have_attribute(
        'placeholder',
        'Full Name'
    )

    page.email_should_have_attribute(
        'placeholder',
        'name@example.com'
    )

    page.current_address_should_have_attribute(
        'placeholder',
        'Current Address'
    )


def test_login_with_text_box(browser):
    # GIVEN
    page = TextBoxPage(browser)
    page.open_text_box_form()

    # WHEN
    page.fill_full_name('Bill Gates')
    page.fill_email('bill@gmail.com')
    page.fill_current_address('Microsoft Campus')
    page.fill_permanent_address('MS Campus')
    page.click_submit()

    # THEN
    page.output_border_should_be_visible()
    page.output_values_should_have_texts(
        'Bill Gates',
        'bill@gmail.com',
        'Microsoft Campus',
        'MS Campus'
    )
