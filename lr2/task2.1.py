import math


class Rational:
    """
    Class Rational
    Takes 2 parameters: the numerator and the denominator of the fraction
    Has 2 methods that return the form of a fraction and the form of a number
    """

    def __init__(self, num=1, den=1):
        if not isinstance(num, int):
            raise TypeError("Incorrect numerator type")
        if not isinstance(den, int):
            raise TypeError("Incorrect denominator type")
        if not den:
            raise ZeroDivisionError("Division on zero!")

        gcd = math.gcd(num, den)
        self.__num = num // gcd
        self.__den = den // gcd

    def print_float(self):
        return self.__num/self.__den

    def print_fraction(self):
        return f"{self.__num}/{self.__den}"


if __name__ == "__main__":
    example = Rational(4, 5)
    print(example.print_fraction())
    print(example.print_float())