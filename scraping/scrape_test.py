import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

c_name = []
c_rating = []
c_review = []

driver = webdriver.Chrome()
url = "https://www.flipkart.com/limestone-bleed-blue-day-date-functioning-strap-adult-quartz-analog-watch-men/p/itm5082b2caa2252?pid=WATFHJCZSDYUGCHG&lid=LSTWATFHJCZSDYUGCHGPQBTJF&marketplace=FLIPKART&q=watch+for+men&store=r18%2Ff13&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_NMvcvjeIhrKgHv1fA6LJslzCSo6TbUwpgnaUeQAlDbWVuKN2FTAchHEb-TTntPr5oIE8O29KknGFgEiHeIHPIQ%3D%3D&ppt=sp&ppn=sp&qH=555fccd53ee1fb27"
driver.get(url)
driver.maximize_window()
sleep(3)
soup = BeautifulSoup(driver.page_source,"lxml")

soup = BeautifulSoup(driver.page_source, "lxml")
try:
    customer_names = soup.find_all("p", class_="_2sc7ZR _2V5EHH _1QgsS5")
    for i in customer_names:
        print(i.text)
except:
    print("not found")
customer_ratings = soup.find_all("div", class_="_3LWZlK _1BLPMq _3B8WaH")
# print(customer_ratings)
customer_review = soup.find_all("div", class_="_6K-7Co")
print(customer_review)



# for name, rating, review in zip(customer_names, customer_ratings, customer_review):
#     c_name.append(name)
#     c_rating.append(rating)
#     c_review.append(review)

#
# print(c_name)
# print(c_rating)
# print(c_review)

sleep(5)