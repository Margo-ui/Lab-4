import math


def gcd(a, b):
    return math.gcd(a, b)


class Rational:

    def __init__(self, x=1, y=1):
        self.num = x
        self.denom = y
        if not y:
            self.denom = 1

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def get_denom(self):
        return self.denom

    def set_denom(self, denom):
        self.denom = denom

    def reduce(self):
        a = gcd(int(self.num), int(self.denom))
        self.num = self.num / a
        self.denom = self.denom / a

    def __add__(self, other):
        k = Rational()
        k.num = self.num * other.denom + other.num * self.denom
        k.denom = self.denom * other.denom
        k.reduce()
        return k

    def __iadd__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        k = Rational()
        k = self + other
        k.reduce()
        return k

    def __isub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        k = Rational()
        k = self - other
        k.reduce()
        return k

    def __sub__(self, other):
        k = Rational()
        k.num = self.num * other.denom - other.num * self.denom
        k.denom = self.denom * other.denom
        k.reduce()
        return k

    def __imul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        k = Rational()
        k = self * other
        k.reduce()
        return k

    def __mul__(self, other):
        k = Rational()
        k.num = self.num * other.num
        k.denom = self.denom * other.denom
        k.reduce()
        return k

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        k = Rational()
        k.num = self.num * other.denom
        k.denom = self.denom * other.num
        k.reduce()
        return k

    def __idiv__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        k = Rational()
        k = self/other
        return k

    def __cmp__(self, other):
        k = self.num * other.denom
        m = self.denom * other.num
        if k > m:
            return 1
        if k < m:
            return -1
        return 0

    def fraction(self):
        self.x = str(self.num)
        self.y = str(self.denom)
        return self.x + "/" + self.y

    def decimal(self, place):
        self.no = float(self.num / self.denom)
        self.str = str(self.no)
        return self.str


r1 = Rational(3, 7)
r2 = Rational(4, 10)
r3 = Rational(5, 11)
r2 += r3
print(r2.fraction())
r2 -= r1
print(r2.fraction())
r2 /= r3
print(r2.fraction())
r2 *= r1
print(r2.fraction())
print(r2 == r3)
