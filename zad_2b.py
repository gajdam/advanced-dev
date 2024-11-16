def multiple_list(nums):
    multiply_nums = []

    for num in nums:
        multiply_nums.append(num * 2)

    return multiply_nums

def multiple_fold_list(nums):
    return [num * 2 for num in nums]

nums = [1, 2, 3, 4, 5]

print(multiple_list(nums))
print(multiple_fold_list(nums))

