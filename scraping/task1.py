import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
w_brand = []
w_price = []
w_discount = []
w_description = []
t_reviews = []
c_name = []
c_rating = []
c_review = []
t_stars = []



driver = webdriver.Chrome()
url = "https://www.flipkart.com/search?q=watch%20for%20men&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
driver.get(url)
driver.maximize_window()
sleep(3)
soup = BeautifulSoup(driver.page_source,"lxml")
# print(soup.prettify())

# watch name ---------------
page = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")
rows = page.find_all("div",class_ ="_1AtVbE col-12-12")
print(len(rows))
rows = len(rows)
length = page.find_all("div",{"class":"_1xHGtK _373qXS"})
length = len(length)
# print(len(length))
watch_company = page.find_all("div", {"class": "_2WkVRV"},limit=8)
watch_price = page.find_all("div",class_="_30jeq3")
try:
    watch_discount= page.find_all("div",class_ = "_3Ay6Sb")
except:
    watch_discount.append("no discount")

counter = 1

for company,price,discount in zip(watch_company,watch_price,watch_discount):
    # print(counter,"-",company.text,price.text,discount.text)
    counter = counter+1

    w_brand.append(company.text)
    w_price.append(price.text)
    w_discount.append(discount.text)




print(w_brand)
print(w_price)
print(w_discount)
sleep(3)
for j in range(2,4):
    for i in range(1,5):
        item_link = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/a".format(j=j,i=i))
        item_link.click()
        sleep(2)

        driver.switch_to.window(driver.window_handles[-1])
        sleep(2)

    # get_url = driver.current_url
    # print("Current URL:", get_url)
        soup = BeautifulSoup(driver.page_source, "lxml")
        try:
            customer_names = soup.find("p",class_="_2sc7ZR _2V5EHH _1QgsS5")
            customer_ratings = soup.find("div",class_="_3LWZlK _1BLPMq _3B8WaH")
            customer_review = soup.find("div",class_="_6K-7Co")

            for name,rating,review in zip(customer_names,customer_ratings,customer_review):
                c_name.append(name)
                c_rating.append(rating.text)
                c_review.append(review.text)
        except:
            c_name.append("Not found")
            c_rating.append("Not found")
            c_review.append("Not found")



        try:
            reviews = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[7]/div[4]/div/div[1]/div[2]/span[2]/span")
            t_reviews.append(reviews.text)
        except:
            t_reviews.append("No reviews yet")



        try:
            stars = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div/div/span[1]/div")
            # print(stars.text)
            t_stars.append(stars.text)
        except:
            t_stars.append("Not found")
        sleep(2)

    # Close the current window/tab
        driver.close()

    # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
print(w_brand)
print(w_price)
print(w_discount)
print(t_stars)
print(c_name)
print(c_review)
print(c_rating)

df = pd.DataFrame({"Brand":w_brand,"Price":w_price,"Discount":w_discount,"Stars":t_stars,"Customer":c_name,
                   "Customer_Ratings":c_rating,"Reviews":t_reviews})
print(df)
df.to_excel("Watches.xlsx")
sleep(4)
driver.quit()


