class Lucas:
    def __init__(self, u0, u1, p, q, n):
        self.first = u0
        self.second = u0
        self.third = u1
        self.p = p
        self.q = q
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
            self.first = self.second
            self.second = self.third
            self.third = self.p * self.second - self.q * self.first
            self.counter += 1
            if self.counter > self.n:
                raise StopIteration
            return self.first


print(list(Lucas(0, 1, 1, 1, 10)))
