# Python 3.9.5
# WK League match info scraping
# File name: wkleague_match_info.py

import requests

wkleague_page = "https://www.kwff.or.kr/match"
response = requests.get(wkleague_page)
print(response.status_code)
#print(response.content)
f = open('C:\Users\yjk80\Desktop\python_projects\practice\Web_Crawling\info.txt', 'w', encoding = 'UTF-8')
f.write("hello")
f.close()
