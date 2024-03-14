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
driver.get("https://www.google.com/maps/search/restaurants+in+washington+dc/@38.895915,-77.0818783,13z/data=!3m1!4b1?entry=ttu")
driver.maximize_window()
sleep(4)



# Find the div_element
# selecting scroll body
scrollable = driver.find_element(By.XPATH,"//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]")
while True:
    driver.execute_script("arguments[0].scrollTop += 1000;", scrollable)  # Adjust the scrolling offset as needed
    sleep(4)


    for i in range(1,30):
        try:
            name = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{0}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]".format(i))
            print(name.text if name else None)
        except:
            pass

    sleep(10)