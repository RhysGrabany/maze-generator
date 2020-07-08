#!/usr/bin/python3
import random
from classes.maze import Maze, Cell

#Recursive Backtracking algorithm


'''
Choose the initial cell, mark it as visited and push it to the stack
While the stack is not empty
    Pop a cell from the stack and make it a current cell
    If the current cell has any neighbours which have not been visited
        Push the current cell to the stack
        Choose one of the unvisited neighbours
        Remove the wall between the current cell and the chosen cell
        Mark the chosen cell as visited and push it to the stack 
'''

# Because i'm only allowing one start point and one endpoint (top and bottom respectively)
# I'm going to set all the sides and top to true
def settingTrueFirstRun(maze):

    for y in range(0, len(maze)):
        maze[y][0].setVisited(True)
        maze[y][len(maze[y])-1].setVisited(True)

    for x in range(0, len(maze[0])):
        maze[0][x].setVisited(True)

# this changes all the walls on the bottom to true visited to only allow one exit point
def settingTrueSecRun(maze):
    for x in range(0, len(maze[0])):
        maze[len(maze)-1][x].setVisited(True)

# moving through the maze to make sure there are walls on either side
def settingWalls(maze, curr, nextC):
    cy, cx = curr.coords()
    ny, nx = nextC.coords()

    direction = (ny-cy, nx-cx)

    # solving edgecases that might turn up
    if (cy-1 < 0 or cy+1 >= len(maze)) or (cx-1 < 0 or cx+1 >= (len(maze[0]))):
        return

    if direction[1]:
        maze[cy+1][cx].setVisited(True)
        maze[cy-1][cx].setVisited(True)
    elif direction[0]:
        maze[cy][cx+1].setVisited(True)
        maze[cy][cx-1].setVisited(True)

# main method for this file
# does a backtracking algo to create a maze
def create(maze):

    stack = []

    # Randomly choose the starting position
    initial = random.randrange(1, len(maze[0])-1)
    curr = maze[0][initial]

    curr.setVisited(True)
    curr.setElement(' ')
    stack.append(curr)

    settingTrueFirstRun(maze)

    while(stack):
        curr = stack.pop()
        neighbours = curr.findUnvisited(maze)
        if(neighbours):
            stack.append(curr)

            ran = random.randrange(0, len(neighbours))

            y, x = neighbours[ran]

            nextC = maze[y][x]
            nextC.setElement(' ')
            nextC.setVisited(True)

            if y == (len(maze)-1):
                settingTrueSecRun(maze)
            
            settingWalls(maze, curr, nextC)

            stack.append(nextC)