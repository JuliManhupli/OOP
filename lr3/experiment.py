import random
import os
import timeit


def fill_in_file():
    with open('file.txt', 'w') as f:
        while os.path.getsize('file.txt') <= 50 * 1024 * 1024:
            line = str(random.randint(1, 100)) + "\n"
            f.write(line)


def test_readlines():
    s = 0
    with open('file.txt', 'r') as f:
        for line in f.readlines():
            if line.strip().isdigit():
                s += int(line.strip())
    return s


def test_for_line():
    s = 0
    with open('file.txt', 'r') as f:
        for line in f:
            if line.strip().isdigit():
                s += int(line.strip())
    return s


def test_generator():
    with open('file.txt', 'r') as f:
        nums = (int(line.strip()) for line in f if line.strip().isdigit())
        s = sum(nums)
    return s


if __name__ == '__main__':
    fill_in_file()
    print(timeit.timeit(test_readlines, number=1))
    print(timeit.timeit(test_for_line, number=1))
    print(timeit.timeit(test_generator, number=1))
