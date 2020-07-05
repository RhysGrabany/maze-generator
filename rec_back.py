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




def solve(grid):

    stack = []

    initial = random.randrange(1, len(grid[0])-1)
    curr = grid[0][initial]

    curr.setVisited(True)
    curr.setElement(' ')
    stack.append(curr)

    while(stack):
        grid.print()
        curr = stack.pop()
        neighbours = curr.findUnvisited(grid)
        if(neighbours):
            stack.append(curr)

            ran = random.randrange(0, len(neighbours))

            y, x = neighbours[ran]
            nextC = grid[y][x]
            nextC.setElement(' ')
            nextC.setVisited(True)
            stack.append(nextC)