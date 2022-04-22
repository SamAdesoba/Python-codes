first_int = int(input("Enter the first integer: "))
second_int = int(input("Enter the second integer: "))
third_int = int(input("Enter the third integer: "))
sum_int = first_int + second_int + third_int
print("The sum is ", sum_int)
average_int = sum_int/3
print("The average is ", average_int)
product_int = first_int * second_int * third_int
print("The product is ", product_int)
if first_int > second_int and first_int > second_int:
    print("The largest number is ", first_int)
elif second_int > first_int and second_int > third_int:
    print("The largest number is ", second_int)
elif third_int > first_int and third_int > second_int:
    print("The largest number is ", third_int)

if first_int < second_int and first_int < third_int:
    print("The smallest number is ", first_int)
elif second_int < first_int and second_int < third_int:
    print("The smallest number is ", second_int)
else:
    print("The smallest number is ", third_int)
