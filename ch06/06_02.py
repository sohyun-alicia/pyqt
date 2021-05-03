import pybithumb

con_key = "e061afdd1328045d4cb378f91ff73c89"
sec_key = "09a5c0872709084c1716ef734f22b0aa"

bithumb = pybithumb.Bithumb(con_key, sec_key)

balance = bithumb.get_balance("BTC")
# print(balance)
print(format(balance[0], 'f'))


# 비트코인의 총 잔고 / 거래 중인 비트코인의 수량 / 보유 중인 총원화 / 주문에 사용된 원화
# (0.0007, 0.0, 3.1217, 0.0)