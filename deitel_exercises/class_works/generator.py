# Generator is like a normal function but rather than return, it yields a value
# It is also used to iterate through a large

def gen():
    count = 0
    while True:
        yield count
        count += 1


lst = gen()

print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

# for i in gen():
#     print(i)


def count(low, high):
    while low <= high:
        yield low
        low += 1


def counter(low, high, step):
    while low <= high:
        yield low
        low += step


print(list(count(2, 6)))
print(list(counter(2, 6, 2)))

