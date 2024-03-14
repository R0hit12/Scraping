from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
sleep(2)
elem = driver.get("https://demoqa.com/elements")
sleep(2)
# new_elem = driver.find_element(By.ID,'item-0')
# new_elem.click()
#
# form = driver.find_element(By.ID,"userForm")
# driver.execute_script("arguments[0].scrollIntoView();", form.find_element(By.ID, "submit"))
#
# # new_elem.find_element(By.ID,"userName")
# uname = form.find_element(By.ID,"userName")
# uemail = form.find_element(By.ID,'userEmail')
# caddress = form.find_element(By.ID,'currentAddress')
# paddress = form.find_element(By.ID,'permanentAddress')
# submit_button = form.find_element(By.ID,'submit')
# uname.send_keys("Rohit")
# uemail.send_keys("test1@gmail.com")
# caddress.send_keys('New delhi 1234 house')
# paddress.send_keys('Shimla 176110 pin code')
# sleep(2)
# driver.execute_script("window.scrollTo(0, 800)")
# submit_button.click()
#
# sleep(15)


# CHECKBOX

checkbox = driver.find_element(By.ID,'item-1')
checkbox.click()
drop_down = driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button')
driver.execute_script("window.scrollTo(0, 400)")
drop_down.click()
sleep(5)
toggle_doc = driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/span/button')
toggle_doc.click()
sleep(3)
check_download = driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[1]')
check_download.click()
sleep(3)
check_download.click()
sleep(2)
collapse_all = driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[2]')
collapse_all.click()
sleep(5)

driver.quit()

#RADIO_BUTTON
# radio_button = driver.find_element(By.ID,'item-2')
# radio_button.click()
# driver.execute_script("window.scrollTo(0, 400)")
# # sleep(5)
# # driver.execute_script("window.scrollTo(0, 400)")
# like_button = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
# like_button.click()
# sleep(5)



