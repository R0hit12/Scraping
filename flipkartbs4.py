from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
a = driver.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
driver.maximize_window()

soup = BeautifulSoup(driver.page_source, 'lxml')
  # Make sure to quit the driver after scraping the page.

mobile_names = soup.find_all("div", class_="_4rR01T")  # Assuming this class holds mobile names.
mobile_prices = soup.find_all("div",{"class":"_30jeq3 _1_WHN1"})
print(mobile_names)
print(mobile_prices)
number = 1
for i in mobile_names:
    for j in mobile_prices:
        print(number,"Mobilename=",i.text,"||,Price=",j.text)
        number+=1
        if number==10:
            break
    break
phone_about = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')
phone_about.click()
a = driver.get("https://www.flipkart.com/poco-c55-cool-blue-128-gb/p/itm26aca9fd143ba?pid=MOBGMXSWJHRVUWFE&lid=LSTMOBGMXSWJHRVUWFESKZGEW&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=da8ac2dc-89f3-443e-be31-064d3eceaaff.MOBGMXSWJHRVUWFE.SEARCH&ppt=hp&ppn=homepage&ssid=far1rcm34g0000001709635783998&qH=eb4af0bf07c16429")




driver.quit()










sleep(15)