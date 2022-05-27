"""
Question: How to find the sum of digits of a positive integer number using recursion ?
    - 21 = 2*10 + 1
    - 234 = 2*100 + 3*10 + 4

    234 // 10 = 23.4  => 4 remainder, 23 result
    23 // 10 = 2.3 => 3 remainder, 2 result
    2 // 10 = 0 if result is 0 return n

"""


def sum_of_digits(n):
    # Edge case
    if n <= 0:
        return 0

    return (n % 10) + sum_of_digits(n // 10)


my_num = 12345
print(sum_of_digits(my_num))
