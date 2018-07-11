class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        gcd_value = gcd(new_num, new_den)
        return Fraction(new_num//gcd_value, new_den//gcd_value)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        gcd_value = gcd(new_num, new_den)
        return Fraction(new_num//gcd_value, new_den//gcd_value)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        gcd_value = gcd(new_num, new_den)
        return Fraction(new_num//gcd_value, new_den//gcd_value)

    def __truediv__(self, other):
        # new_num = self.num * other.den
        # new_den = self.den * other.num
        #
        # gcd_value = gcd(new_num, new_den)
        # return Fraction(new_num//gcd_value, new_den//gcd_value)
        new_frac = Fraction(other.den, other.num)
        return self.__mul__(new_frac)

    def __eq__(self, other):
        new_num = self.num * other.den
        new_other_num = other.num * self.den
        return new_num == new_other_num

    def __gt__(self, other):
        new_num = self.num * other.den
        new_other_num = other.num * self.den
        return new_num > new_other_num

    def __lt__(self, other):
        new_num = self.num * other.den
        new_other_num = other.num * self.den
        return new_num < new_other_num


def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

x = Fraction(2, 3)
y = Fraction(1, 6)
z = Fraction(2, 12)

print(x + y)
print(x == y)
print(y == z)

print(x - y)
print(y - x)

print(x * y)
print(x / y)

print(x > y)
print(x < y)
print(x == y)

