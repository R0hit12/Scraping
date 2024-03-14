import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# s = Service("C:/Users/Lenovo/Downloads/chrome-win64/chrome-win64/chrome.exe")
driver = webdriver.Chrome()
driver.get("https://in.indeed.com/")

driver.maximize_window()


job_title =[]
job_company = []
company_location = []
company_description = []

input_field = driver.find_element(By.XPATH, "//*[@id='text-input-what']")


location_field = driver.find_element(By.XPATH,"//*[@id='text-input-where']")
input_field.clear()
input_field.click()  # Focus the input field
location_field.click()
input_field.click()
input_field.send_keys("Web d")
sleep(4)
for i in range(0,10):
    element = driver.find_element(By.ID,"what-autocomplete-suggestions--"+str(i))
    a = element.text
    if a== "web designer":
        element.click()
        break
    else:
        pass
sleep(4)
input_field.click()
submit = driver.find_element(By.CLASS_NAME,"yosegi-InlineWhatWhere-primaryButton")
submit.click()



# input_field.send_keys(Keys.ENTER)
height = driver.execute_script("return document.body.scrollHeight")
print(height)
# sleep(5)
driver.quit()