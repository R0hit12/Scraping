import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://in.indeed.com/")
driver.maximize_window()

job_title =[]
job_company = []
c_location = []
c_description = []

input_field = driver.find_element(By.XPATH, "//*[@id='text-input-what']")


location_field = driver.find_element(By.XPATH,"//*[@id='text-input-where']")
input_field.clear()
input_field.click()  # Focus the input field
location_field.click()
input_field.click()
input_field.send_keys("Web developer")
input_field.send_keys(Keys.ENTER)
sleep(5)




# j_title = driver.find_element(By.XPATH,"//*[@id='text-input-what']")
# j_title.send_keys("Web developer fresher")
# company_location = driver.find_element(By.XPATH,"//*[@id='text-input-where']")
# company_location.send_keys("Chandigarh")
# submit = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[2]/button")
# submit.click()

# driver.execute_script("window.scrollTo(0,2000)")
# for i in range(1,5):
#         try:
#                 title = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[1]/h2/a/span".format(i))
#                 # print(title.text)
#                 company = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[2]/div/span".format(i))
#                 # print(company.text)
#                 # description = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[2]/tbody/tr/td/div[1]/div/ul/li[1]".format(i))
#                 #
#                 location = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/span/div[4]/div[5]/div[2]/div/div/div/div/div/div[3]/div[1]/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[2]/div/div".format(i))
#                 # print(job_title)
#                 job_title.append(title)
#                 job_company.append(company)
#                 # c_description.append(description)
#                 # c_location.append(location)
#         except:
#                continue
#
#
#
#
# print(len(job_title),len(job_company),len(c_description))
# print(job_company)
# print(c_location)
# print(job_title)
# # df = pd.DataFrame({"JOB_TITLE":job_title,"Company":job_company,"Description":c_description,"Location":c_location})
# # df.to_excel("indeed.xlsx")
# sleep(10)
driver.quit()