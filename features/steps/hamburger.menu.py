from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

SEARCH_HAMBURGER_FIELD = (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def step_impl(context):
    context.driver.find_element(*SEARCH_HAMBURGER_FIELD)