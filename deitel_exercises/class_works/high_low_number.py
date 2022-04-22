
num_int = 15
i = 1
while 1 <= i <= 3:
    guess_int = int(input("Enter a number : "))
    if guess_int > num_int:
        print("Too High")
        break
    elif guess_int < num_int:
        print("Too Low")
        break
i +=1