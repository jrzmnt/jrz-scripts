"""
Module for solving Sudoku puzzles.

Classes:
    Board: Represents the Sudoku board and contains methods for validating and solving the puzzle.

Methods of the Board class:
    __init__(self, board): Initializes the board with a 9x9 matrix.
    __str__(self): Returns a visual representation of the board, where empty cells are marked with '*'.
    find_empty_cell(self): Finds the next empty cell (value 0) on the board.
    valid_in_row(self, row, num): Checks if a number is valid in a specific row.
    valid_in_col(self, col, num): Checks if a number is valid in a specific column.
    valid_in_square(self, row, col, num): Checks if a number is valid in the 3x3 square containing the cell (row, col).
    is_valid(self, empty, num): Checks if a number is valid in a specific cell, considering row, column, and square.
    solver(self): Solves the Sudoku puzzle using backtracking. Returns True if the puzzle is solvable, False otherwise.

Functions:
    solve_sudoku(board): Takes a Sudoku board (9x9 matrix) and attempts to solve it. Prints the original puzzle and the solution if found.

Usage Example:
    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
    solve_sudoku(puzzle)
"""


class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_str = ""
        for row in self.board:
            row_str = [str(i) if i else "*" for i in row]
            board_str += " ".join(row_str)
            board_str += "\n"
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False


def solve_sudoku(board):
    gameboard = Board(board)
    print(f"Puzzle to solve:\n{gameboard}")
    if gameboard.solver():
        print(f"Solved puzzle:\n{gameboard}")
    else:
        print("The provided puzzle is unsolvable.")
    return gameboard


puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5],
]

solve_sudoku(puzzle)
