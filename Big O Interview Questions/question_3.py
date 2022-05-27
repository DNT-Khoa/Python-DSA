"""
What is the time complexity for this method ?
Answer:
    - Time complexity: n^2 / 2 = O(n^2)
"""


def print_unordered_pairs(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            print(f'{seq[i]}{seq[j]}', end=" ")

        print("")


my_arr = [1, 3, 4, 5]
print_unordered_pairs(my_arr)
