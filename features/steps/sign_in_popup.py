from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


SIGN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@when ('Click sign in from popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_BTN))
    e.click()

@then('Verify Sigh in page opens')
def verify_sign_in_page_opens(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        # f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'

    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
        f'Url {context.driver.current_url} does not include https://www.amazon.com/ap/signin'
