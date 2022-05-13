print("module2", __name__)




def add(x, y):
    return x + y

if __name__ == "__main__":
    print("In module 2")
    print("Module 2", __name__)


import pathlib
print(pathlib.Path.cwd())
print(pathlib.Path.home())
