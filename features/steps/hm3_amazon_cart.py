from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

CART_ICON = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
RESULTS_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

@when('Click on Amazon cart icon')
def click_cart_amazon(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify {results_cart} are shown on the page')
def verify_cart_result(context, results_cart):
    actual_text = context.driver.find_element(*RESULTS_CART).text
    expected_text = f'{results_cart}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
