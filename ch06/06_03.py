import pybithumb
import time

con_key = "e061afdd1328045d4cb378f91ff73c89"
sec_key = "09a5c0872709084c1716ef734f22b0aa"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# 1초에 10개씩 모든 가상화폐의 잔고를 화면에 출력
for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)