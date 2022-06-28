from pythonProject.tic_tac_toe.board_exception import BoardException


class Board:

    def __init__(self):
        self.board = ['&'] * 9

    def display_board(self):
        for index, cell in enumerate(self.board):
            if index != 0 and index % 3 == 0:
                print()
            if index % 3 == 0:
                print('|', end="")
            print(f'{cell:^3}|', end="")
        print()


    @staticmethod
    def is_position_allowed(position):
        if position not in range(1,10):
            raise BoardException('Invalid cell position')

    def is_cell_empty(self, position) -> bool:
        self.is_position_allowed(position)
        return self.board[position - 1] == ''

    def is_board_full(self) -> bool:
        return all(self.board)

    def fill_cell(self, position, sign):
        self.is_position_allowed(position)
        if self.is_cell_empty(position):
            self.board[position - 1] = sign
        else:
            raise BoardException(f'Cell position {position} is not empty')






if __name__ == '__main__':
    board = Board()
    print(board.board)
    board.board[2] = '*'
    board.display_board()
    print(board.is_cell_empty(3))
    print(board.is_cell_empty(4))
    print(board.is_board_full())
