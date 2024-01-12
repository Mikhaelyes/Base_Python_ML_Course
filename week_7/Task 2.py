import numpy as np

some_data =  [
    [3, 8, 1, 0, 1, 2],
    [9, 2, 7, 3, 0, 4],
    [2, 5, 1, 3, 1, 8],
    [5, 1, 2, 1, 1, 0]
]
S = np.array(some_data)
lines = S[1:3]
last_column = S[:, -1]
array_t = np.transpose(S)
array_sum = np.sum(S)
array_avg = np.mean(S)

