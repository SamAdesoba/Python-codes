s = "abcadeccdccd"
# itr = iter(s)
# S_array = []
# for char in s:
#     S_array.append(next(itr))

# count = 0
# i = 0
# while i < len(s):
#     for char in s:
#         if char[i] != char[i + 1]:
#             count += 1
#     i += 1
#
# print(count)


def twin_element(lst):
    for i in range(0, len(lst) - 1, 2):
        if lst[i] != lst[i + 1]:
            return lst[i]
        elif lst[-1] != lst[-2]:
            return lst[-1]
    return -1


print(twin_element([1, 1, 3, 3, 4, 4]))
