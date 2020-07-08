#!/usr/bin/python3
import sys, os
from classes.maze import Maze
from classes.maze_bank import Maze_Bank
from generator.rec_back import create
from messages_protoype import messages

bank = Maze_Bank()

def menu():

    while True:
        #os.system("clear")
        print(messages("info") + messages("sel"))
        selecting()


# why doesn't python have select case
def selecting():

    choosing = True
    while choosing:
        sel = input("Input Selection: ")

        if sel not in ["1", "2", "e"]:
            print(messages("invalid_choice"))
            continue
        if sel == "1":
            choosing = False
            create_maze()
        elif sel == "2":
            choosing = False
            view_mazes()
            pass
        elif sel == "e":
            choosing = False
            sys.exit()


def create_maze():
    print(messages("maze_size"))
    size = input("Input Size as WxH (minimum 5x5): ")
    mm_maze_create(size)


def mm_maze_create(size):
    w, h = size.split('x')
    w, h = int(w), int(h)

    if w < 5 or h < 5:
        print(messages("invalid_size"))
        create_maze()


    maze = Maze(w, h)
    create(maze)
    bank.push(maze)

    print(messages("maze_created"))


def view_mazes():
    print(messages("save_maze"))
    bank.print()
    mz = input("Select: ")

    he = len(bank[int(mz)])
    wi = len(bank[int(mz)][0])

    print(str(wi) + "x" + str(he))
    bank[int(mz)].make_image()
    bank[int(mz)].save_image("text.png")
    bank[int(mz)].save_text("test.txt")
    


    
    



