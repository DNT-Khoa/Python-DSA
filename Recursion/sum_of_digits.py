'''
How to find the sum of digits of a positive integer number using recursion?

23456 = 23456 // 10 = 2345 and 23456 % 10 = 6

recursive case: sum(n) = n % 10 + sum(n // 10)

base case: n // 10 = 0 return n

edge case: n < 0

'''


def sumOfDigits(num):
    assert num >= 0, "Positive integer expected"

    if num // 10 == 0:
        return num

    return num % 10 + sumOfDigits(num // 10)


num = 12345


print(sumOfDigits(num))
