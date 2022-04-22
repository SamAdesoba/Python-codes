x = int(input("Enter the score : "))
if x < 40:
    print("Grade is an F")
elif 40 <= x <= 49:
    print("Grade is a D")
elif 50 <= x <= 59:
    print("Grade is a C")
elif 60 <= x <= 69:
    print("Grade is a B")
else:
    print("Grade is an A")
