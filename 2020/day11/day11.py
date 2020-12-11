#!/usr/bin/env python3
import sys
class Cell:
    def __init__(self, state): self.state = state
    def __repr__(self): return self.state
    def is_dead(self): return self.state == 'L'
    def is_alive(self): return self.state == '#'

    def set_alive(self): self.state = '#'
    def set_dead(self): self.state = "L"

    def print_char(self): return self.state

class Board:
    def __init__(self, data):
        self.is_changed = True
        self.rows = len(data)
        self.cols = len(data[0])
        grid = []
        for row in data:
            column = []
            for col in row:
                column.append(Cell(col))
            grid.append(column)
        self.grid = grid

    def draw_board(self):
        for row in self.grid:
            for column in row:
                print(column.print_char(), end='')

    def check_neighbours(self, check_row, check_col):
        search_min = -1
        search_max = 2
        neighbour_list = []
        for row in range(search_min, search_max):
            for col in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_col = check_col + col

                valid_neighbour = True
                if neighbour_row < 0 or neighbour_row > (self.rows-1):
                    valid_neighbour = False
                if neighbour_col < 0 or neighbour_col > (self.cols-1):
                    valid_neighbour = False
                if neighbour_row == check_row and neighbour_col == check_col:
                    valid_neighbour = False
                if valid_neighbour:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_col])
        return neighbour_list

    def update_board(self):
        goes_dead = []  # empty
        goes_alive = []  # occupied

        for row in range(self.rows):
            for col in range(self.cols):
                check_neighbours = self.check_neighbours(row, col)

                living_cells = []
                for neighbour_cell in check_neighbours:
                    if neighbour_cell.is_alive():
                        living_cells.append(neighbour_cell)

                cell = self.grid[row][col]
                if cell.is_alive() and len(living_cells) >= 4:
                    goes_dead.append(cell)
                if cell.is_dead() and len(living_cells) == 0:
                    goes_alive.append(cell)

        if len(goes_alive) == 0 and len(goes_dead) == 0:
            self.is_changed = False

        for cell in goes_alive:
            cell.set_alive()
        for cell in goes_dead:
            cell.set_dead()
    def count_alive(self):
        alive = 0
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                if cell.is_alive():
                    alive += 1
        return alive

def load_data(filename):
    with open(filename) as file_:
        data = file_.readlines()
    return data

if __name__ == '__main__':
    filename = sys.argv[1]
    data = load_data(filename)
    board = Board(data)
    while board.is_changed:
        #board.draw_board()
        board.update_board()
        #print()

    print(board.count_alive())
