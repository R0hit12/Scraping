import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait

driver = webdriver.Chrome()
driver.get("https://afriwise.com/")
driver.maximize_window()
sleep(3)

try:
    cookie_container = driver.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']")
    close_button = cookie_container.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']/button")
    close_button.click()
    sleep(5)
except:
    print("Not found")

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
sleep(10)

submit_button = driver.find_element(By.XPATH,"//*[@id='__nuxt']/div/main/div[2]/div/div[2]/form/button")

submit_button.click()


sleep(10)

