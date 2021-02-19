from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


PRODUCT_RESULT = (By. XPATH, "//span[@data-component-type='s-search-results']//a[.//span[@class='a-price']]")

@when ('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


