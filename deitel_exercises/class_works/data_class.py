from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    __slots__ = ['name', 'age']  # this means you cannot change the instance variables
    name: str
    age: int
    children: list = field(default_factory=lambda: [])

    def is_minor(self):
        return self.age <= 18


p1 = Person("Adefolarin", 16, ["ades", "Tayo"])
p2 = Person("Adesoba", 20, ["Tolu", "Tope"])

# print(p1)
# print(p1.name)
# print(p1.age)
print(p2 == p1)
print(p1.is_minor)
