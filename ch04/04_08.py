import requests

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

bitcoin = r.json()      # Json포맷의 데이터를 딕셔너리로 변환


print(bitcoin)
print(type(bitcoin))
print(bitcoin['last'])
print(bitcoin['bid'])
print(bitcoin['ask'])
print(bitcoin['volume'])