import random
import pandas as pd

random.seed(10)

list_metrics = []

for i in range(0,300):
  n = random.randint(-100,1000)
  list_metrics.append(n)

list_metrics = pd.DataFrame({'Прирост': list_metrics})

result1 = round(list_metrics.std()['Прирост'], 2)
result2 = round((list_metrics.max() - list_metrics.mean())['Прирост'], 2)
print(result1)
print(result2)
