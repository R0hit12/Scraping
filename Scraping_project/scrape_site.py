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
driver.get("https://app.afriwise.com/dashboard")
driver.maximize_window()

sleep(6)


try:
    cookie_container = driver.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']")
    close_button = cookie_container.find_element(By.XPATH,"//*[@id='CybotCookiebotDialogHeader']/button")
    close_button.click()
    sleep(5)
except:
    print("Not found")

search_bar = driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/input")
search_bar.click()
search_bar.send_keys("DRC")
search_bar.send_keys(Keys.ENTER)

sleep(4)