def fibonacci(index):
    N = int(index)
    Current = 0
    if (N >= 3):
        F = [0, 1]
        for i in range(3, N + 1):
            Current = F[0] + F[1]
            F[0] = F[1]
            F[1] = Current

    elif (N == 2):
        Current = 1

    return Current


index = input()
print(fibonacci(index))