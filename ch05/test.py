import pybithumb
import time

def bringBTCprice():
        while True:
            price = pybithumb.get_current_price("BTC")
            print(price)
            time.sleep(10)

bringBTCprice()