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
driver.execute_script("window.scrollTo(0,300)")
### SCRApe from hereeee-------

sleep(3)
next_page = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/nav/ul/li[6]/a")
next_page.click()
print("hello page 2")
# sleep(5)
try:
    exit_button = driver.find_element(By.XPATH,'//*[@id="mosaic-desktopserpjapopup"]/div[1]/button')
    exit_button.click()
    try:
        exit_button = driver.find_element(By.CLASS_NAME,"css-yi9ndv e8ju0x51")
        exit_button.click()
    except:
        print("class  not found")
        pass
    try:
        exit_button = driver.find_element(By.XPATH,'//*[@id="mosaic-desktopserpjapopup"]/div[1]/button/svg')
        exit_button.click()
    except:
        print("svg x path not found")
        pass
except:
    print("not found")
    pass
# driver.execute_script("window.scrollTo(0,4500")
sleep(150)


#
#
for i in range(1,10):
    try:
        j_title = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[1]/h2/a/span".format(i))
    # print(j_title)
        j_title = j_title.text
    except:
        j_title = "Not found"
    try:
        j_company = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[2]/div/span".format(i))
        # print(j_company)
        j_company = j_company.text
    except:
        j_company = "Not found"

    try:
        c_location = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[2]/div/div".format(i))
        # print(c_location)
        c_location = c_location.text
    except:
        c_location = "None"
    try:
        try:
            c_description = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[2]/tbody/tr/td/div[1]/div/ul/li".format(i))
            c_description = c_description.text
        except:
            c_description = driver.find_element(By.XPATH,"/html/body/main/div/div[1]/div/div[5]/div/div[1]/div[5]/div/ul/li[{0}]/div/div[1]/div/div/div/table[2]/tbody/tr/td/div[1]/div/ul/li[1]".format(i))
            c_description = c_description.text
    except:
        c_description= "Not found"

    job_title.append(j_title)
    job_company.append(j_company)
    company_location.append(c_location)
    company_description.append(c_description[:60])




print(job_title)
df = pd.DataFrame({"JOB_TITLE":job_title,"Company":job_company,"Location":company_location,"Description":company_description})
# df.to_excel("indeed.xlsx")
# sleep(5)
# driver.quit()
