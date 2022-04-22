x = int(input("Enter the number: "))
# factors = 1
# sum_of_factors = 0
# while factors < x:
#     if x % factors == 0:
#         sum_of_factors += factors
#     factors += 1
# print("Sum of factors is ", sum_of_factors)
# if sum_of_factors == x:
#     print(x, " is a perfect number")
# elif sum_of_factors > x:
#     print(x, " is an abundant number")
# elif sum_of_factors < x:
#     print(x, " is a deficient number")

# OR

factors = 2
sum_of_factors = 1
while factors <= (x//2):
    if x % factors == 0:
        sum_of_factors += factors
    factors += 1
print("Sum of factors is ", sum_of_factors)
if sum_of_factors == x:
    print(x, " is a perfect number")
elif sum_of_factors > x:
    print(x, " is an abundant number")
elif sum_of_factors < x:
    print(x, " is a deficient number")
