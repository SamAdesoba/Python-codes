import random

random_number = random.randint(0,10)
print(random_number)
# random.seed(75)
random_number = random.randint(0,10)
print(random_number)

random_number = random.randrange(0,10,2)
print(random_number)

lst = [1,2,3,4,5,6]
print(random.choice(lst))
random.shuffle(lst)
print(lst)

lst_2 = random.random()
print(lst_2)