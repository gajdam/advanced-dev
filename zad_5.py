def is_number_in_list(numbers: list, num: int) -> bool:
    return num in numbers

print(is_number_in_list([1, 2, 3], 3))
print(is_number_in_list([1, 2, 3], 4))