from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/')

search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('Watches')

search_icon = driver.find_element(By.ID, 'nav-search-submit-button')
search_icon.click()

# actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
actual_text = driver.find_element(By.XPATH, "//*[@id="twotabsearchtextbox"]").text
# actual_text = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/span/div/span/h1/div/div[1]/div/div/span[3]").text
expexted_text = '"Watches"'

assert expexted_text == actual_text, f'Expected {expexted_text}, but got {actual_text}'
driver.quit()
