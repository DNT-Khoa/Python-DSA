"""
Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
"""


def find_max_sum(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for i in range(len(arr)):
        window_sum += arr[i]

        if i - start + 1 == k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[start]
            start += 1

    return max_sum


print(find_max_sum([3, 5, 2, 1, 7], 2))
