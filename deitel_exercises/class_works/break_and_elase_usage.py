num = 1
while num < 11:
    print(num)
    num += 1
else:
    print("All went well")
print()
print()
num = 1
while num < 11:
    if num == 5:
        print("All did not go well")
        break
    print(num)
    num += 1
else:
    print("All went well")
print()
print()
num = 1
while num < 11:
    if num == 5:
        print("All did not go well")
        break
    elif num == 7:
        continue
    print(num)
    num += 1
print("All went well")

