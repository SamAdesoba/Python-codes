# class PLayer:
#     def __init__(self, name: str, sign: str) -> None;
#     self.name = name


from dataclasses import  dataclass


@dataclass(frozen=True)
class Player:
    name: str
    sign: str


if __name__ == '__main__':
    player1 = Player.name
