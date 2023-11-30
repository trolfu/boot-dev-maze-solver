from cell import Cell
from line import Line, Point
from maze import Maze
from window import Window

def main():
    win = Window(800, 600)

    maze = Maze(100, 100, 4, 6, 100, 100, win)

    win.wait_for_close()

main()