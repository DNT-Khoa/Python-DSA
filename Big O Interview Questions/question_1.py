"""
Time complexity of a method that returns Sum and Product of an array

Answer:
    Time complexity = O(n)
"""


def spof_array(seq):
    sum = 0
    product = 1

    for i in seq:
        sum += i

    for j in seq:
        product *= j

    return sum, product


my_array = [1, 3, 4, 5]
print(spof_array(my_array))
