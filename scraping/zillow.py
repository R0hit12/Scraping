import requests
import json
import pandas as pd
url = "https://www.zillow.com/async-create-search-page-state"

payload = json.dumps({
  "searchQueryState": {
    "isMapVisible": False,
    "mapBounds": {
      "west": -74.041878,
      "east": -73.833552,
      "south": 40.570842,
      "north": 40.739135
    },
    "usersSearchTerm": "Brooklyn, New York, NY",
    "regionSelection": [
      {
        "regionId": 37607,
        "regionType": 17
      }
    ],
    "filterState": {
      "sortSelection": {
        "value": "globalrelevanceex"
      },
      "isAllHomes": {
        "value": True
      }
    },
    "isListVisible": True
  },
  "wants": {
    "cat1": [
      "listResults"
    ],
    "cat2": [
      "total"
    ]
  },
  "requestId": 2,
  "isDebugRequest": False
})
headers = {
  'authority': 'www.zillow.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'zguid=24|%24a81bd53c-fb84-4a7c-9461-d890a09c24cb; zgsession=1|04e83e15-2d55-41b7-afa8-c399ba9e0d6d; _ga=GA1.2.1572258647.1710397933; _gid=GA1.2.377148687.1710397933; pxcts=97fe90f0-e1cc-11ee-b94b-2d43c81406f4; _pxvid=97fe86b8-e1cc-11ee-b94b-7f2147bfedc8; zjs_anonymous_id=%22a81bd53c-fb84-4a7c-9461-d890a09c24cb%22; zjs_user_id=null; zg_anonymous_id=%22cf9fcce4-2d0c-4000-afce-68e8c20125b7%22; JSESSIONID=2B11D08E3E634346681BCE4B536F637E; _gcl_au=1.1.880236863.1710397936; DoubleClickSession=true; __pdst=1aee15b5eaea422ebcf913072e8e64bb; _fbp=fb.1.1710397936829.944773911; _pin_unauth=dWlkPU9EZGtOVE00TkRJdE1XUm1OeTAwWVRoa0xXRXpZek10WVRjM1lXRm1PV0pqWmpSag; _clck=nk82qq%7C2%7Cfk2%7C0%7C1534; _hp2_id.1215457233=%7B%22userId%22%3A%225003167492353866%22%2C%22pageviewId%22%3A%225006822902998387%22%2C%22sessionId%22%3A%228166121464629285%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1710400837886%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; x-amz-continuous-deployment-state=AYABeNZm0JG73kkSDo7n7d4EZ9sAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADAJaVRtGD+A4XYAVdQAwovW1TBAYDppib3yXWgCMcWGokbL5spLIUPMjWwh37i6iUAlqPh9c16eJipdLtUWjAgAAAAAMAAQAAAAAAAAAAAAAAAAAAFcsJ5ptYSyHWxc8ZKu6qgz%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwMn2T%2FSxNwpH3OZPr2ovM3lMKyMvWX0xMZT6Zb; search=6|1712993626911%7Cregion%3Dbrooklyn-new-york-ny%26rb%3DBrooklyn%252C-New-York%252C-NY%26rect%3D40.739135%252C-73.833552%252C40.570842%252C-74.041878%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%0937607%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _uetsid=99da8c60e1cc11eeab7b07710981c0ac; _uetvid=99da79a0e1cc11ee85cdf95e10b3cae6; _clsk=17y2do2%7C1710401631235%7C25%7C0%7Ci.clarity.ms%2Fcollect; AWSALB=N8aiPZGevk+yiEchYxLicCEWA6svFxRPn1qiflYQyjlHAD3Xc49tK4H4iG6A4tSt0/OkmJMA4CXHrL4F35V9r60+YFiYlcJQLDZqh+lCYKbtujUGd0M00bTvDnwa; AWSALBCORS=N8aiPZGevk+yiEchYxLicCEWA6svFxRPn1qiflYQyjlHAD3Xc49tK4H4iG6A4tSt0/OkmJMA4CXHrL4F35V9r60+YFiYlcJQLDZqh+lCYKbtujUGd0M00bTvDnwa; _px3=07cd8265ca8386d680d0acdc3a542e752e2ca4c8fad6cf3c7ec7c6afb6fed53d:QZxFXZ8+hsv2Fpseyylx5jm5n0nZiQzRPFmi8h1xXitvGAAKd27cX8NgJHJZh4nBZm9MaSBzwx1TpQrjZHP2rw==:1000:9h425ANnCodqlCWJVvsJr5x0R+/OUdEy8vSw1bkr94tp4oHs5mTGxGaRot4jWZouJ+W32vLyG0jJhoFLRNLclQceyYrULBBvQVC/z8p/IsUJXgD2o7LHlIfqHXVTs/KrxL2FHiMluZ0ngjVNoASVndgVKoSS4H52PpLRuRlH3cVKthpg9/lIqGMdSvoL3cSSjlsXE8SlMLOXiwWj1230o7+YAYJLkazHw7WtNTFPxTs=; _gat=1; search=6|1712994852479%7Crect%3D40.739135%2C-73.833552%2C40.570842%2C-74.041878%26rid%3D37607%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26student-housing%3D0%26income-restricted-housing%3D0%26military-housing%3D0%26disabled-housing%3D0%26senior-housing%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0937607%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; x-amz-continuous-deployment-state=AYABeO3i6zpDnxgKb%2Fc5VCycr2IAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADKm+HxrSg7Bk2EqLQgAwY%2Fx6mRk4lxV7fy%2FBqOBUOR6IpJEkjTsKecr3Jo%2F+dXn440TJk5LABcbPvaedX1NsAgAAAAAMAAQAAAAAAAAAAAAAAAAAAHpO7SQyeZkcp2vKpIovI8n%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwkQ0V1xo9W0KPYX7gSVjyyh74u67Ro%2FUUFJZgU',
  'origin': 'https://www.zillow.com',
  'referer': 'https://www.zillow.com/brooklyn-new-york-ny/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-74.041878%2C%22east%22%3A-73.833552%2C%22south%22%3A40.570842%2C%22north%22%3A40.739135%7D%2C%22usersSearchTerm%22%3A%22Brooklyn%2C%20New%20York%2C%20NY%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A37607%2C%22regionType%22%3A17%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D',
  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
t_data = []
r = requests.request("PUT", url, headers=headers, data=payload)
a = r.json()
# print(r.json())
for i in (a['cat1']["searchResults"]["listResults"]):
  t_data.append(i)

df = pd.json_normalize(t_data)
df.to_excel('data.xlsx')