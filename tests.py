import unittest
from functools import reduce

from maze import Maze
from window import Window

class Tests(unittest.TestCase):

    ROWS = 6
    COLS = 5
    CELL_SIZE = 20
    MARGIN = 0

    def test_maze_create_cells(self):
        m1 = Maze(Tests.MARGIN, Tests.MARGIN, Tests.ROWS, Tests.COLS, Tests.CELL_SIZE, Tests.CELL_SIZE)
        self.assertEqual(
            len(m1._cells),
            Tests.ROWS
        )
        self.assertEqual(
            len(m1._cells[0]),
            Tests.COLS
        )
    
    def test_maze_has_exits(self):
        mz = Maze(Tests.MARGIN, Tests.MARGIN, Tests.ROWS, Tests.COLS, Tests.CELL_SIZE, Tests.CELL_SIZE)
        cell_top_left = mz._get_cell(0, 0)
        cell_bottom_right = mz._get_cell(Tests.ROWS - 1, Tests.COLS - 1)
        self.assertFalse(cell_top_left.has_top_wall)
        self.assertFalse(cell_bottom_right.has_bottom_wall)
    
    def test_get_neighbours(self):
        mz = Maze(Tests.MARGIN, Tests.MARGIN, Tests.ROWS, Tests.COLS, Tests.CELL_SIZE, Tests.CELL_SIZE)
        
        cell_1 = mz._get_cell(0, 0)
        cell_1.visited = True
        neighbours = mz._get_neighbours(0, 0)
        manual_neighbours = [(0,1), (1,0)]
        self.assertEqual(neighbours, manual_neighbours)
        cell_1.visited = False

        cell_1 = mz._get_cell(1, 1)
        cell_1.visited = True
        neighbours = mz._get_neighbours(1, 1)
        manual_neighbours = [(0,1), (1,0), (1,2), (2,1)]
        self.assertEqual(neighbours, manual_neighbours)
        cell_1.visited = False

        cell_1 = mz._get_cell(Tests.ROWS - 1, Tests.COLS - 1)
        cell_1.visited = True
        neighbours = mz._get_neighbours(Tests.ROWS - 1, Tests.COLS - 1)
        manual_neighbours = [(Tests.ROWS - 2, Tests.COLS - 1), (Tests.ROWS - 1, Tests.COLS - 2)]
        self.assertEqual(neighbours, manual_neighbours)
        cell_1.visited = False
    
    def test_reset_cells_visited(self):
        mz = Maze(Tests.MARGIN, Tests.MARGIN, Tests.ROWS, Tests.COLS, Tests.CELL_SIZE, Tests.CELL_SIZE)
        # Get list of items from list of list of items.
        cell_list = reduce(lambda x, y: x + y, mz._cells)

        # Set all cells to True
        for row in range(mz.num_rows):
            for col in range(mz.num_cols):
                mz._get_cell(row, col).visited = True
        
        # Check all are True
        cell_map = map(lambda x: x.visited, cell_list)
        self.assertTrue(all(cell_map))
        
        # Reset to False
        mz._reset_cells_visited()
        
        # Check all are False now
        cell_map = map(lambda x: x.visited, cell_list)
        self.assertTrue(not any(cell_map))

if __name__ == "__main__":
    unittest.main()