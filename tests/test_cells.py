#!/usr/bin/python3

import sys, os, pytest
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from classes.maze import Maze, Cell

class TestingCell:

    def test_cell_get_x(self):
        maze = Maze(10,10)
        assert maze[4][3].getX() == 3
    
    def test_cell_get_y(self):
        maze = Maze(10,10)
        assert maze[6][4].getY() == 6
    
    def test_cell_get_element_pound(self):
        maze = Maze(10, 10)
        assert maze[1][1].getElement() == '#'
    
    def test_cell_get_element_space(self):
        maze = Maze(10, 10)
        maze[1][1].setElement(' ')
        assert maze[1][1].getElement() == ' '
    
    def test_cell_get_visited_false(self):
        maze = Maze(10, 10)
        assert maze[1][1].getVisited() == False
    
    def test_cell_get_visited_true(self):
        maze = Maze(10, 10)
        maze[1][1].setVisited(True)
        assert maze[1][1].getVisited() == True
    
    def test_cell_neighbours(self):
        maze = Maze(10,10)
        assert maze[1][1].findUnvisited(maze)