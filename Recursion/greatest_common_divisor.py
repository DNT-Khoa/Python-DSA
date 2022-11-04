'''
How to find GCD (Greatest Common Divisor) of two numbers using recursion?
'''


def gcd(a, b):
    assert int(a) == a and int(b) == b, "Integer numbers are expected!"
    if a < 0:
        a = -a

    if b < 0:
        b = -b

    if b == 0:
        return a

    return gcd(b, a % b)


a = -12
b = -6

print(gcd(a, b))
