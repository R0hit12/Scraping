from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
sleep(2)
elem = driver.get("https://demoqa.com/elements")
sleep(2)
driver.execute_script("window.scrollTo(0,200)")
buttons = driver.find_element(By.ID,'item-4')
buttons.click()
driver.execute_script("window.scrollTo(0,300)")
sleep(4)
d_click = driver.find_element(By.ID,'doubleClickBtn')
action_chains = ActionChains(driver)
action_chains.double_click(d_click).perform()
# Create an ActionChains object
r_click = driver.find_element(By.ID,'rightClickBtn')
action_chains = ActionChains(driver)

# Perform a right-click on the element
action_chains.context_click(r_click).perform()
sleep(5)
