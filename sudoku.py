import pygame
from pygame.locals import *
from backtracking import BacktrackingSolver
from brute_force import BruteForceSolver

class Sudoku:
    def __init__(self, filename):
        """
        Initialize the Sudoku object.

        Args:
            filename (str): The name of the file containing the Sudoku grid.
        """
        self.filename = filename
        self.grid = self._parse_file()
        self.initial_grid = [row[:] for row in self.grid]

    def _parse_file(self):
        """
        Read a file and convert it into a 2D list of integers representing a Sudoku grid.
        Each line in the file is converted into a row in the grid.
        The '_' character is treated as a 0 in the grid.
        Returns the grid.
        """
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        
        grid = []
        for line in lines:
            row = [int(x) if x != '_' else 0 for x in line.strip()]
            grid.append(row)
        
        return grid

    def solve_with_backtracking(self):
        """
        Solve the Sudoku grid using the backtracking algorithm.
        """
        solver = BacktrackingSolver(self.grid)
        solver.solve()
        self.grid = solver.board

    def solve_with_brute_force(self):
        """
        Solve the Sudoku grid using the brute force algorithm.
        """
        solver = BruteForceSolver()
        solver.read_board(self.grid)
        solver.solve_board()
        self.grid = solver.board

    def run_game(self):
        """
        Run the Sudoku game using Pygame.
        """
        pygame.init()
        screen = pygame.display.set_mode((600, 650))
        pygame.display.set_caption("Sudoku Solver")

        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        button_color = pygame.Color(50, 150, 255)
        text_color = pygame.Color(255, 255, 255)

        solve_button_rect = pygame.Rect(220, 585, 160, 50)
        solve_button_text = font.render("Solve", True, text_color)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if solve_button_rect.collidepoint(mouse_pos):
                        self.solve_with_backtracking()  # Choose between self.solve_with_brute_force() and self.solve_with_backtracking()

            screen.fill((255, 255, 255))

            for i in range(9):
                for j in range(9):
                    cell_value = self.grid[i][j]
                    initial_value = self.initial_grid[i][j]
                    cell_text = font.render(str(cell_value), True, (0, 0, 0))
                    cell_rect = pygame.Rect(j * 60 + (j // 3) * 10 + 20, i * 60 + (i // 3) * 10 + 20, 60, 60)
                    if initial_value != 0:
                        pygame.draw.rect(screen, (220, 220, 220), cell_rect)
                    pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)
                    screen.blit(cell_text, cell_rect.move(22, 12))

            pygame.draw.rect(screen, button_color, solve_button_rect)
            screen.blit(solve_button_text, solve_button_rect.move(50, 12))

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()


# We choose which file we want to parse
sudoku = Sudoku('puzzles/sudoku.txt')
sudoku.run_game()
