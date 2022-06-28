temp_file = open("temp.txt", mode="w")
print("file print", file=temp_file)
print("I love you", file=temp_file)
temp_file.close()
temp_file = open("temp.txt", mode="r")
print(temp_file.read())
temp_file.close()

with open("temp.txt", mode="r+") as temp_file:
    print("I'm here for you", file=temp_file)
    for lines in temp_file:
        print(temp_file.read())
