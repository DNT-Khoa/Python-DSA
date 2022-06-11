"""
Question: Given an array of size 'n', calculate the maximum sum of k consecutive elements in the array
"""


# Time complexity: O(n)
# Space complexity: O(1)

def find_max_sum(nums, k):
    max_sum = window_size = 0
    ptr_1 = 0

    for ptr_2 in range(len(nums)):
        window_size += nums[ptr_2]

        if ptr_2 - ptr_1 + 1 == k:
            max_sum = max(max_sum, window_size)
            window_size -= nums[ptr_1]
            ptr_1 += 1

    return max_sum


arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
print(find_max_sum(arr, 4))
