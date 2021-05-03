import pandas as pd

url = "https://finance.naver.com/world/"
df = pd.read_html(url)      # read_html : 웹페이지를 DataFrame으로 변환
print(df[0])