from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

BENEFIT_BOXES = (By. CSS_SELECTOR, 'div.benefit-box')

@given ('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then ('Verify {expected_boxes} benefit are displayed')
def verify_benefit(context, expected_boxes):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    print(*actual_boxes, sep="\n")
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes} boxes, but we see {len(actual_boxes)}'