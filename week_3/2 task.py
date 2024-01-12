def last_discharge(a):
    Numeral = a.split('.')
    if(len(Numeral) == 2):
        N = 10 ** int(len(Numeral[1]))
        b = float(a)
        exit = b - 1 / N
    else:
        exit = int(a) - 1

    return exit

a = input()
print(last_discharge(a))