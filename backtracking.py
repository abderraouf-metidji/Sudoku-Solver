class BacktrackingSolver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        """
        Solve a Sudoku board using backtracking.

        Returns:
            bool: True if the board is solved, False otherwise.
        """
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
        """
        Check if a number is valid to be placed in a position on the Sudoku board.

        Args:
            number (int): The number to be checked.
            position (tuple): The position (row, col) to be checked.

        Returns:
            bool: True if the number is valid, False otherwise.
        """
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
        """
        Print the Sudoku board.
        """
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
        """
        Find the first empty cell in the Sudoku board.

        Returns:
            tuple: The coordinates (row, col) of the empty cell, or None if no empty cell is found.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, column

        return None