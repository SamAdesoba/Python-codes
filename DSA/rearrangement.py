def rearrange(lst):
    lst1 = []
    lst2 = []
    # for i in lst:
    #     if i < 0:
    #         lst1.append(i)
    #     else:
    #         lst2.append(i)
    # return lst1 + lst2
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            lst1.append(lst[i])
        else:
            lst2.append(lst[i])
        i += 1
        print(lst1)
        print(lst2)
    return lst1 + lst2


# print(rearrange([11, -1, 20, 4, 5, -9, -6]))