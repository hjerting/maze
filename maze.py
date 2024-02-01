from cell import Cell

class Maze:
    
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x = x1
        self.y = y2
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.width = num_cols * cell_size_x
        self.width = num_rows * cell_size_y

        _create_cells()
    
    def _create_cells():
        self._cells = []

