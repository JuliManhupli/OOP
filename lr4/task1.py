from Rational import *

if __name__ == "__main__":
    e1 = Rational(2, 4)
    e2 = Rational(30, 90)
    e3 = e1 + e2
    print(f"{e1} + {e2} = {e3}")
    e3 = e1 + 2
    print(f"{e1} + 2 = {e3}")
    e2 += e1
    print(f"{e1} + 1/3 = {e2}")
    e1 += 3
    print(f"3 + 1/2 = {e1}\n")

    e3 = e1 - e2
    print(f"{e1} - {e2} = {e3}")
    e3 = e1 - 2
    print(f"{e1} - 2 = {e3}")
    e2 -= e1
    print(f"5/6 - {e1} = {e2}")
    e1 -= 1
    print(f"7/2 - 1 = {e1}\n")

    e3 = e1 * e2
    print(f"{e1} * {e2} = {e3}")
    e3 = e1 * 2
    print(f"{e1} * 2 = {e3}")
    e2 *= e1
    print(f"-8/3 * {e1} = {e2}")
    e2 *= -2
    print(f"-20/3 * -2 = {e2}\n")

    e3 = e1 / e2
    print(f"{e1} / {e2} = {e3}")
    e3 = e1 / 2
    print(f"{e1} / 2 = {e3}")
    e2 /= e1
    print(f"40/3 / {e1} = {e2}")
    e2 /= 2
    print(f"16/3 / 2 = {e2}\n")

    print(f"{e2} = {e1} - {e2 == e1}")
    e3 = Rational(4)
    print(f"{e3} = 4 - {e3 == 4}")
    print(f"{e2} != {e1} - {e2 != e1}")
    print(f"{e3} != 4 - {e3 != 4}\n")

    print(f"{e1} < {e2} - {e1 < e2}")
    print(f"{e2} < 1 - {e2 < 1}")
    print(f"{e1} > {e2} - {e1 > e2}")
    print(f"{e2} > 1 - {e2 > 1}\n")

    e3 = Rational(5, 2)
    print(f"{e1} <= {e3} - {e1 <= e3}")
    print(f"{e1} >= {e3} - {e1 >= e3}")
    e3 = Rational(15, 15)
    print(f"{e3} <= 1 - {e3 <= 1}")
    print(f"{e3} >= 1 - {e3 >= 1}")
