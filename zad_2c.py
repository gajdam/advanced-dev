def print_evens(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            print(nums[i])


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_evens(nums)
