from demoqa_test_with_selenopiv_framework.pages.buttons_page import ButtonsPage


def test_double_click_btn(browser):
    # GIVEN
    page = ButtonsPage(browser)
    page.open_buttons_form()

    # WHEN
    page.activate_double_click_btn()

    # THEN
    page.should_be_visible(page.double_click_msg)
    page.should_have_exact_text(page.double_click_msg, 'You have done a double click')


def test_right_click_btn(browser):
    # GIVEN
    page = ButtonsPage(browser)
    page.open_buttons_form()

    # WHEN
    page.activate_right_click_btn()

    # THEN
    page.should_be_visible(page.right_click_msg)
    page.should_have_exact_text(page.right_click_msg, 'You have done a right click')


def test_dynamic_click_btn(browser):
    # GIVEN
    page = ButtonsPage(browser)
    page.open_buttons_form()

    # WHEN
    page.activate_dynamic_click_btn()

    # THEN
    page.should_be_visible(page.click_msg)
    page.should_have_exact_text(page.click_msg, 'You have done a dynamic click')
