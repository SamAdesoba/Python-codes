import collections


s = "Hello World"
s1 = "hi you"
c = collections.Counter(s)
c1 = collections.Counter(s1)
print(c)
print(c1)
print(c1.most_common())
print(c.most_common(2))
c.subtract(c1)
print(c)

Person = collections.namedtuple("Person", ["name", "age"])
p1 = Person(name="John", age=16)
print(p1.name)
