class Luhn:
    def __init__(self, n):
        self.n = [int(n) for n in str(n)]

    def addends(self):
        return [Luhn.dubly(i, x) for (i, x) in enumerate(self.n[::-1])]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def dubly(i,x):
        y = x if i % 2 == 0 else 2 * x
        return y if y <= 9 else y-9

    @staticmethod
    def create(n):
        luhn = Luhn(n)
        for check in range(9):
            luhn.n.append(check)
            if luhn.is_valid():
                return int(''.join([str(i) for i in luhn.n]))
            else:
                luhn.n.pop()
