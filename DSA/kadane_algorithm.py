def max_sub_list(lst):
    global_max = lst[0]
    current_max = lst[0]
    for i in range(1, len(lst)):
        if current_max < 0:
            current_max = lst[i]
        else:
            current_max += lst[i]
        if current_max > global_max:
            global_max = current_max
    return global_max


print(max_sub_list([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
