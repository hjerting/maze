from tkinter import Tk, BOTH, Canvas

class Window:
    BACKGROUND_COLOR = '#FFF'

    def __init__(self, width, height):
        self.__root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, borderwidth=0, highlightthickness=0, bg=Window.BACKGROUND_COLOR)
        self.window_running = False
        self.__root.title(f'Window {self.width} x {self.height}')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas.pack()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
    
    def close(self):
        self.window_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        # print(f"line drawn from ({line.point1.x}, {line.point1.y}) to ({line.point2.x}, {line.point2.y})")
