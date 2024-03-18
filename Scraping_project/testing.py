import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get("https://afriwise.com/login/")
driver.maximize_window()


sleep(6)

try:
    cookie_container = driver.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']")
    close_button = cookie_container.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']/button")
    close_button.click()
    sleep(5)
except:
    print("Not found")

driver.execute_script("window.scrollTo(0,300)")
sleep(3)
# Find the form element
form_element = driver.find_element(By.XPATH, "//*[@id='__nuxt']/div/main/div[2]/div/div[2]")

# Wait for the user input element to be clickable
user_input = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))

# Scroll the user input element into view
driver.execute_script("arguments[0].scrollIntoView();", user_input)

actions = ActionChains(driver)

# Perform a double-click on the user and password elements
actions.send_keys_to_element(user_input,"paul.mutegi@betika.com").perform()

password_input = WebDriverWait(driver,20).until(ec.element_to_be_clickable((By.XPATH,"//*[@id='password']")))

actions.send_keys_to_element(password_input,"%V5tVgrw45y4&246vt2").perform()
sleep(2)

submit_button = driver.find_element(By.XPATH,"//*[@id='__nuxt']/div/main/div[2]/div/div[2]/form/button")

submit_button.click()
sleep(4)

driver.get("https://app.afriwise.com/browse/knowledge/countries/CD/categories/31/326")

# Wait for the list data element to be clickable
list_data_element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='app']/div/div[4]/div/div/div/div[3]/div[2]/div/ul/li[1]/h3")))

# Print the text of the list data element
print(list_data_element.text)
sleep(4)

driver.execute_script("window.scrollTo(0,500)")

expand_button = driver.find_element(By.XPATH,"//*[@id='app']/div/div[4]/div/div/div/div[3]/div[3]/div/div[1]/div[2]/button[2]")

expand_button.click()
sleep(2)
table_data = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/p")
print(table_data.text)

sleep(3)

#
# sleep(10)

