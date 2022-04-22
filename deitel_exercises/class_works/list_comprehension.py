lst = []
for i in range(1,10):
    lst.append(i)
print(lst)
print()

print(list(range(1,10)))
print()

print([i for i in range(1,10)])
print()

print([i for i in range(1,10) if i%2 ==0])
print()

print([i if i%2 ==0 else i**2 for i in range(1, 10)])
print()

rang = int(input("Enter the number of elements "))
print([int(input(f"Enter the element {i+1} ")) for i in range(0,rang)])

# List nexted for
list_nexted_for = [(x,y) for x in range(1,5) for y in range(1,2)]
print(list_nexted_for)

upper_case = [name.upper() for name in ["tola", "samson", "dele"]]
print(upper_case)

upper_case_value = [len(name) for name in ["tola", "samson", "dele"]]
print(upper_case_value)

list_dictionary = [{key:value} for key, value in zip(upper_case, upper_case_value)]
print(list_dictionary)

print(list[zip(upper_case, upper_case_value)])

#  changing the apprentices to get a set comprehension
upper_case_value_set = {len(name) for name in ["tola", "samson", "dele"]}
print(upper_case_value_set)

#  changing the apprentices to get a dictionary comprehension
upper_case_value_dict = {key:value for key, value in zip(upper_case, upper_case_value)}
print(upper_case_value_dict)

def get_first(s: str) -> str:
    return s[0]

l = [get_first(val) for val in ['Hello', 'How', 'Are', 'You']]
print(l)