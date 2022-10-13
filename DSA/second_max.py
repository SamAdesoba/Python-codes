def second_max(lst):
    max = float('-inf')
    second = float('-inf')
    for i in lst:
        if i > max:
            second = max
            max = i
        elif second < i < max:
            second = i
    return second


print(second_max([8, 2, 3, 9, 10]))
