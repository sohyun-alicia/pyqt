import pybithumb

df = pybithumb.get_ohlcv("BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]          # 끝에서 두 번재 위치한 전일 이동평균을 last_ma5 변수에 바인딩

price = pybithumb.get_current_price("BTC")

if price > last_ma5:
    print("상승장")
else:
    print("하락장")