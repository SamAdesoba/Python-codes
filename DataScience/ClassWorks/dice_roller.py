import random


def dice_roll(numbers_of_dice, numbers_of_side):
    lst = []
    for die in range(numbers_of_dice):
        side_number = random.randint(1, numbers_of_side)
        lst.append(side_number)
    print(f'The number of dice is {numbers_of_dice}')
    print(f'The number of sides is {numbers_of_side}')
    print(f'The highest number rolled is {max(lst)}')
    print(f'The total sum of number rolled is {sum(lst)}')
    print("The list of numbers generated is")
    return lst


def collect_user_input():
    global numbers_of_dice, numbers_of_side

    numbers_of_dice = float(input("Enter the numbers of dices(die): "))
    numbers_of_side = float(input("Enter the numbers of sides: "))

    while numbers_of_dice <= 0:
        print("Invalid input, Please enter a whole number ")
        numbers_of_dice = int(input("Enter the numbers of dices(die): "))
    else:
        while numbers_of_side <= 0:
            print("Invalid input, Please enter a positive whole number ")
            numbers_of_side = int(input("Enter the numbers of sides: "))
        else:
            pass
    return dice_roll(numbers_of_dice, numbers_of_side)


print(collect_user_input())
