from cell import Cell
from line import Line, Point
from window import Window

def main():
    win = Window(800, 600)

    p1 = Point(200, 200)
    p2 = Point(500, 500)
    line = Line(p1, p2)
    win.draw_line(line, "red")

    full_cell = Cell(100, 100, 200, 200, win)
    full_cell.draw()

    missing_left_cell = Cell(150, 150, 250, 250, win)
    missing_left_cell.has_left_wall = False
    missing_left_cell.draw()

    missing_right_cell = Cell(350, 350, 450, 450, win)
    missing_right_cell.has_right_wall = False
    missing_right_cell.draw()

    win.wait_for_close()

main()