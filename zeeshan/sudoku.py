# sudoku.py

import random

class Sudoku:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def is_valid_move(self, row, col, num):
        return (
            self.is_valid_row(row, num) and
            self.is_valid_col(col, num) and
            self.is_valid_box(row - row % 3, col - col % 3, num)
        )

    def is_valid_row(self, row, num):
        return num not in self.grid[row]

    def is_valid_col(self, col, num):
        return all(self.grid[row][col] != num for row in range(9))

    def is_valid_box(self, start_row, start_col, num):
        return all(
            self.grid[row][col] != num
            for row in range(start_row, start_row + 3)
            for col in range(start_col, start_col + 3)
        )

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def generate(self):
        self.solve()
        self.remove_cells()

    def remove_cells(self):
        cells_to_remove = random.randint(40, 50)  # Adjust this range for difficulty
        for _ in range(cells_to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def check_solution(self, user_solution):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != user_solution[i][j]:
                    return False
        return True
