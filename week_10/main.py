import pandas as pd
import numpy as np

data = pd.read_csv('california_housing.csv')

X = data["MedInc"].to_frame()
Y = data["MedHouseVal"].to_frame()

X.insert(0, 'w0', [1] * X   .shape[0])

w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

#print(w)
SS_tot = (((Y - Y.mean())**2).sum().to_list())[0]
#SS_res = ((Y["MedInc"] - X.dot(w)[0])**2).sum()
SS_res = ((Y["MedHouseVal"] - X.dot(w)[0])**2).sum()

ESS = SS_tot - SS_res
R = 1 - SS_res / SS_tot

#print(ESS)
#print(SS_tot)
#print(R)
print(X.describe())
