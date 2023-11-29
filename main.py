from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)
    p1 = Point(200, 200)
    p2 = Point(500, 500)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()