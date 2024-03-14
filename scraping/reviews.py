import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
url = "https://www.flipkart.com/search?q=watch%20for%20men&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
driver.get(url)
driver.maximize_window()
soup = BeautifulSoup(driver.page_source, 'lxml')
sleep(3)

click_item = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a")
click_item.click()
sleep(4)
# Wait for the new page to load
# Switch to the newly opened window
driver.switch_to.window(driver.window_handles[1])
sleep(3)
# Now you can scrape data from the new URL
get_url = driver.current_url
print("Current URL:", get_url)

name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span[2]")
name_c = name.text
print("Product Name:", name_c)

