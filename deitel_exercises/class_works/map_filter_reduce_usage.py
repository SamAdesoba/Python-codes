from functools import reduce
# Map does the same work as a list comprehension
map_object = map(lambda x: x**2 if x%2==0 else x, range(1, 10))
print(list(map_object))
lst1 = list(map_object)
lst2 = list(map_object)
print("1", lst1)
print("2", lst2)

# Usage of filter
def isEven(x):
    return x % 2 == 0


filter_object = list(filter(isEven, range(1,10)))

print(filter_object)

# Usage of reduce
# reduce also does the work of sum amd multiplication
def add(x, y):
    return x + y

def operartor(x, fn):
    return fn(x)



print(reduce(add, range(1,11)))

print(reduce(lambda x, y: x+y, range(1, 11)))

print(reduce(lambda x, y: x*y, range(1, 11)))

names = ["Amaka", "Segun", "comb", "Samson", "foil"]
longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
print(longest_name)
shortest_name = reduce(lambda x, y: x if len(x) < len(y) else y, names)
print(shortest_name)

print(max(names, key=len))

print(sorted(names, key=len,))

print(sorted(names, key=len, reverse=True))

print(sorted(names, key=lambda x: x[-1]))


