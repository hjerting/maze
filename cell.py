from point import Point
from line import Line

class Cell:

    WALL_COLOR = 'red'

    def __init__(self, window, x1, y1, x2, y2):
        self._win = window
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            print("has left wall")
            line = Line(top_left, bottom_left)
            self._win.draw_line(line, self.WALL_COLOR)
        if self.has_right_wall:
            print("has right wall")
            line = Line(top_right, bottom_right)
            self._win.draw_line(line, self.WALL_COLOR)
        if self.has_top_wall:
            print("has top wall")
            line = Line(top_left, top_right)
            self._win.draw_line(line, self.WALL_COLOR)
        if self.has_bottom_wall:
            print("has bottom wall")
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line, self.WALL_COLOR)
    
    def midpoint(self, val1, val2):
        return val1 + (val2 - val1) // 2

    def draw_move(self, to_cell, undo=False):
        color = 'red'
        if undo:
            color = 'gray'
        x1 = self.midpoint(self._x1, self._x2)
        y1 = self.midpoint(self._y1, self._y2)
        x2 = self.midpoint(to_cell._x1, to_cell._x2)
        y2 = self.midpoint(to_cell._y1, to_cell._y2)
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line = Line(point1, point2)
        self._win.draw_line(line, color)
