class Player:
    name = "Yakubu"
    # def init also known as redundant init serve the same purpose as constructor

    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age


    # def say_my_name(self):
    #     print("Yakubu")

#
# player1 = Player()
# player2 = Player()
# player3 = Player()
# player1.name = "Ronaldo"
# player2.name = "Messi"
# print(player1.name)
# print(player2.name)
# print(player3.name)

player4 = Player("Samson", 30)
print(player4.name)
print(player4.age)

