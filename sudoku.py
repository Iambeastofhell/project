# Credits to Rajdeep for implementation

import random

class Sudoku:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]

    def solve(self): #this function returns a solved grid of sudoku
        empty_cell = self.find_empty_cell()
        if not empty_cell: # for the case when all cells are already filled
            return True
        row, col = empty_cell
        for num in range(1,10): # takes vales from 1 to 9 and each time check if the number will satify the sudoku grid.
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0 # if num not satisfythe solution the again set to zero(empty) for another number to be tried in its place
        return False

    def is_valid_move(self, row, col, num): # the number to be entered must satisfy the conditions of sudoku
        return (
            self.is_valid_row(row, num) and
            self.is_valid_col(col, num) and
            self.is_valid_box(row - row % 3, col - col % 3, num)
        )

    def is_valid_row(self, row, num): # checks if numbers from 1 to 9 in each row
        return num not in self.grid[row]

    def is_valid_col(self, col, num):  # checks if numbers from 1 to 9 in each column
        return all(self.grid[row][col] != num for row in range(9))

    def is_valid_box(self, start_row, start_col, num): # checks if numbers from 1 to 9 in each box
        return all(self.grid[row][col] != num for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3))

    def find_empty_cell(self): # iterates over the entire grid to find empty cells
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def generate(self):
        self.solve() # we take a solved grid 
        self.remove_cells() # we remove some elements from this grid which would be needed to be filled by the user

    def remove_cells(self):
        cells_to_remove = random.randint(40, 50)  # this value removes number of cells from sudoku grid . More number of cells removed, more the game would be tough
        for _ in range(cells_to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0

    def get_grid(self):
        return self.grid # to return current state of the sudoku grid

    def set_grid(self,grid):
        self.grid = [[0] * 9 for _ in range(9)] #empty sudoku grid

    def check_solution(self, user_solution): # compares each cell to solved grid's cell to see win condition
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != user_solution[i][j]:
                    return False
        return True
