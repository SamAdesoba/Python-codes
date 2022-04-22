
def function(y):
    y = 4
    return y
x = 5
print(function(5))

def add(a:  int, b: str)-> tuple[int, str]:
    return a,b

print(add(3, "5"))
print(add(3))
print(add())
# print(add("add", 3)) this is wrong

def mutatable_ish(a = None):
    if a is None:
        a = []
        a.append("python")
    return a

print(mutatable_ish())
print(mutatable_ish())

def add_list(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

lst = [2,3,2,1,6]
a = (2,3,5,7,3)
print(add_list(*a))
print(add_list(*lst))

def dict_pack_unpack(**kwargs):
    print(kwargs)

dict_pack_unpack(name = "Shola", age = 45, sex = "Male")

def dict_pack_unpack(*args,**kwargs):
    print("Kwargs", kwargs)
    print("Args", args)

dict_pack_unpack( 4, 6, "goal", name = "Shola", age = 45, sex = "Male")

def sub(a,b,/,c):
    print(a,b,c)

print(sub(2,3,c=4))