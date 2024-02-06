from point import Point
from line import Line
from window import Window

class Cell:

    WALL_COLOR = '#000'
    PATH_COLOR = '#0F0'
    PATH_UNDO = '#AAA'

    def __init__(self, x1, y1, x2, y2, window = None):
        self._window = window
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def remove_top(self):
        self.has_top_wall = False
    
    def remove_bottom(self):
        self.has_bottom_wall = False

    def remove_right(self):
        self.has_right_wall = False

    def remove_left(self):
        self.has_left_wall = False
    
    def _draw_wall(self, x1, y1, x2, y2, color):
        line = Line(Point(x1, y1), Point(x2, y2))
        self._window.draw_line(line, color)

    def draw(self):
        """
        # Clear walls
        # Clear top wall
        self._draw_wall(self._x1 + 1, self._y1, self._x2 - 1, self._y1, Window.BACKGROUND_COLOR)

        # Clear right wall
        self._draw_wall(self._x2, self._y1 + 1, self._x2, self._y2 - 1, Window.BACKGROUND_COLOR)

        # Clear bottom wall
        self._draw_wall(self._x1 + 1, self._y2, self._x2 - 1, self._y2, Window.BACKGROUND_COLOR)

        # Clear left wall
        self._draw_wall(self._x1, self._y1 + 1, self._x1, self._y2 - 1, Window.BACKGROUND_COLOR)
        """
        # Draw top wall
        if self.has_top_wall:
            self._draw_wall(self._x1 - 1, self._y1, self._x2 + 1, self._y1, Cell.WALL_COLOR)

        # Draw right wall
        if self.has_right_wall:
            self._draw_wall(self._x2, self._y1 - 1, self._x2, self._y2 + 1, Cell.WALL_COLOR)

        # Draw bottom wall
        if self.has_bottom_wall:
            self._draw_wall(self._x1 - 1, self._y2, self._x2 + 1, self._y2, Cell.WALL_COLOR)

            # Draw left wall
        if self.has_left_wall:
            self._draw_wall(self._x1, self._y1 - 1, self._x1, self._y2 + 1, Cell.WALL_COLOR)

    
    def _midpoint(self, val1, val2):
        return val1 + (val2 - val1) // 2

    def _draw_move(self, to_cell, undo=False):
        color = Cell.PATH_COLOR
        if undo:
            color = Cell.PATH_UNDO
        x1 = self._midpoint(self._x1, self._x2)
        y1 = self._midpoint(self._y1, self._y2)
        x2 = self._midpoint(to_cell._x1, to_cell._x2)
        y2 = self._midpoint(to_cell._y1, to_cell._y2)
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line = Line(point1, point2)
        self._window.draw_line(line, color)
