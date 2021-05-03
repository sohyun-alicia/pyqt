import pybithumb

detail = pybithumb.get_market_detail("BTC")
print(detail)


# 저가, 고가, 평균 거래 금액, 거래량
# (61008000.0, 62990000.0, 57330000.0, 62911000.0, 4291.90492686)