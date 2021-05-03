from pandas import DataFrame


# Pandas DataFrame
data = {'open': [100, 200], "high" : [110, 210]}
df  = DataFrame(data)
print(df)

'''
open  high
0   100   110
1   200   210
'''