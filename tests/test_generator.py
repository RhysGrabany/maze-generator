#!/usr/bin/python3

import sys, os, pytest
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from classes.maze import Maze, Cell
from generator.rec_back import create

class TestGenerator:

    def test_starting_position(self):
        maze = Maze(10,10)
        create(maze)

        for x in range(0, len(maze[0])):
            if maze[0][x].getElement() == ' ':
                assert maze[0][x].getElement() == ' '
    
    def test_start_visited(self):
        maze = Maze(10,10)
        create(maze)

        for x in range(0, len(maze[0])):
            if maze[0][x].getVisited() == False:
                assert maze[0][x].getVisited() == False
    
    def test_end_position(self):
        maze = Maze(10,10)
        create(maze)
        lastrow = len(maze)-1

        for x in range(0, len(maze[lastrow])):
            if maze[lastrow][x].getElement() == ' ':
                assert maze[lastrow][x].getElement() == ' '

    def test_end_visited(self):
        maze = Maze(10,10)
        create(maze)
        lastrow = len(maze)-1

        for x in range(0, len(maze[lastrow])):
            if maze[lastrow][x].getElement() == ' ':
                assert maze[lastrow][x].getVisited() == True
        
