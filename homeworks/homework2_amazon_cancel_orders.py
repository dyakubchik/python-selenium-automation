from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


driver = webdriver.Chrome(executable_path=r'C:\Users\dmitr\PycharmProjects\python-selenium-automation\chromedriver.exe')
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/gp/help/customer/display.html')


search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('Cancel Order')
search_field.send_keys(Keys.ENTER)


# actual_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[4]/div/div[1]/h2/a").text
# actual_text = driver.find_element(By.XPATH, "//a[contains(@href,'1612234044&amp;sr=1-1')]").text
# actual_text = driver.find_element(By.XPATH, "//a[(@href='1612234044&amp;sr=1-1')]").text
actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text #// look diper to html element


expexted_text = 'Cancel Items or Orders'

assert expexted_text == actual_text, f'Expected {expexted_text}, but got {actual_text}'
driver.quit()

