"""
Question:
- Create a method which takes an array as a parameter and reverse it
- Find the runtime of the created method ?

Answer:
    Time complexity: O(n/2) = O(n)
"""


def reverse_str(my_str):
    size = len(my_str)
    for i in range(size // 2):
        my_str[i], my_str[size - i - 1] = my_str[size - i - 1], my_str[i]

    return ''.join(my_str)


my_str = "Khoa"
print(reverse_str(list(my_str)))
