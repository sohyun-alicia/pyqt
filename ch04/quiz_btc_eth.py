import requests
from bs4 import BeautifulSoup


def get_price(a):
    url = "https://www.bithumb.com/"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tag = soup.select(a)[0]

    return tag.text

print(get_price("#assetRealBTC_KRW"))
print(get_price("#assetRealETH_KRW"))