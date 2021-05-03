import pybithumb

# 목표가 계산하기
# DataFrame 객체에 목표가 컬럼을 추가하는 코드
df = pybithumb.get_ohlcv("BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel("btc.xlsx")