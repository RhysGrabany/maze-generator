#!/usr/bin/python3


def messages(option):
    if option == "info":
        message = '''
        This is the maze generator which creates small mazes for hobby use
        Please select an option below on what you would like to do:
        '''
    elif option == "sel":
        message = '''
        1. Create New Maze
        2. Check Previous Mazes
        e. Exit
        '''
    elif option == "maze_size":
        message = '''
        You have chosen to create a maze. What size of maze would you like generated?
        '''
    elif option == "maze_created":
        message = '''
        Maze Created
        '''
    elif option == "invalid_choice":
        message = '''
        Invalid Choice, please try again
        '''
    elif option == "invalid_size":
        message = '''
        Invalid Size, please try again
        '''
    elif option == "choose_maze":
        message = '''
        Please choose a maze to view:
        '''

    return message