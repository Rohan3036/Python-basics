def get_average(nums):
    total=0
    for n in nums:
        total += n
    return total / len(nums)

marks = [80, 85, 90]
print("Average:", get_average(marks))
