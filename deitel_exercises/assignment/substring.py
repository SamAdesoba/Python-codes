from deitel_exercises.class_works.generator import counter

s = "abcadeccdccd"
# itr = iter(s)
# S_array = []
# for char in s:
#     S_array.append(next(itr))

count = 0
i = 0
while i < len(s):
    for char in s:
        if char[i] != char[i + 1]:
            count += 1
    i += 1

print(count)
