"""
Question:
    Given an array containing N integers, and a number S denoting a target sum.
    Find two distinct integers that can pair up to form target sum. Let us assume there will
    be only one such pair

    Input
    array = [10, 5, 2, 3, -6, 9, 11]
    S = 4
    Output [10, -6]


"""


def find_pair(arr, S):  # Time complexity: O(n)
    st = set()

    for num in arr:
        if S - num not in st:
            st.add(num)
        else:
            return [num, S - num]


array = [10, 5, 2, 3, -6, 9, 11]
S = 4

print(find_pair(array, S))
