import pybithumb
import time

con_key = "e061afdd1328045d4cb378f91ff73c89"
sec_key = "09a5c0872709084c1716ef734f22b0aa"

bithumb = pybithumb.Bithumb(con_key, sec_key)


# 본인 계좌의 보유 원화를 조회
#  최우선 매도 호가 금액을 얻어와 매수할 수 있는 비트코인 개수를 계산

krw = bithumb.get_balance("BTC")[2]             # 튜플을 리턴, 그중 2번 인덱스에 ‘원화 잔고’가 저장
orderbook = pybithumb.get_orderbook("BTC")      # get_orderbook() 함수는 딕셔너리를 리턴. asks'라는 키를 통해 매수 호가 내역을 리스트로 얻어올 수 있음

asks = orderbook['asks']
sell_price = asks[0]['price']                   # 매도 호가 리스트에서 인덱싱을 통해 호가 정보 하나를 불러옴
unit = krw/sell_price                           # 원화 잔고를 최우선 매도 호가 금액으로 나누면 매수 수량을 구하기
print(unit)