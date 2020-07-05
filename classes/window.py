#!/usr/bin/python3

import tkinter as tk
import tkinter.filedialog

class Window(tk.Frame):
    def __init__(self, master=None, width="250", height="250"):
        super().__init__(master)
        self.m_Master = master
        self.m_Master.geomtery(width, height)


        self.create_window()
        self.pack()
        #self.buttons_main()
    
    def create_window(self):
        wndw = self.m_Master
        wndw.title("Testing")
        wndw.configure(width=250, height=250, bg="lightgrey")

        self.buttons_main()

    
    def buttons_main(self):
        btnSave = tk.Button(self, text="Save", bd=5, command=self.save_as_pic)
        btnQuit = tk.Button(self, text="Quit", bd=5, command=self.master.destroy)
        btnSave.pack(side="top")
        btnQuit.pack(side="bottom")
    
    def save_as_pic(self):
        sa = tkinter.filedialog.asksaveasfile(mode="w", defaultextension=".png")

        if sa is None:
            return
        