class BacktrackingSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        """This is a recursive function that solves a Sudoku board using backtracking. It first looks for an empty cell on the board, and if there are none left, it returns True, indicating that the board has been solved. If there is an empty cell, it tries to fill it with a number from 1 to 9, and checks if the number is valid according to the rules of Sudoku. If the number is valid, it continues to recursively solve the board. If the board cannot be solved with that number, it backtracks and tries the next number. If no number works, it returns False, indicating that the board is unsolvable."""

        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def valid(self, number, position):

        """This function checks if a given number is valid to be placed in a certain position on the Sudoku board. It first checks the row and column of the position to make sure the number is not already present. Then, it checks the 3x3 box that the position belongs to, making sure the number is not already present. If the number is not found in any of these checks, the function returns True, indicating that the number is valid for the given position."""
        # Check row
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == number and position[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][position[1]] == number and position[0] != i:
                return False

        # Check 3x3 box
        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == number and (i, j) != position:
                    return False

        return True

    def print_board(self):
        """The above code defines a class with two methods - print_board and find_empty. The print_board method prints the current state of the Sudoku board in a user-friendly format, with horizontal and vertical separators and empty cells represented by zeros. The find_empty method iterates through the board to find the first empty cell (represented by a zero) and returns its coordinates as a tuple. If no empty cell is found, it returns None. Overall, these methods are useful for visualizing and manipulating a Sudoku board."""
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

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, column

        return None