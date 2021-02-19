from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import  WebDriverWait

# init driver
driver = webdriver.Chrome()
# driver.implicitly_wait(10) #100 ms

driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

driver.wait = WebDriverWait(driver, 10)
e = driver.wait.until.(EC.element_to_be_clickable((By.NAME,'btnK'))) #500 ms

# wait for 4 sec
# sleep(4)

# click search
e.click()
# driver.find_element(By.NAME, 'btnK').click()

# verify
# assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
