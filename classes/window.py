#!/usr/bin/python3

import tkinter as tk
import tkinter.filedialog

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.pack()

# This is the mainmenu that will be used 
class MainMenu(Window):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.m_Width = 200
        self.m_Height = 150

        self.create_window()
    
    # creates the main window
    def create_window(self):
        size = str(self.m_Width) + 'x' + str(self.m_Height)
        self.m_Master.geometry(size)
        self.m_Master.title("Create Maze")
        self.m_Master.resizable(width=False, height=False)
        self.create_widgets()
        self.pack()
    
    # this creates the widgets on this window
    def create_widgets(self):

        # BUTTONS
        maze = tk.Button(self.m_Master, text="Maze", command=lambda: self.create_maze_window())
        close = tk.Button(self.m_Master, text="Exit", command=self.m_Master.destroy)
        close.pack(side=tk.BOTTOM, fill=tk.BOTH)
        maze.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # USER ENTRY
        width = tk.Entry(self.m_Master, width='4')
        height = tk.Entry(self.m_Master, width='4')
        width.place(x=130, y=25)
        height.place(x=130, y=50)

        # INFO
        w_info = tk.Label(self.m_Master, text="Width:")
        h_info = tk.Label(self.m_Master, text="Height:")
        w_info.place(x=30, y=25)
        h_info.place(x=30, y=52)

    # this creates the maze window
    def create_maze_window(self):
        window = tk.Toplevel(self.m_Master)
        maze_window = MazeCreation(window)
        maze_window.mainloop()  

# This is the maze creation window that opens once the button is pressed 
class MazeCreation(Window):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.pack()
        self.m_Master.geometry('500x500')

