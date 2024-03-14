import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://www.amazon.in/s?k=watches+for+men&crid=5Y76Y4O5WVXO&sprefix=wa%2Caps%2C815&ref=nb_sb_ss_ts-doa-p_3_2"
driver.get(url)
sleep(2)

click_element = driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[1]/div/span/a')
click_element.click()
sleep(4)
driver.quit()