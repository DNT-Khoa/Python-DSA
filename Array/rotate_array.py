def rotate_array(nums, k):
    result = []
    size = len(nums)

    for i in range(size):
        prev_index = i - k if i - k >= 0 else i - k + size
        result.append(nums[prev_index])

    return result


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotate_array(nums, k))
