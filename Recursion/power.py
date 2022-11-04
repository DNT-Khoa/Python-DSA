'''
How to calculate power of a number using recursion?
'''


def power(base, exp):
    assert int(exp) == exp, "Pow is expected to be integer"

    if exp == 0:
        return 1

    if exp < 0:
        return (1/base) * power(base, exp + 1)

    return base * power(base, exp - 1)


base = 4
exp = 2

print(power(base, exp))
