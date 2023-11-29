from line import Line, Point
from window import Window

class Cell:
    """Defines a maze cell by its top left (point 1) and bottom right (point 2) coordinates"""
    def __init__(self, x1: float, y1: float, x2: float, y2: float, window: Window) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__window = window
        self.__wall_color = "blue"

    def draw(self):
        if self.has_left_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), self.__wall_color)
        if self.has_right_wall:
            self.__window.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), self.__wall_color)
        if self.has_top_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), self.__wall_color)
        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), self.__wall_color)