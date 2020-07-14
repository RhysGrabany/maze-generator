#!/usr/bin/python3

from PIL import Image, ImageOps
import os

class Maze():
    ###############
    # CONSTRUCTOR #
    ###############
    def __init__(self, cols, rows):
        self.m_Cols = cols
        self.m_Rows = rows
        
        self.m_Maze = []
        self.m_MazeImage = []
        self.m_MazeEnhancedImage = []
        
        self.m_Name = "MAZE_" + str(cols) + "x" + str(rows)
        self.m_EName = ""

        self.fill()

    
    ##############
    # DESTRUCTOR #
    ##############
    def __del__(self):
        del self.m_Maze

    ###########
    # GETTERS #
    ###########
    def getRows(self):
        return self.m_Rows
    def getCols(self):
        return self.m_Cols
    def __getitem__(self, key):
        return self.m_Maze[key]
    def getMazeImage(self):
        return self.m_MazeImage
    def getName(self):
        return self.m_Name

    ###########
    # SETTERS #
    ###########
    def setName(self, name):
        self.m_Name = name


    def __len__(self):
        return len(self.m_Maze)

    ###########
    # METHODS #
    ###########
    def fill(self):
        for y in range(0, self.m_Rows):
            _ = []
            for x in range(0, self.m_Cols):
                _.append(Cell(y, x))
            self.m_Maze.append(_)
    
    def print(self):
        for y in range(0, self.m_Rows):
            _ = []
            for x in range(0, self.m_Cols):
                _.append(self.m_Maze[y][x].getElement())
            print("".join(_))
        print("\n")
    
    def make_image(self):
        rows = self.m_Rows
        cols = self.m_Cols
        im = Image.new("RGB", (rows+2, cols+2), "#ffffff")
        pixels= im.load()

        for y in range(0, self.m_Rows):
            for x in range(0, self.m_Cols):
                if self.m_Maze[y][x].getElement() == '#':
                    pixels[y+1,x+1] = (0, 0, 0)
                elif self.m_Maze[y][x].getElement() == ' ':
                    pixels[y+1, x+1] = (255, 255, 255)

        rotated = im.transpose(Image.ROTATE_270)
        flip = ImageOps.mirror(rotated)
        self.m_MazeImage = flip
    
    def save_image(self, type):
        cwd = os.getcwd()
        img = cwd + "/maze/images/"


        if type is 0:
            self.m_MazeImage.save(img + self.m_Name + ".png")
        else:
            self.m_MazeEnhancedImage.save(img + self.m_EName + ".png")
    
    def save_image_enhanced(self):
        cwd = os.getcwd()
        img = cwd + "/maze/images/"
        self.m_MazeEnhancedImage.save(img + self.m_EName + ".png")

    # 
    def setting_increase(self, pixels, y, x, color, magnitude):

        pixels[y, x] = color
        for m in range(0, magnitude):
            for mp in range(0, magnitude):
                # paints the pixel left to right one row at a time
                print(m, mp)
                pixels[y+m, x+mp] = color

    # this increases the size of the image to each pixel and doubles it
    def increase_image_size(self, m):
        
        new_rows = self.m_Rows*m
        new_cols = self.m_Cols*m
        im = Image.new("RGB", (new_rows+10, new_cols+10), "#ffffff")
        pixels = im.load()

        maze = self.m_Maze

        wall_color = (0, 0, 0)
        path_color = (255, 255, 255)

        for y in range(0, len(maze)):
            for x in range(0, len(maze[y])):
                
                # this offset is where the pixels start and then will continue from where the last calulation will be
                # so if 1x at (0,0) is # and with magnitude 5x - 0,0 until (0,4) will be #####
                # and then the next pixel to the right (0,1) will start at (0,5) and will continue 
                offset_y = y*m+5
                offset_x = x*m+5

                t_ele = self.m_Maze[y][x].getElement()

                if t_ele is "#":
                    self.setting_increase(pixels, offset_y, offset_x, wall_color, m)
                elif t_ele is " ":
                    self.setting_increase(pixels, offset_y, offset_x, path_color, m)
        
        rotated = im.transpose(Image.ROTATE_270)
        flip = ImageOps.mirror(rotated)
        self.m_MazeEnhancedImage = flip

        self.m_EName = "MAZE_" +  str(new_cols) + "x" + str(new_rows)


    # saving the text file to file
    def save_text(self):
        saving = self.m_Maze
        cwd = os.getcwd()
        path = cwd + "/maze/text/" + self.m_Name + ".txt"
        
        with open(path, "w") as f:
            for ele in saving:
                for i in ele:
                    f.write(i.getElement())
                f.write("\n")
        f.close()

class Cell():

    ###############
    # CONSTRUCTOR #
    ###############
    def __init__(self, y, x, element='#', visited=False):
        self.m_X = x
        self.m_Y = y

        self.m_Element = element
        self.m_Visited = visited


    ###########
    # SETTERS #
    ###########
    def setX(self, x):
        self.m_X = x
    def setY(self, y):
        self.m_Y = y
    def setElement(self, element):
        self.m_Element = element
    def setVisited(self, visited):
        self.m_Visited = visited


    ###########
    # GETTERS #
    ###########
    def getX(self):
        return self.m_X
    def getY(self):
        return self.m_Y
    def getElement(self):
        return self.m_Element
    def getVisited(self):
        return self.m_Visited


    ###########
    # METHODS #
    ########### 
    def findUnvisited(self, Maze):
        # the possible directions that can be made
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        available = []
        
        x = self.m_X
        y = self.m_Y

        for y2, x2 in dirs:
            # solving edge cases
            if (y+y2 < 0 or y+y2 >= len(Maze)) or (x+x2 < 0 or x+x2 >= (len(Maze[0]))):
                continue
            if not(Maze[y+y2][x+x2].getVisited()):

                available.append(((y+y2), (x+x2)))
            else:
                continue
        
        return available

    def coords(self):
        return (self.m_Y, self.m_X)
            





