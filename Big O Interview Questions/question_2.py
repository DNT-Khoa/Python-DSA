"""
Time complexity of print pairs methods
Question:
    - Create a function which prints to the console the pairs from given array
    - Find the time complexity for created method
"""


def print_pairs(seq):
    for i in seq:
        for j in seq:
            print(f'{i}{j}', end=" ")

        print("")


my_arr = [1, 3, 4, 5]
print_pairs(my_arr)
