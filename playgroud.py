def check_array(nums):
    pivot_index = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= pivot_index:
            pivot_index = i

    return pivot_index == 0


my_array_1 = [2, 3, 1, 1, 4]
my_array_2 = [3, 2, 1, 0, 4]
print(check_array(my_array_1))
print(check_array(my_array_2))
