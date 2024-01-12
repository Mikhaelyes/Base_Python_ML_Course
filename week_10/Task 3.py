import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import scipy.stats as sps
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('winequality-red.csv', sep=';')

Y = data['quality']
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']]

preprocessing.scale(Y)
preprocessing.scale(X)

regr = LinearRegression()
regr.fit(X, Y)
diabetes_y_pred = regr.predict(X)

print(f"Coefficients: \n{regr.coef_}")
print(f"Intercept: {regr.intercept_}")

print(regr.coef_.sum() + regr.intercept_)
