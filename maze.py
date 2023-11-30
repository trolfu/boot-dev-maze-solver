from cell import Cell
import time
from window import Window

class Maze:
    def __init__(
            self,
            x1: float,
            y1: float,
            num_rows: int,
            num_cols: int,
            cell_size_x: float,
            cell_size_y: float,
            window: Window) -> None:
        
        # Top left corner of the maze
        self.__x1 = x1
        self.__y1 = y1

        # Maze dimensions as cells
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[None] * self.__num_rows] * self.__num_cols
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        left = self.__x1 + (i - 1) * self.__cell_size_x
        right = left + self.__cell_size_x
        top = self.__y1 + (j - 1) * self.__cell_size_y
        bottom = top + self.__cell_size_y

        cell = Cell(left, top, right, bottom, self.__window)
        self.__cells[i][j] = cell
        cell.draw()
        self.__animate()

    # TODO: The picture doesn't look as expected until after moving the window on screen. Needs investigation
    def __animate(self):
        self.__window.redraw()
        time.sleep(0.05)
