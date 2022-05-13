# Zip takes two or more iterable and then brings them together as a turple
a = [1,2,3,4,5]
b = [7,5,7,8,4,2,4]
print(list(zip(a, b)))
# print(list(zip(a, b, strict=True))) this will always through an error because the list are not of the same length
print(dict(zip(a, b)))

student_1 = [24, 45, 84]
student_2 = [13, 34, 80]
student_3 = [44, 40, 22]

subject_scores = [student for student in zip(student_1, student_2, student_3)]
max_subject_scores = max(student for student in zip(student_1, student_2, student_3))
print(subject_scores)
print(max_subject_scores)

s_slice = slice(1,3)

print("hello",[s_slice])