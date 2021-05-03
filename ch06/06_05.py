import pybithumb
import time

con_key = "e061afdd1328045d4cb378f91ff73c89"
sec_key = "09a5c0872709084c1716ef734f22b0aa"

bithumb = pybithumb.Bithumb(con_key, sec_key)


# 지정가 매수는 buy_limit_order() 메서드를 사용
# buy_limit_order() 메서드의 파라미터로 구매하고자 하는 가상화폐의 티커, 지정가, 매수 수량을 순서대로 입력
order = bithumb.buy_limit_order("BTC", 3900000, 0.001)
print(order)