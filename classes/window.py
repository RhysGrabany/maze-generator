#!/usr/bin/python3

import tkinter as tk
import tkinter.filedialog

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.pack()

class MainMenu(Window):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.m_Master.geometry('200x250')
        self.create_widgets()
        #self.pack()
    
    def create_widgets(self):
        # BUTTONS
        maze = tk.Button(self, text="MAZE", command=lambda: self.create_maze_window())
        close = tk.Button(self, text="EXIT", command=self.m_Master.destroy)
        maze.pack()
        close.pack()

        # USER ENTRY
        width = tk.Entry(self, width='4')
        height = tk.Entry(self, width='4')
        width.pack()
        height.pack()



        

    def create_maze_window(self):
        window = tk.Toplevel(self.m_Master)
        maze_window = MazeCreation(window)

class MazeCreation(Window):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.pack()
        self.m_Master.geometry('500x500')

