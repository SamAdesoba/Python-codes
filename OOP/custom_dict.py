class custom_dict(dict):

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def __getitem__(self, value):
        return super().__getitem__(value)


# my_dict = {'Name': "Adesoba", 'age': 30}
# my_dict1 = {'Name': "Samson", 'age': 100}
#
# temp_file = open("my_dict.txt", mode="w")
# print(my_dict, file=temp_file)
# print(my_dict1, file=temp_file)
# print(my_dict['age'], file=temp_file)
# temp_file.close()

file = open("my_dict.txt", mode="r")
print(file.read())
