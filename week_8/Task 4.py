import pandas as pd
import numpy as np
from sklearn import datasets

pd.set_option('display.max_columns', None)

dataset = datasets.load_iris()
dataset1 = datasets.load_iris(as_frame=True)

ext_target = dataset.target[:, None]


maskSet = (data['target name'] == 'setosa')
maskVer = (data['target name'] == 'versicolor')
maskVir = (data['target name'] == 'virginica')

numberSet = maskSet.sum()
numberVer = maskVer.sum()
numberVir = maskVir.sum()


print(dataset1.data.describe())
#print(dataset1.data.keys())
#print(data.value_counts())

#nulls = data.isnull().sum().sort_values(ascending=False)
#data.drop_duplicates(inplace=True)
#print(data.duplicated().sum())

