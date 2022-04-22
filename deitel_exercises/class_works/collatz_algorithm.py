num_int = int(input("Enter a number : "))
while num_int != 1:
    if num_int % 2 == 1:
        num_int = int(num_int * 3 + 1)
    elif num_int % 2 == 0:
        num_int = int(num_int/2)
    print(num_int, end=" ")
