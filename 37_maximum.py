def get_max(nums):
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

values = [12, 45, 7, 89, 23]
print("Maximum value:", get_max(values))
