#!/usr/bin/python3


def messages(option):
    if option == "info":
        return('''
        This is the maze generator which creates small mazes for hobby use
        Please select an option below on what you would like to do:
        ''')
    elif option == "sel":
        return('''
        1. Create New Maze
        2. Check Previous Mazes
        e. Exit
        ''')
    elif option == "maze_size":
        return('''
        You have chosen to create a maze. What size of maze would you like generated?
        ''')
    elif option == "maze_created":
        return('''
        Maze Created
        ''')
    elif option == "invalid_choice":
        return('''
        Invalid Choice, please try again
        ''')
    elif option == "invalid_size":
        return('''
        Invalid Size, please try again
        ''')
    elif option == "choose_maze":
        return('''
        Please choose a maze to view:
        ''')
    elif option == "save_maze":
        return('''
        Select a maze to save:
        ''')
    elif option == "save_maze_options":
        return('''
        1. Save 1x image
        2. Save an enhanced image (2x - 10x)
        3. Save text version
        e. Go back
        ''')