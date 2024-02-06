import time
import random
from cell import Cell

class Maze:
    max_level = 0
    DIRECTIONS = ['up', 'right', 'down', 'left']

    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None,
            seed = None
        ):
        self.x = x
        self.y = y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.width = num_cols * cell_size_x
        self.width = num_rows * cell_size_y
        self.window = window
        self.seed = seed

        if seed != None:
            random.seed(seed)

        self._create_cells()
        self.start_cell = self._get_cell(0, 0)
        self.end_cell = self._get_cell(self.num_rows - 1, self.num_cols - 1)

        self._break_entrance_and_exit()

        if (self.window):
            #  self._draw_cells()
            print("Constructing maze:")
            self._break_walls_recursive(0, 0, 0)
            print(f"Max recursion level:{self.max_level}")
        
    def _create_cells(self):
        self._cells = []
        y1 = self.y
        for row_no in range(self.num_rows):
            y2 = y1 + self.cell_size_y
            row = []
            x1 = self.x
            for col_no in range(self.num_cols):
                x2 = x1 + self.cell_size_x
                row.append(Cell(x1, y1, x2, y2, self.window))
                x1 += self.cell_size_x
            y1 += self.cell_size_y
            self._cells.append(row)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].remove_top()
        self._cells[self.num_rows - 1][self.num_cols - 1].remove_bottom()

    def _get_cell(self, row, column):
        if row < 0 or column < 0 or row >= self.num_rows or column >= self.num_cols:
            return None
        return self._cells[row][column]

    def _get_neighbours(self, i, j):
        neighbours = []
        for row in range(i - 1, i + 2):
            if row == i:
                for col in range(j - 1, j + 2):
                    cell = self._get_cell(row, col)
                    if cell and not cell.visited:
                        neighbours.append((row, col))
            else:
                cell = self._get_cell(row, j)
                if cell and not cell.visited:
                    neighbours.append((row, j))
        return neighbours
    
    def _remove_walls(self, i1, j1, i2, j2):
        cell1 = self._get_cell(i1, j1)
        cell2 = self._get_cell(i2, j2)
        if i1 == i2:
            if j1 < j2:
                cell1.remove_right()
                cell2.remove_left()
            else:
                cell1.remove_left()
                cell2.remove_right()
        else:
            if i1 < i2:
                cell1.remove_bottom()
                cell2.remove_top()
            else:
                cell1.remove_top()
                cell2.remove_bottom()

    def _break_walls_recursive(self, i, j, level):
        if level > self.max_level:
            self.max_level = level
        self._get_cell(i, j).visited = True
        while True:
            neighbours = self._get_neighbours(i, j)
            if len(neighbours) == 0:
                self._get_cell(i, j).draw()
                # self._animate()
                return
            new_i, new_j = random.choice(neighbours)
            # break wall between the cells
            self._remove_walls(i, j, new_i, new_j)
            self._break_walls_recursive(new_i, new_j, level + 1)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _draw_cells(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._draw_cell(r, c)

    def _animate(self):
        self.window.redraw()
        time.sleep(.05)

    def _reset_cells_visited(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self._get_cell(r, c).visited = False
    
    def solve(self):
        print("Solving maze:")
        self._reset_cells_visited()
        self.max_level = 0
        result = self._solve_r(0, 0, 0)
        if result:
            print("Hurrah! Solved maze! :-)")
        else:
            print("Failed to solve maze! :-(")
        print(f"Max recursion level:{self.max_level}")

    def _next(self, row, col, direction):
        if direction == 'up':
            if self._get_cell(row, col).has_top_wall:
                return None
            return (row - 1, col)
        if direction == 'right':
            if self._get_cell(row, col).has_right_wall:
                return None
            return (row, col + 1)
        if direction == 'down':
            if self._get_cell(row, col).has_bottom_wall:
                return None
            return (row + 1, col)
        if direction == 'left':
            if self._get_cell(row, col).has_left_wall:
                return None
            return (row, col - 1)
        raise Exception("Unknown move direction.")
    
    def _solve_r(self, row, col, level):
        if level > self.max_level:
            self.max_level = level
        # Call the _animate method.
        self._animate()
        # Mark the current cell as visited
        self._cells[row][col].visited = True
        # If you are at the "end" cell (the goal) then return True.
        if self._cells[row][col] is self.end_cell:
            return True
        # For each direction:
        for direction in Maze.DIRECTIONS:
            dir = self._next(row, col, direction)
            if not dir:
                continue
            next_row, next_col = dir
            next_cell = self._get_cell(next_row, next_col)
            # If there is a cell in that direction, there is no wall blocking you,
            # and that cell hasn't been visited:
            if next_cell and not next_cell.visited:
                # Draw a move between the current cell and that cell
                self._cells[row][col]._draw_move(next_cell)
                # Call _solve_r recursively to move to that cell. 
                if self._solve_r(next_row, next_col, level + 1):
                    # If that cell returns True, then just return True and 
                    # don't worry about the other directions.
                    return True
                else:
                    #Otherwise, draw an "undo" move between the current cell and 
                    # the next cell
                    self._cells[row][col]._draw_move(next_cell, True)

        # If none of the directions worked out, return False.
        return False


    
    

