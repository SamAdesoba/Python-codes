
def rotate(lst = [1, 2, 3, 4, 5], a = 2) -> list:
    rang = (1, a)
    for i in rang:
        last = lst.pop()
        lst.insert(0, last)
    return lst


print(rotate())

def rotate(lst, k):
    r = k % len(lst)
    return lst[-2:]+ lst[:-2]
print(rotate([1,2,3,4,5,6], 6))



