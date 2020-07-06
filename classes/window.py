#!/usr/bin/python3

import tkinter as tk
import tkinter.filedialog

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.m_Master = master
        self.pack()
