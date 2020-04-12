from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


for i in fact(15):
    print(i)
