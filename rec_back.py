#!/usr/bin/python3
import random
from classes.grid import Grid
from classes.grid import Cell

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
def settingTrueFirstRun(grid):

    for y in range(0, len(grid)):
        grid[y][0].setVisited(True)
        grid[y][len(grid[y])-1].setVisited(True)

    for x in range(0, len(grid[0])):
        grid[0][x].setVisited(True)

# this changes all the walls on the bottom to true visited to only allow one exit point
def settingTrueSecRun(grid):
    for x in range(0, len(grid[0])):
        grid[len(grid)-1][x].setVisited(True)

# moving through the maze to make sure there are walls on either side
def settingWalls(grid, curr, nextC):
    cy, cx = curr.coords()
    ny, nx = nextC.coords()

    direction = (ny-cy, nx-cx)

    # solving edgecases that might turn up
    if (cy-1 < 0 or cy+1 >= len(grid)) or (cx-1 < 0 or cx+1 >= (len(grid[0]))):
        return

    if direction[1]:
        grid[cy+1][cx].setVisited(True)
        grid[cy-1][cx].setVisited(True)
    elif direction[0]:
        grid[cy][cx+1].setVisited(True)
        grid[cy][cx-1].setVisited(True)

# main method for this file
# does a backtracking algo to create a maze
def create(grid):

    stack = []

    # Randomly choose the starting position
    initial = random.randrange(1, len(grid[0])-1)
    curr = grid[0][initial]

    curr.setVisited(True)
    curr.setElement(' ')
    stack.append(curr)

    settingTrueFirstRun(grid)

    while(stack):
        curr = stack.pop()
        neighbours = curr.findUnvisited(grid)
        if(neighbours):
            stack.append(curr)

            ran = random.randrange(0, len(neighbours))

            y, x = neighbours[ran]

            nextC = grid[y][x]
            nextC.setElement(' ')
            nextC.setVisited(True)

            if y is (len(grid)-1):
                settingTrueSecRun(grid)
            
            settingWalls(grid, curr, nextC)
            


            stack.append(nextC)