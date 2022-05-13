add = lambda x, y: x + y
print(add.__name__)
def add(x, y):
    return x + y


def sub(x, y):
    return y - x


def mul(x, y):
    return y * x


def operator(x, y, func):
    return func(x, y)


val_add = operator(5, 24, add)
val_sub = operator(5, 24, sub)
val_mul = operator(5, 24, mul)

print(val_sub)
print(val_add)
print(val_mul)
print(operator(5, 25, lambda x, y: y / x))
print(operator(5, 25, lambda x, y: y + x))
print(operator(5, 25, lambda x, y: y - x))


def multiple(x, fn):
    return fn(x)


print(multiple(5, lambda x: (2 * x)))
print(multiple(5, lambda x: (3 * x)))
