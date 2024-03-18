import pandas as pd
from selenium import webdriver
from seleniumbase import Driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
driver.maximize_window()
sleep(4)

job_button = driver.find_element(By.XPATH,"/html/body/nav/ul/li[4]/a")
job_button.click()
sleep(5)

job_search = driver.find_element(By.XPATH,"//*[@id='job-search-bar-keywords']")
job_search.click()
job_search.send_keys("web developer")

job_location_element = driver.find_element(By.XPATH,"//*[@id='job-search-bar-location']")
job_location_element.click()
job_location_element.clear()
job_location_element.send_keys("Chandigarh")
job_search.send_keys(Keys.ENTER)
sleep(4)



ul_element = driver.find_element(By.CLASS_NAME,"jobs-search__results-list")
li_element = ul_element.find_element(By.TAG_NAME,"li")
t_element = li_element.text
print(t_element)
sleep(5)
