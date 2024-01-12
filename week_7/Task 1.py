import numpy as np

array = np.arange(10) ** 4
array_2 = np.arange(10) ** 3

array_sum = np.sum(np.add(array, array_2))
array_difference = np.sum(np.subtract(array, array_2))
game_payments2 = array[2]
subscription_last = array_2[-1]


print(array_sum)