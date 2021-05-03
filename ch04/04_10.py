from pandas import Series           # pandas 내의 Series 모듈 import

# Series의 생성자로 date와 xrp_close를 넘겨줌
# 각 날짜를 문자열로 표현하고 이를 리스트 객체로 만듬
date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']  
xrp_close = [512, 508, 512, 507, 500]       # 리플 종가를 리스트화
s = Series(xrp_close, index=date)           # 리플 종가로 Series 객체 생성. 인덱스 값으로 날짜 지정

print(s)
