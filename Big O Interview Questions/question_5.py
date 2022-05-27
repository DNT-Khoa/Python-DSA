"""
What is the time complexity of the following method
Answer:
    Time complexity: O(ab) (with a, b are length of array a and b respectively)
"""


def print_unordered_pairs(seq_a, seq_b):
    for i in seq_a:
        for j in seq_b:
            for k in range(10000000):
                print(f'{i}, {j}')
