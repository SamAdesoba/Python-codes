# Inheriting from a single class
class Animal:
    def __init__(self, name: str, age=0) -> None:
        self.name = name

    def speak(self):
        return "I speak "


class Dog(Animal):
    def __init__(self, type_, age, name: str):
        super().__init__(name, age)
        self.age = 0
        self.type = type_

    def speaking(self):
        return "like a "


class Cat(Animal):
    pass


dog = Dog("Bingo", 0, "local dog")
print(f'{dog.speak()}{dog.speaking()}{dog.type}')
cat = Cat("Kitten")
print(cat.speak())
print(dog.name)
print(dog.age)


# Inheriting from different classes
class Bingo(Dog, Animal):
    pass


bingo = Bingo("bingo", 0, "local")
help(bingo)
