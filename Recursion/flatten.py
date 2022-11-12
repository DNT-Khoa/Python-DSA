'''
Flatten
Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

Examples

flatten([1, 2, 3, [4, 5]]) # [1, 2, 3, 4, 5]
flatten([1, [2, [3, 4], [[5]]]]) # [1, 2, 3, 4, 5]
flatten([[1], [2], [3]]) # [1, 2, 3]
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) # [1, 2, 3]
'''


def flatten(arr):
    my_arr = []

    for i in arr:
        if type(i) is list:
            my_arr.extend(flatten(i))
        else:
            my_arr.append(i)

    return my_arr


print(flatten([1, 2, 3, [4, 5]]))
