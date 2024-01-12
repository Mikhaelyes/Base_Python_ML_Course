Name = input()

F = open(Name, "r")
s = F.read().split()

File = list(s)
Words = list(set(File))
Final = [[0] * 2 for i in range(len(Words))]

print(File)
print(Words)

Counter = [0] * len(Words)
k = 0

for i in Words:
    for j in File:
        if i == j:
            Counter[k] += 1
    k += 1

for i in range(0, len(Words)):
    Final[i][0] = Counter[i]
    Final[i][1] = Words[i]

Final.sort(key = lambda x: x[1])
Final.sort(reverse=True, key = lambda x: x[0])

for i in range(0, len(Words)):
    print(Final[i][0], Final[i][1])

F.close()