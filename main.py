#!/usr/bin/env python3

from window import Window
from cell import Cell

def main():
    window = Window(800, 400)
    cell1 = Cell(window, 1, 1, 100, 100)
    cell1.draw()
    cell2 = Cell(window, 100, 1, 200, 100)
    cell2.draw()
    cell1.draw_move(cell2, undo=True)
    cell3 = Cell(window, 1, 100, 100, 200)
    cell3.draw()
    cell1.draw_move(cell3)
    window.wait_for_close()

main()