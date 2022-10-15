def rearrange_element(lst):
    lst1 = []
    k = 0
    for i in range(len(lst)):
        lst1.append(len(lst) - k)
        k += 1
    return lst1


print(rearrange_element([1, 2, 3, 4, 5]))
