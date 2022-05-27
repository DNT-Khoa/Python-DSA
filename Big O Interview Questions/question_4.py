"""
What is the runtime of the following code
Answer:
    Time complexity: O(ab) (a, b are length of array a and b respectively)
"""


def print_unordered_pairs(seq_a, seq_b):
    for i in seq_a:
        for j in seq_b:
            if i < j:
                print(f'{i}, {j}')


seq_a = [1, 2, 8, 3, 5]
seq_b = [5, 3, 2, 7, 4]
print_unordered_pairs(seq_a, seq_b)
