import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/searchresults.en-gb.html?aid=2311236&label=en-in-booking-desktop-CmH43mrsjzqEEFQPgVycoAS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9303130%3Ali%3Adec%3Adm&no_rooms=1&srpvid=9936236d997101d1&highlighted_hotels=1560359&redirected=1&city=-2092770&hlrd=no_dates&group_adults=2&source=hotel&group_children=0&expand_sb=1&keep_landing=1&sid=13a1dbe2a5266461538ffc593a3f73f0#hotelTmpl"
r = requests.get(url)

print(r.text)
soup = BeautifulSoup(r.text,'lxml')
# print(soup.prettify())

names = soup.find_all("div", attrs={"data-testid": "title" })
print(names)

