# def quotient(x, y):
#     if y == 0:
#         raise ValueError("Wrong denominator value")
#     return x / y
#
#
# num = int(input("Enter the numerator: "))
# den = int(input("Enter the denominator: "))
# while True:
#     try:
#         print(quotient(num, den))
#         break
#     except ValueError:
#         print("Wrong value")
#         num = int(input("Enter the numerator: "))
#         den = int(input("Enter the denominator: "))

try:
    print("Life is good")
    # print(1/0)
    print([1,2,3][4])
    print("After life")
except ZeroDivisionError as e:
    print("ZeroError", e)
except IndexError as e:
    print("IndexError", e)
else:
    print("ELse I run only when there's no error")
finally:
    print("Finally, I run everytime")
