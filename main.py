#!/usr/bin/python3
import tkinter as tk
import sys
from classes.window import Window, MainMenu, MazeCreation
from classes.maze import Maze
from generator.rec_back import create
from mainmenu_proto.main_menu_prototype import menu


def main():
    #root = tk.Tk()
    #main = MazeCreation(master=root)
    #main.mainloop()

    menu()



if __name__ == "__main__":
    main()




