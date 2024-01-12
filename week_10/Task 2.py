import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import scipy.stats as sps

data = pd.read_csv('income.data.csv')
lin_model = sps.linregress(data['income'], data['happiness'])
a, b = lin_model.slope, lin_model.intercept

n = data.shape[0]

# оценка ср.кв. ошибки для a и b
a_err, b_err = lin_model.stderr, lin_model.intercept_stderr
# Доверительный интервал для alpha=5%
a_conf = sps.t.interval(0.95, df = n-2, loc=a, scale=a_err)
b_conf = sps.t.interval(0.95, df = n-2, loc=b, scale=b_err)

print(f"a = {a:0.4f}, α=5% [{a_conf[0]:0.4f} - {a_conf[1]:0.4f}]")
print(f"b = {b:0.4f}, α=5% [{b_conf[0]:0.4f} - {b_conf[1]:0.4f}]")

