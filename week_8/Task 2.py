import pandas as pd

data = pd.read_csv("police.csv", sep=',')
nulls = data.isnull().sum().sort_values(ascending=False)
name = nulls.keys()[0]
print(nulls)


#del_arr =
