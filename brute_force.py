import random
import copy

class BruteForceSolver:
    def __init__(self):
        """Initialize a BruteForceSolver instance."""
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = []
        self.empty_cells = []
        self.attempts = set()

    def read_board(self, board):
        """
        Read a Sudoku board and prepare the solver to begin solving the puzzle.

        Args:
            board (list): The Sudoku board to be solved.
        """
        self.board = board
        self.original_board = copy.deepcopy(board)
        self.empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        self.attempts = set()

    def fill_board(self):
        """
        Fill the empty cells of the Sudoku board.

        Returns:
            bool: True if the board is filled successfully, False otherwise.
        """
        random.shuffle(self.empty_cells)
        for i, j in self.empty_cells:
            available_numbers = self.get_available_numbers(i, j)
            if not available_numbers:
                return False
            self.board[i][j] = random.choice(available_numbers)
        return True

    def get_available_numbers(self, row, col):
        """
        Get the available numbers that can be placed in a cell of the Sudoku board.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            list: The list of available numbers for the given cell.
        """
        available_numbers = set(range(1, 10))
        available_numbers -= set(self.board[row])
        available_numbers -= set(self.board[i][col] for i in range(9))
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        available_numbers -= set(self.board[i][j] for i in range(subgrid_row, subgrid_row + 3) for j in range(subgrid_col, subgrid_col + 3))
        return list(available_numbers)

    def is_valid_board(self):
        """
        Check if the current Sudoku board is valid.

        Returns:
            bool: True if the board is valid, False otherwise.
        """
        for row in self.board:
            if len(set(row)) != 9:
                return False
        for j in range(9):
            col = [self.board[i][j] for i in range(9)]
            if len(set(col)) != 9:
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [self.board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if len(set(subgrid)) != 9:
                    return False
        return True

    def solve_board(self):
        """Solve the Sudoku board using a backtracking algorithm."""
        while True:
            self.board = copy.deepcopy(self.original_board)
            random.shuffle(self.empty_cells)
            if self.fill_board() and self.is_valid_board():
                print("Solved board:")
                print("-----------------------")
                self.print_board()
                return

    def print_board(self):
        """Print the Sudoku board."""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("-----------------------")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
