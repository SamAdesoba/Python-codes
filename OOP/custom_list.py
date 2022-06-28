class CustomList(list):
    # pass
    def __getitem__(self, index):
        pass

        if index <= 0:
            raise IndexError('Index out of bounds')

        return super().__getitem__(index - 1)

    def __setitem__(self, index, value):
        pass

        if index <= 0:
            raise IndexError('Index out of bounds')

        return super().__setitem__(index - 1, value)


a = CustomList()
a.append(10)
a.append(20)
a.append(30)
print(a)
print(a[1])
a[3] = 100
print(a)