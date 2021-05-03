import pyupbit

price = pyupbit.get_current_price("KRW-BTC")
print("현재 비트코인의 가격은 ", price, "입니다.")

# 비트코인, 리플 가격 리스트로 출력
price = pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"])
print(price)