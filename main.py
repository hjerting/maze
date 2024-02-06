#!/usr/bin/env python3

from window import Window
from cell import Cell
from maze import Maze
import sys

sys.setrecursionlimit(10000)

def main():
    MARGIN = 10
    ROWS = 40
    COLUMNS = 90
    CELL_SIZE = 20
    
    width = COLUMNS * CELL_SIZE + 2 * MARGIN
    height = ROWS * CELL_SIZE + 2 * MARGIN

    window = Window(width, height)
    maze = Maze(MARGIN, MARGIN, ROWS, COLUMNS, CELL_SIZE, CELL_SIZE, window)
    window.wait_for_close()

if __name__ == "__main__":
    main()