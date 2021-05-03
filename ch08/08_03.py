import pyupbit

# 시가(open), 고가(high), 저가(low), 종가(close), 거래량(volume) >> OHLCV
df = pyupbit.get_ohlcv("KRW-BTC", interval = "minute")
print(df)