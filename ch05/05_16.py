import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

window = close.rolling(5)   # rolling(5) : 5일 윈도우를 설정. 5일씩 모든 데이터를 그룹화
ma5 = window.mean()
print(ma5)