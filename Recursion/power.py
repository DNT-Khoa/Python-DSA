""""
How to calculate the power of a number using recursion ?
"""


def power(n, exp):
    if exp == 1:
        return n

    return n * power(n, exp - 1)


print(power(-2, 3))
