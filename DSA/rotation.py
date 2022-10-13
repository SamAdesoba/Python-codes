def rotate_clockwise(lst, k):
    if len(lst) == 0:
        return lst
    else:
        k = k % len(lst)
        return lst[len(lst) - k:] + lst[0:len(lst) - k]


def rotate_anticlockwise(lst, k):
    if len(lst) == 0:
        return lst
    else:
        k = k % len(lst)
        return lst[k:] + lst[:k]


print(rotate_clockwise([10, 20, 30, 40, 50], 3))
print(rotate_anticlockwise([10, 20, 30, 40, 50], 22))
