
from functools import reduce


def add(x, y):
    return x + y

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(add, values)
print(result)