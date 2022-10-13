b = [1, 4, 2, 10, 2, 3, 1, 0, 20]


# Two pointers
def max_sub_array_two_pointer(lst, k):
    window = lst[0:k]
    maximum = sum(lst[0:k])
    total = sum(lst[0:k])
    start = 0
    end = k
    lst1 = []
    print(window)
    while end < len(lst):
        total = total - lst[start] + lst[end]
        if total > maximum:
            maximum = total
        start += 1
        end += 1
        lst1 = lst[start:end]
        print(lst1)
    return maximum


# print(max_sub_array_two_pointer(b, 4))

a = [1, 4, 2, 10, 2, 3, 1, 0, 20]


def max_sub_array(lst, k):
    window = lst[0:k]
    maximum = sum(lst[0:k])
    total = sum(lst[0:k])
    lst1 = []
    for i in range(len(lst) - k):
        total = total - lst[i] + lst[i + k]
        if total > maximum:
            maximum = total
        lst1 = lst[i: i+k]
        print(lst1)
    print(lst[k+1:])
    return maximum


print(max_sub_array(a, 4))
