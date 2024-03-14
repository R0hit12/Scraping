from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.python.org")
sleep(2)
elem = driver.find_element(By.NAME, "q")
# elem.clear()
# sleep(1)

elem.send_keys("pycon")
sleep(2)
elem.clear()
elem.send_keys('Community')
print(elem.is_displayed())
elem.send_keys(Keys.RETURN)
sleep(2)
new_elem = driver.find_element(By.XPATH,'//*[@id="news"]/a')
new_elem.click()
# elem = driver.find_element(By.XPATH,'//*[@id="submit"]')
#
# elem.find_element(By.XPATH,'//*[@id="submit"]')
# elem.click()


# download_ele = driver.find_element(By.ID, 'downloads')
# download_ele.click()
sleep(15)
driver.quit()