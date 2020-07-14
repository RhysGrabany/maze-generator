#!/usr/bin/python3
import sys, os
from classes.maze import Maze
from classes.maze_bank import Maze_Bank
from generator.rec_back import create

from .messages_protoype import messages

bank = Maze_Bank()

# creates the directories to hold the images and text
def create_dir():
    path = os.getcwd()

    maze_dir = path + "/maze"
    images = maze_dir + "/images"
    text = maze_dir + "/text"

    dirs = [maze_dir, images, text]
    
    for dir in dirs:

        if os.path.isdir(dir):
            continue
        else: 
            try:
                os.mkdir(dir)
            except (OSError, IsADirectoryError):
                print("Creating directory failed")



# why doesn't python have select case
def mm_selecting():

    choosing = True
    while choosing:
        sel = input("Input Selection: ")

        if sel not in ["1", "2", "e"]:
            print(messages("invalid_choice"))
            continue
        if sel == "1":
            create_maze()
        elif sel == "2":
            view_mazes()
            pass
        elif sel == "e":
            sys.exit()


def create_maze():
    print(messages("maze_size"))
    size = input("Input Size as WxH (minimum 5x5): ")
    mm_maze_create(size)


# menu with options to create the maze
def mm_maze_create(size):
    w, h = size.split('x')
    w, h = int(w), int(h)

    if w < 5 or h < 5:
        w, h = 5, 5


    maze = Maze(w, h)
    create(maze)
    bank.push(maze)

    print(messages("maze_created"))
    menu()

def maze_selecting(mz):

    while True:
        sel = input("Select: ")

        if sel not in ["1", "2", "3", "e"]:
            print(messages("invalid_choice"))
            continue
        if sel == "1":
            bank[int(mz)].make_image()
            bank[int(mz)].save_image(0)
            menu()

        elif sel == "2":

            mag = input("Enter increase: ")

            if int(mag) < 2:
                mag = 2
            elif int(mag) > 10:
                mag = 10
            else:
                m = int(mag)

            bank[int(mz)].increase_image_size(m)
            bank[int(mz)].save_image(1)
            menu()
        
        elif sel == "3":
            bank[int(mz)].save_text()
            menu()

        elif sel == "e":
            menu()

# output for viewing the mazes saved
def view_mazes():
    print(messages("save_maze"))
    bank.print()
    mz = input("Select: ")
    
    print(messages("save_maze_options"))

    create_dir()

    maze_selecting(mz)

    
# the main method for this program
def menu():
    while True:
        os.system("clear")
        print(messages("info") + messages("sel"))

        try:
            mm_selecting()
        except KeyboardInterrupt:
            sys.exit()

    
    



