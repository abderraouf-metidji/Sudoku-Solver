import random

class BruteForceSolver:
    def __init__(self, board):
        self.board = board
        self.attempts = 0

    def solve(self):
        """The above code is a method to solve a Sudoku puzzle using a recursive algorithm. It first prints the original Sudoku board, then starts solving it. If a solution is found, it prints the solved board and the number of attempts it took to solve it. If no solution is found, it prints a message indicating that."""
        print("Original Sudoku:")
        self.print_board()
        print("Let me work")

        solved = self.solve_recursive(0)

        if solved:
            print("\nSolution:")
            self.print_board()
            print(f"\nSolved in {self.attempts} attempts.")
        else:
            print("\nNo solution found.")

    def solve_recursive(self, index):
        """This is a recursive function that solves a Sudoku board by backtracking. It takes an index parameter that represents the current cell being evaluated. If the index reaches 81, it means all cells have been filled and the function returns True. If the current cell already has a value, the function moves on to the next cell. Otherwise, it generates a list of random numbers from 1 to 9 and tries each one until a valid number is found. If a valid number is found, it is assigned to the current cell and the function moves on to the next cell. If the function successfully solves the board, it returns True. Otherwise, it backtracks and tries a different number until a solution is found or all possibilities have been exhausted. The function keeps track of the number of attempts made and prints the board after each attempt."""
        if index == 81:
            return True

        row = index // 9
        col = index % 9

        if self.board[row][col] != 0:
            return self.solve_recursive(index + 1)

        random_numbers = random.sample(range(1, 10), 9)
        for num in random_numbers:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                self.attempts += 1
                print(f"Attempt {self.attempts}:")
                self.print_board()
                if self.solve_recursive(index + 1):
                    return True
                self.board[row][col] = 0

        return False

    def is_valid(self, row, col, num):
        """This function checks if a given number is valid to be placed in a specific row and column of a Sudoku board. It first checks the row and column to ensure that the number is not already present. Then it checks the 3x3 box that the cell belongs to, to ensure that the number is not already present in that box. If the number passes all these checks, the function returns True, indicating that it is valid to be placed in that cell. If not, it returns False."""
        # Check row
        for i in range(9):
            if self.board[row][i] == num and i != col:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num and (start_row + i != row or start_col + j != col):
                    return False

        return True

    def print_board(self):
        """This is a method to print the current state of the Sudoku board. It uses nested loops to iterate through each row and column of the board, and prints out the values in a formatted way with horizontal and vertical lines separating the 3x3 sub-grids. This method is useful for checking the progress of the game and ensuring that the board is being updated correctly."""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")