

s = "Hello"
itr = iter(s)
print(next(itr), end="")
print(next(itr), end="")
print(next(itr), end="")
print(next(itr), end="")
print(next(itr))


def custom_for(iterable, func):
    it = iter(iterable)

    while True:
        try:
            func(next(it))
        except StopIteration:
            break


def cube(num):
    return print(num**2)


names = "ADEFOLARIN"
custom_for(names, print)
number = [1,2,3,4,5]
custom_for(number, cube)
