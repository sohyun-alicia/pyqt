import requests
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

bitcoin = r.json()      # Json포맷의 데이터를 딕셔너리로 변환

timestamp = bitcoin['timestamp']            # 최종 체결 시각
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)
