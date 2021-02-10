from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys(search_query)


@when('Click on Amazon search icon')
def click_search_amazon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Product results for {results_word} are shown on Amazon')
def verify_search_result(context, results_word):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = f'{results_word}'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'\


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    assert query in context.driver.current_url, f'Query not in {context.driver.current_url}'