import math

number_int = int(input("Enter the number: "))
square_int = number_int * number_int
log_int = math.floor(math.log10(square_int))
power_int = math.pow(10, log_int)
remainder_int = number_int % power_int
if number_int == remainder_int:
    print("It is an ambigram")
else:
    print("It is not an ambigram")