from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BUTTON = (By.ID, 'dropdown_selected_size_name')
SIZE = (By.ID, 'size_name_0')

COLOR_OPTIONS = (By.CSS_SELECTOR, '')
SELECTED_COLOR = (By.CSS_SELECTOR, '')

@when('Click on Add to card button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when ('Select shoes size')
def select_size(context):
    context.driver.find_element(*SIZE_SELECTION_BUTTON).click()
    context.driver.find_element(*SIZE).click()


@then('Verify card has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {actual_text}'


# @then('Verify user can click through colors')
# def verify_can_select_colors(context):
#     expected_colors = ['Emerald', 'Ivory', 'Navi']
#     colors = context.driver.find_element(*COLOR_OPTIONS)
#     # [Webelement 0, Webelement 1, Webelement 2]
#
#     for i in range (len(colors)):
#         color.click()
#         selected_color = context.driver.find_element(*SELECTED_COLOR).text
#         assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]} but got {selected_color}