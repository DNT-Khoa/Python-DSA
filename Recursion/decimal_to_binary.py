"""
    How to convert a number from Decimal to Binary using recursion
"""


def dec_to_bin(n):
    if n == 0:
        return ""

    return str(dec_to_bin(n // 2)) + str(n % 2)


# Using loop
# def dec_to_bin(n):
#     bin_str = ""
#     while n:
#         bin_str = str(n % 2) + bin_str
#         n //= 2
#
#     return bin_str


print(dec_to_bin(112))
