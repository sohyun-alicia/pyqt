import pybithumb


# 가상화폐별 상승/하락 문구 출력
def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    price = pybithumb.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False

# tickers = pybithumb.get_tickers()
# for ticker in tickers:
#     is_bull = bull_market(ticker)
#     if is_bull:
#         print(ticker, " 상승장")
#     else:
#         print(ticker, " 하락장")


# def bringcurrentprice(ticker):
#     df = pybithumb.get_ohlcv(ticker)
#     ma5 = df['close'].rolling(window=5).mean()
#     price = pybithumb.get_current_price(ticker)
#     last_ma5 = ma5[-2]

#     return price
#     # if price > last_ma5:
#     #     return True
#     # else:
#     #     return False

# tickers = pybithumb.get_tickers()
# for ticker in tickers:
#     print(bringcurrentprice(ticker))


# 비트코인 현재 시세
def bringcurrentprice(a):
    df = pybithumb.get_ohlcv(a)
    ma5 = df['close'].rolling(window=5).mean()
    price = pybithumb.get_current_price(a)
    last_ma5 = ma5[-2]

    return price
    # if price > last_ma5:
    #     return True
    # else:
    #     return False


print(bringcurrentprice("BTC"))


