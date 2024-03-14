from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium.webdriver.chrome import webdriver

w_company = []
w_name = []
w_price = []
w_discount = []
actual_price = []
driver = webdriver.Chrome()

for i in range(1,10):
    url = 'https://www.flipkart.com/search?q=watch+for+men&sid=r18%2Cf13&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=watch+for+men%7CWrist+Watches&requestId=5f066321-5f58-4e64-b329-41147fadb063&as-backfill=on&page='+str(i)
    driver.get(url)
    print(url)

    r = requests.get(url)
    # print(r.text)
    soup = BeautifulSoup(r.text,'lxml')




    page = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")
    watch_company = page.find_all("div", {"class": "_2WkVRV"},limit=10)
    watch_name = page.find_all("a", class_="IRpwTa")
    watch_price = page.find_all("div",class_ ="_30jeq3")
    total_price = page.find_all("div",class_ ="_3I9_wc")
    try:
        watch_discount = page.find_all("div",class_ ="_3Ay6Sb")
    except:
        w_price.append("no discount")



















    counter = 1

    for company, name,price,discount,totalprice in zip(watch_company, watch_name,watch_price,watch_discount,total_price):
        print(counter,"-",company.text, name.text, price.text,discount.text,totalprice.text)
        w_company.append(company.text)
        w_name.append(name.text)
        w_price.append(price.text)
        w_discount.append(discount.text)
        actual_price.append(totalprice.text)
        counter = counter+1


 #---------------Reviews ---------------#
















#
    # click =
#
#
#
# df = pd.DataFrame({"Brand":w_company,"Name":w_name,"Discounted_Price":w_price,"Discount":w_discount,"Total Price":actual_price})
# # print(df)
#
# df.to_excel("Flipkart_Watches.xlsx")

