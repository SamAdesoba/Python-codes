class PlayGround:

    count = 0
    # _name represent a private variable
    # __name represent name mangling, it is mostly used in inheritance and can be called through the name of the class
    # __name__ is redundant variable that is used and called by python

    def __init__(self, first_name: str, last_name: str, age: int):
        self._age = age
        self._name = f'{last_name} {first_name}'
        PlayGround.count += 1

    # creating a getter function in python
    @property
    def name(self):
        return self._name

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def function_only():
        return "Am on my way"

    # creating a setter function in python
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @age.deleter
    def age(self):
        del self._age

    def __del__(self):
        PlayGround.count -= 1


player_1 = PlayGround("Samson", "Adesoba", 30)
player_2 = PlayGround("Adebanke", "Adefolarin", 30)
print(PlayGround.count)
print(player_1.count)
print(player_2.count)
del player_1
print(PlayGround.count)
print(player_2.count)


