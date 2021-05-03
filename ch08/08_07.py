import pyupbit

access_key = "rudr1srMrxFdcMtV578ug17GCOwvgOf1iLZQxgpj"
secret_key = "vVmpSDxNnwGn1k2O7PDLIc9qDdP9Fom2j38M6Iew"

upbit = pyupbit.Upbit(access_key, secret_key)
ret = upbit.buy_limit_order("KRW-XRP", 100, 20)
print(ret)