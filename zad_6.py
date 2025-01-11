def handle_list(list1: list, list2: list) -> list:
    return list(set(list1 + list2))


tmp = handle_list([1, 2, 3, 4, 5], [1, 2, 5, 10, 11])
print(tmp)
