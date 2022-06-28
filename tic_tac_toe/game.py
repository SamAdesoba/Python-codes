from .board import Board
from .player import Player


class Game:
    def __init__(self, board: Board) -> None:
        self.game_board = Board()
        self.player_1 = Player("Player 1", "X")
        self.player_2 = Player("Player 2", "X")

    def create_player_one(self, name, sign):
        self.player_one = Player(name, sign)

    def create_player_two(self, name, sign):
        self.player_two = Player(name, sign)

    def play(self,player: Player, position: int):
        print(f"{player.name}'s turn")
        self.game_board.fill_cell(position, player.sign)

    def determine_turn(self):
        pass
