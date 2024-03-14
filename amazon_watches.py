from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()
# a_choice = 3
# other = 2

search_bar = driver.find_element(By.ID,'twotabsearchtextbox')
search_bar.send_keys('watches for men')
search_bar.send_keys(Keys.RETURN)
driver.execute_script("window.scrollTo(0,400)")


for i in range(7,20):
    try:
        watch_card = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]'.format(i))
    except:
        pass

    # mobile_phone_home =driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[5]')
    # mobile_phone_home.click()
    try:
        watch_brand_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[2]/div/h2/span'.format(i))
        watch_brand = watch_brand_element.text
    except:
        try:
            watch_brand_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[2]/div/h2/span'.format(i))
            watch_brand = watch_brand_element.text
        except:
            watch_brand =''

    try:
        watch_name_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[2]/h2/a/span'.format(i))
        watch_name = watch_name_element.text
    except:
        try:
            watch_name_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[2]/h2/a/span'.format(i))
            watch_name = watch_name_element.text
        except:
            watch_name = ''

    try:
        total_ratings_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[3]/div[1]/span[2]/a/span'.format(i))
        total_ratings = total_ratings_element.text
    except:
        try:
            total_ratings_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[3]/div[1]/span[2]/a/span'.format(i))
            total_ratings = total_ratings_element.text
        except:
            total_ratings = ''

    # price = driver.
    # find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[9]/div/div/span/div/div/div[2]/div[4]/div/div[1]/a/span/span[2]/span[2]')
    try:
        price = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[4]/div/div[1]/a/span/span[2]/span[2]'.format(i))
        watch_price = price.text
    except:
        try:
            price = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[4]/div/div[1]/a/span/span[2]/span[2]'.format(i))
            watch_price = price.text
        except:
            watch_price = ''

    try:
        discount_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[4]/div/div[1]/span[2]'.format(i))
        discount = discount_element.text
    except:
        try:
            discount_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[4]/div/div[1]/span[2]'.format(i))
            discount = discount_element.text
        except:
            discount = ''



    try:
        color_elements = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[1]/div/div/a/u'.format(i))
        color_patterns = color_elements.text
    except:
        try:
            color_elements = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[1]/div/div/a/u'.format(i))
            color_patterns = color_elements.text
        except:
            color_patterns = ''


    try:
        total_price_element  = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[3]/div[4]/div/div[1]/a/div/span[2]/span[2]'.format(i))
        total_price = total_price_element.text
    except:
        try:
            total_price_element = watch_card.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{0}]/div/div/span/div/div/div[2]/div[4]/div/div[1]/a/div/span[2]/span[2]'.format(i))
            total_price = total_price_element.text
        except:
            total_price = ''





    print('---------------')
    print("Watch-brand=", watch_brand)
    print("Watch-name = ",watch_name)
    print("Ratings=",total_ratings)
    print("Current price=",watch_price)
    print("Actual price=",total_price)
    print("Discount=",discount)
    print("color patterns available=",color_patterns)



sleep(20)

