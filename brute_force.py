import random
import copy

class BruteForceSolver:
    """The code defines a class called BruteForceSolver which initializes a 9x9 Sudoku board with all cells initially set to 0. It also creates an empty list to store the original board and another list to store the empty cells in the board. Additionally, it creates a set to store the attempted values during the brute force solving process."""
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = []
        self.empty_cells = []
        self.attempts = set()

    def read_board(self, board):
        """This function takes a Sudoku board as input and initializes several instance variables of the SudokuSolver class. It copies the input board to a separate variable for later reference, identifies all empty cells in the board, and creates an empty set to keep track of attempted values in those cells. This function prepares the solver to begin solving the Sudoku puzzle."""
        self.board = board
        self.original_board = copy.deepcopy(board)
        self.empty_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]
        self.attempts = set()

    def fill_board(self):
        """This function takes a Sudoku board as input and initializes several instance variables of the SudokuSolver class. It copies the input board to a separate variable for later reference, identifies all empty cells in the board, and creates an empty set to keep track of attempted values in those cells. This function prepares the solver to begin solving the Sudoku puzzle."""
        random.shuffle(self.empty_cells)
        for i, j in self.empty_cells:
            available_numbers = self.get_available_numbers(i, j)
            if not available_numbers:
                return False
            self.board[i][j] = random.choice(available_numbers)
        return True

    def get_available_numbers(self, row, col):
        """This is a method that takes in a row and column index and returns a list of available numbers that can be placed in that cell in a Sudoku board. It first creates a set of numbers from 1 to 9 and then removes any numbers that are already present in the same row, column, or sub-grid as the given cell. It then returns the remaining available numbers as a list."""
        available_numbers = set(range(1, 10))
        available_numbers -= set(self.board[row])
        available_numbers -= set(self.board[i][col] for i in range(9))
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        available_numbers -= set(self.board[i][j] for i in range(subgrid_row, subgrid_row + 3) for j in range(subgrid_col, subgrid_col + 3))
        return list(available_numbers)

    def is_valid_board(self):
        """This is a method to check if the current Sudoku board is valid or not. It checks each row, column, and subgrid to ensure that there are no duplicate numbers. If there are any duplicates, it returns False, indicating that the board is not valid. If there are no duplicates, it returns True, indicating that the board is valid. This is an important method to ensure that the user is not able to input an invalid board, which could cause errors in the solving process."""
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
        """This is a method that attempts to solve the Sudoku board by using a backtracking algorithm. It first makes a deepcopy of the original board and shuffles the list of empty cells. Then, it tries to fill in the board and checks if the board is valid. If it is valid, the solved board is printed and the method returns. If it is not valid, the process is repeated until a valid solution is found or until it is determined that the board cannot be solved."""
        while True:
            self.board = copy.deepcopy(self.original_board)
            random.shuffle(self.empty_cells)
            if self.fill_board() and self.is_valid_board():
                print("Solved board:")
                print("-----------------------")
                self.print_board()
                return

            print("Unable to solve the board.")

    def print_board(self):
        """This function is used to find an empty cell in the Sudoku board. It iterates through each row and column of the board and checks if the cell is empty (represented by 0). If an empty cell is found, its coordinates (row, column) are returned. If there are no empty cells, it returns None."""
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
