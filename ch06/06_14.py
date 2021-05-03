import datetime
import time

# dt = datetime.datetime(2018, 12, 1)
# now = datetime.datetime.now()
# mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

# print(now)
# print(mid)

while True:
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
    if now == mid :
        print("정각입니다.")
        # now = datetime.datetime.now()
        

    print(now, "vs", mid)
    time.sleep(1)