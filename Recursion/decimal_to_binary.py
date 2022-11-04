'''
How to convert a number from Decimal to Binary
'''


def decToBin(n):
    assert int(n) == n, "Integer numbers expected!"

    if (n == 0):
        return 0
    return (n % 2) + (10 * decToBin(n // 2))


num = 13
print(decToBin(num))
