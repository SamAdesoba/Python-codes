characters = "Hello World"
print(characters[0], end=" ")
print()
print()
print(characters[3], end=" ")
print()
print()
print(characters[2:7], end=" ")
print()
print()
print(characters[:7], end=" ")
print()
print()
print(characters[2:], end=" ")
print()
print()
print(characters[:], end=" ")
print()
print()
print(characters[0:6]+characters[6:11], end=" ")
print()
print()
print(characters[0:11:2], end=" ")
print()
print()
print(characters[::-1], end=" ")
print()
print()
copy_string = characters[:]
print(characters[::-2], end=" ")
print()
print()
n = int(12321)
n_string = str(n)
print(n_string[:])
reverse_string = n_string[:]
print()
if n_string == reverse_string[::-1]:
    print("True")
else:
    print("False")
print()
print()
length = len(n_string)
print("length is ", length)
print()
print( type(n_string))
print()
print(ord(characters[5]))
#
# for i in range(1, 11):
#     print("*" * i)
