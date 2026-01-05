def get_total(nums):
    total = 0
    for n in nums:
        total += n
    return total

marks = [80, 85, 90]
print("Total marks:", get_total(marks))
