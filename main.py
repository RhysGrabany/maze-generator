#!/usr/bin/python3
import tkinter as tk
from classes.window import Window
from classes.grid import Grid
from rec_back import solve


def main():
    #root = tk.Tk()
    #window = Window(master=root)
    #window.create_window()
    #window.mainloop()
    #window.buttons_main(window)

    grid = Grid(10, 10)
    solve(grid)




if __name__ == "__main__":
    main()




