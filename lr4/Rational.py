import math


class Rational:

    def __init__(self, num=1, den=1):
        self.num, self.den = Rational.gcd(num, den)

    @staticmethod
    def gcd(num, den):
        gcd = math.gcd(num, den)
        num = num // gcd
        den = den // gcd
        return num, den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if not isinstance(num, int):
            raise ValueError("Incorrect numerator type")
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        if not isinstance(den, int):
            raise TypeError("Incorrect denominator type")
        if not den:
            raise ZeroDivisionError("Division on zero!")
        self.__den = den

    def __add__(self, other):
        if isinstance(other, int):
            num = self.num + other * self.den
            return Rational(num, self.den)
        elif isinstance(other, Rational):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den
            return Rational(num, den)
        else:
            raise NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            num = self.num + other * self.den
            self.num, self.den = Rational.gcd(num, self.den)
            return self
        elif isinstance(other, Rational):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den
            self.num, self.den = Rational.gcd(num, den)
            return self
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            num = self.num - other * self.den
            return Rational(num, self.den)
        elif isinstance(other, Rational):
            num = self.num * other.den - other.num * self.den
            den = self.den * other.den
            return Rational(num, den)
        else:
            raise NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            num = self.num - other * self.den
            self.num, self.den = Rational.gcd(num, self.den)
            return self
        elif isinstance(other, Rational):
            num = self.num * other.den - other.num * self.den
            den = self.den * other.den
            self.num, self.den = Rational.gcd(num, den)
            return self
        else:
            raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.num * other, self.den)
        elif isinstance(other, Rational):
            num = self.num * other.num
            den = self.den * other.den
            return Rational(num, den)
        else:
            raise NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.num, self.den = Rational.gcd(self.num * other, self.den)
            return self
        elif isinstance(other, Rational):
            num = self.num * other.num
            den = self.den * other.den
            self.num, self.den = Rational.gcd(num, den)
            return self
        else:
            raise NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.num, self.den * other)
        elif isinstance(other, Rational):
            num = self.num * other.den
            den = self.den * other.num
            return Rational(num, den)
        else:
            raise NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, int):
            self.num, self.den = Rational.gcd(self.num, self.den * other)
            return self
        elif isinstance(other, Rational):
            num = self.num * other.den
            den = self.den * other.num
            self.num, self.den = Rational.gcd(num, den)
            return self
        else:
            raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, int):
            return self.num == other
        elif isinstance(other, Rational):
            return self.num == other.num and self.den == other.den
        else:
            raise NotImplemented

    def __ne__(self, other):
        if isinstance(other, int):
            return self.num != other
        elif isinstance(other, Rational):
            return self.num != other.num or self.den != other.den
        else:
            raise NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.num < other * self.den
        elif isinstance(other, Rational):
            if self.den == other.den:
                return self.num < other.num
            else:
                lcm = math.lcm(self.den, other.den)
                num1 = self.num * lcm / self.den
                num2 = other.num * lcm / other.den
                return num1 < num2
        else:
            raise NotImplemented

    def __le__(self, other):
        if isinstance(other, int):
            return self.num <= other * self.den
        elif isinstance(other, Rational):
            if self.den == other.den:
                return self.num <= other.num
            else:
                lcm = math.lcm(self.den, other.den)
                num1 = self.num * lcm / self.den
                num2 = other.num * lcm / other.den
                return num1 <= num2
        else:
            raise NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.num > other * self.den
        elif isinstance(other, Rational):
            if self.den == other.den:
                return self.num > other.num
            else:
                lcm = math.lcm(self.den, other.den)
                num1 = self.num * lcm / self.den
                num2 = other.num * lcm / other.den
                return num1 > num2
        else:
            raise NotImplemented

    def __ge__(self, other):
        if isinstance(other, int):
            return self.num >= other * self.den
        elif isinstance(other, Rational):
            if self.den == other.den:
                return self.num >= other.num
            else:
                lcm = math.lcm(self.den, other.den)
                num1 = self.num * lcm / self.den
                num2 = other.num * lcm / other.den
                return num1 >= num2
        else:
            raise NotImplemented

    def print_float(self):
        return round(self.__num/self.__den, 2)

    def __str__(self):
        if self.__den == 1:
            return f"{self.__num}"
        else:
            return f"{self.__num}/{self.__den}"
