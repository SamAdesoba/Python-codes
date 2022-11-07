# print("Answer")
# while True:
#     pass
# print("45")
from pythonProject.deitel_exercises.class_works.tuples_and_dictionary import values


def func(x=3, y=4, z=6):
    return x + y + z


values = {"x": 9, "z": -1}
print(func(**values))


