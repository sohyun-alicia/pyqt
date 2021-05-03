import pybithumb


# 비트코인의 호가 정보
orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

for k in orderbook:
    print(k)
