class Multiplex:
    def __init__(self, num):
        self.num = num

    def plus(self):
        self.num += '+'
        return self.num

five = Multiplex(str(5))
print(five.plus)