s1 = {1,2,3,4,7}
s2 = {5,2,45,4,5,}
s3 = s1 & s2
print(s3)
s4 = s1.intersection(s2)
print(s4)
s1 &= s2
print(s1)

s5 = s1 | s2
print(s5)
s1 |= s2
print(s1)
print()
print(s1.isdisjoint(s2))
s6 = s1.difference(s2)
s7 = s2.difference(s1)
print(s6)
print()
print(s7)
print(s1 ^ s2)