"""
What is the runtime of the below code
Answer: O(logN)
"""


def power_of_2(n):
    if n < 1:
        return 0

    if n == 1:
        return 1

    prev = power_of_2(n // 2)
    curr = prev * 2
    print(curr)
    return curr


power_of_2(8)
