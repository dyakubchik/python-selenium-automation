from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

CANCEL_SEARCH_FIELD = (By.ID, 'helpsearch')
LINK_RESULT_HELP_PAGE = (By.XPATH, "//div[@class='help-content']/h1")

@given('Open Amazon cancel order page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_query} into help library search field')
def input_amazon_help_search(context, search_query):
    search_field = context.driver.find_element(*CANCEL_SEARCH_FIELD)
    search_field.send_keys(search_query)
    search_field.send_keys(Keys.ENTER)

@then('Search results for {result} are shown on help page')
def verify_search_result(context, result):
    actual_text = context.driver.find_element(*LINK_RESULT_HELP_PAGE).text
    expected_text = f'{result}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
