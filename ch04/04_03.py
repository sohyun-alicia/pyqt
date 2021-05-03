import requests                    # 인터넷 문서를 끌어올때
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_dvr")
tag = tags[0]

# print(html)            # 해당 페이지의 모든 내용을 가져옴
print(tag.text)
