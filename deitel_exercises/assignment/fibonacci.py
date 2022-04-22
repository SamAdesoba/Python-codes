user_input = int(input("Enter the nth number: "))
i = 0
first_num = 0
second_num = 1
print(first_num, second_num, end=" ")
while i < user_input:
    sum_int = first_num + second_num
    print(sum_int, end=" ")
    first_num = second_num
    second_num = sum_int
    i += 1
my_string = "Adesoba"
my_string.find