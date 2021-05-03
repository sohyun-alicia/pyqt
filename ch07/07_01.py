import pybithumb

# 가상화폐 일봉 데이터 얻기
df = pybithumb.get_ohlcv("BTC")
print(df.tail())
df.to_excel("btc.xlsx")