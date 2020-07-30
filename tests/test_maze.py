#!usr/bin/python3


import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from classes.maze import Maze, Cell

class TestingMaze:
    def test_width(self):
        maze = Maze(20, 5)
        assert maze.getCols() == 20
    
    def test_min_width(self):
        maze = Maze(2,2)
        assert maze.getCols() == 5
    
    def test_height(self):
        maze = Maze(5,50)
        assert maze.getRows() == 50

    def test_min_height(self):
        maze = Maze(2,2)
        assert maze.getRows() == 5
    
    def test_maze_name(self):
        maze = Maze(5,5)
        assert maze.getName() == "MAZE_5x5"
    
    def test_maze_get(self):
        maze = Maze(5,5)
        assert isinstance(maze[0][0], Cell)
    
    def test_maze_set_name(self):
        maze = Maze(5,5)
        maze.setName("Testing")
        assert maze.getName() == "Testing"
    
    def test_maze_fill_pound(self):
        maze = Maze(5,5)
        assert maze[0][0].getElement() == '#'

    def test_maze_fill_space(self):
        maze = Maze(5,5)
        assert maze[4][4].getElement() != ' '
    
    def test_maze_image_null(self):
        maze = Maze(5,5)
        assert maze.getMazeImage() == []

    def test_maze_eimage_null(self):
        maze = Maze(5,5)
        assert maze.getMazeEnhancedImage() == []
    
    def test_maze_len(self):
        maze = Maze(5,10)
        assert len(maze) == 10

class TestingMazeGenerated:
    pass
    






