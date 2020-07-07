#!/usr/bin/python3

import tkinter as tk
import tkinter.filedialog
import random

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
        self.m_Master.configure(bg="#f2f2f2")
        self.m_Master.resizable(width=False, height=False)
        self.create_widgets()
        self.pack()
    
    # this creates the widgets on this window
    def create_widgets(self):

        # BUTTONS (prefix b_ for button)
        b_maze = tk.Button(self.m_Master, text="Maze", bg="#f2f2f2", command=lambda: self.create_maze_window())
        b_close = tk.Button(self.m_Master, text="Exit", bg="#f2f2f2", command=self.m_Master.destroy)
        b_close.pack(side=tk.BOTTOM, fill=tk.BOTH)
        b_maze.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # USER ENTRY (prefix l_ for label)
        e_width = tk.Entry(self.m_Master, bg="#f2f2f2", width='4')
        e_height = tk.Entry(self.m_Master, bg="#f2f2f2", width='4')
        e_width.place(x=130, y=25)
        e_height.place(x=130, y=50)

        # INFO (prefix l_ for label)
        l_w_info = tk.Label(self.m_Master, bg="#f2f2f2", text="Width:")
        l_h_info = tk.Label(self.m_Master, bg="#f2f2f2", text="Height:")
        l_w_info.place(x=30, y=25)
        l_h_info.place(x=30, y=52)

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
        self.m_Width = 1000
        self.m_Height = 550

        self.create_window()
        self.pack()


    def create_window(self):
        size = str(self.m_Width) + 'x' + str(self.m_Height)
        self.m_Master.title("Create Maze")
        self.m_Master.configure(bg="#f2f2f2")
        self.m_Master.resizable(width=False, height=False)
        self.m_Master.geometry(size)
        self.create_widgets()
        self.pack()
    

    def create_widgets(self):
        # CANVAS (prefix c_ for canvas)
        c_grid = tk.Canvas(self.m_Master, width=850, height=550)
        #f_tools = tk.Frame(self.m_Master, width=150, height=550, bg="red")
        self.create_grid(c_grid)
        c_grid.pack(anchor=tk.W)
        #f_tools.pack(anchor=tk.E)



        test = tk.Button(self.m_Master, text="Exit", command=self.m_Master.destroy)
        test.place(x=852, y=519, width=150)
    
    def create_grid(self, canvas):
        col_width = 850/50 # Get current width of canvas
        row_height = 550/50 # Get current height of canvas
        col = int(850//col_width)
        row = int(550//row_height)
        #c.delete('grid_line') # Will only remove the grid_line

        grid = []

        for y in range(0, row):
            _ = []
            for x in range(0, col):

                color = ["black", "red"]

                _.append(canvas.create_rectangle(
                    col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height
                    , fill="black"))
                
            grid.append(_)
        print(len(grid[0]))

        for i in range(0, len(grid)):
            print(str(i) + " " + str(grid[i]))

        
        #print(grid[50][50])
        #canvas.itemconfig(grid[50][50], fill="red")
        canvas.pack()

