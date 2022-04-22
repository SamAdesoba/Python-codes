import math

number_int = int(input("Enter the number: "))
factors = 2
while factors <= (math.ceil(math.sqrt(number_int))):
    if number_int % factors == 0:
        print("not a prime")
        break
    factors += 1
else:
    print(" prime")
