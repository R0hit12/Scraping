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
t_posted = []


driver = webdriver.Chrome()
for i in range(1,4):
    url = "https://www.flipkart.com/shivark-new-designer-set-3-black-dial-watch-1-bracelet-boys-analog-men/product-reviews/itm097ce701fe44a?pid=WATGNH9QQKC7JZEY&lid=LSTWATGNH9QQKC7JZEYKCULEP&marketplace=FLIPKART&page="+str(i)
    driver.get(url)
    driver.maximize_window()
    soup = BeautifulSoup(driver.page_source,"lxml")
    sleep(4)

    parent_div = soup.find_all("div",class_="row _1ExUpQ")

    try:
        customer_name = soup.find_all("p",class_="_2sc7ZR _2V5EHH _1QgsS5")
        customer_rating = soup.find_all("div",class_="_3LWZlK _1BLPMq _3B8WaH")
        customer_review = soup.find_all("div",class_="_6K-7Co")
        if customer_review == None:
            customer_review



        for div in parent_div:
            time_posted = div.find_all("p")
            t_posted.append(time_posted[1].text)

        for name,rating,review in zip(customer_name,customer_rating,customer_review):
            c_name.append(name.text)
            c_rating.append(rating.text)
            c_review.append(review.text)
    except:
        print("Not found")


print(len(c_name))
print(len(c_rating))
print(len(c_review))
print(len(t_posted))
print((c_name))
print((c_rating))
print((c_review))
print((t_posted))
new_list = t_posted[1::2]
t_posted.pop()
print(len(t_posted))


df = pd.DataFrame({"Customer":c_name,"Rating":c_rating,"Review":c_review,"Posted_in":t_posted})
df.to_excel("Full_reviews.xlsx")
# print(new_list)

sleep(4)