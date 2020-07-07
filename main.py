#!/usr/bin/python3
import tkinter as tk
from classes.window import Window, MainMenu, MazeCreation
from classes.grid import Grid
from generator.rec_back import create

def main():
    #root = tk.Tk()
    #main = MazeCreation(master=root)
    #main.mainloop()

    grid = Grid(40, 40)
    create(grid)
    grid.make_image()
    grid.print()
    grid.save_image("test.png")





if __name__ == "__main__":
    main()




