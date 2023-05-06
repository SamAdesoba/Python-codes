b = [1, 4, 2, 10, 2, 3, 1, 0, 20]


# Two pointers
# def max_sub_array_two_pointer(lst, k):
#     window = lst[0:k]
#     maximum = sum(lst[0:k])
#     total = sum(lst[0:k])
#     start = 0
#     end = k
#     lst1 = []
#     print(window)
#     while end < len(lst):
#         total = total - lst[start] + lst[end]
#         if total > maximum:
#             maximum = total
#         start += 1
#         end += 1
#         lst1 = lst[start:end]
#         print(lst1)
#     return maximum


# print(max_sub_array_two_pointer(b, 4))

a = [1, 4, 2, 10, 2, 3, 1, 0, 20]


# def max_sub_array(lst, k):
#     window = lst[0:k]
#     maximum = sum(lst[0:k])
#     total = sum(lst[0:k])
#     lst1 = []
#     for i in range(len(lst) - k):
#         total = total - lst[i] + lst[i + k]
#         if total > maximum:
#             maximum = total
#         lst1 = lst[i: i + k]
#         print(lst1)
#     print(lst[k + 1:])
#     return maximum


# print(max_sub_array(a, 4))


# def rearrange_array(lst):
#     lst1 = []
#     start = 0
#     end = len(lst) - 1
#     while start <= end:
#         lst1.append(lst[end])
#         lst1.append(lst[start])
#         start += 1
#         end -= 1
#     if len(lst) != len(lst1):
#         lst1.pop(-1)
#     return lst1

# def tab_move(lst, k):
#     lst1 = []
#     start = 0
#     num = lst[k-1]
#     lst1.append(num)
#     lst.remove(num)
#     end = len(lst)
#     while start < end:
#         lst1.append(lst[start])
#         start += 1
#     return lst1
#
#
# print(tab_move([1, 2, 3, 4, 5], 4))

# arr = [1, 3, 4, 2, 6]
arr = [2, 3, 4, 5, 6]
lst = []
#
i = 0
while i < len(arr):
    acount = 0
    bcount = 0
    num = arr[i]
    for j in range(len(arr)):
        if num % arr[j] == 0:
            acount += 1
        elif arr[j] % num == 0:
            bcount += 1
    lst.append(acount + bcount - 1)
    i += 1
print(lst)


# def getlst():
#     lst = []
#     a = [1, 3, 4, 2, 6]
#     for count in range(len(a)):
#         c = sum([i % a[count] == 0 for i in a]) - 1
#         b = sum([a[count] % i == 0 for i in a]) - 1
#         lst.append(c+b)
#     return lst
#
# print(getlst())


