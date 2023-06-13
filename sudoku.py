from backtracking import BacktrackingSolver

class Sudoku:
    def __init__(self, filename):
        self.filename = filename
        self.grid = self._parse_file()

    def _parse_file(self):
        """This function reads a file and converts it into a 2D list of integers, representing a Sudoku grid. Each line in the file is read and converted into a row in the grid. The '_' character is treated as a 0 in the grid. The function returns the grid."""
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        grid = []
        for line in lines:
            row = [int(x) if x != '_' else 0 for x in line.strip()]
            grid.append(row)
        return grid

#We choose which file we want to parse
sudoku = Sudoku('evil_sudoku.txt')
board = sudoku.grid

solver = BacktrackingSolver(board)
solver.print_board()
solver.solve()
print("-----------------------")
solver.print_board()