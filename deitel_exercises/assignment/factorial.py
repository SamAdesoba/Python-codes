user_input = int(input("Enter the number : "))
# factorial = 1
# while user_input > 0:
#     factorial = factorial * user_input
#     user_input -= 1
# print(factorial)
# print()
#
# user_input = int(input("Enter the number : "))
# sum = 0
# while user_input > 0:
#     sum = sum + user_input
#     user_input -= 1
print(sum)
print()
total = 0
for i in range(1, (user_input + 1)):
    total += i
print(total)

# recursion can be explained with factorial, it means, a function calling another function


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
