#!/usr/bin/python3
import tkinter as tk
from classes.window import Window, MainMenu, MazeCreation
from classes.grid import Grid
from rec_back import create


def main():
    root = tk.Tk()
    main = MainMenu(master=root)
    main.mainloop()





if __name__ == "__main__":
    main()




