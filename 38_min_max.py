def get_max_min(nums):
    maximum = nums[0]
    minimum = nums[0]

    for n in nums:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n

    return maximum, minimum


values = [12, 45, 7, 89, 23]
mx, mn = get_max_min(values)

print("Maximum:", mx)
print("Minimum:", mn)
