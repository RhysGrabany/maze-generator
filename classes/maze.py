#!/usr/bin/python3

from PIL import Image, ImageOps

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
        #self.m_MazeImage = Image.new("RGB", (self.m_Rows+2, self.m_Cols+2), "#ffffff")
        #self.m_MazeEnhancedImage = Image.new("RGB", ((self.m_Rows*2)+2, (self.m_Cols*2)+2), "#ffffff")

        self.m_Name = "MAZE_" + str(cols) + "x" + str(rows)
        self.m_EName = "MAZE_" + str(cols*2) + "x" + str(rows*2)

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
        im = Image.new("RGB", (self.m_Rows+2, self.m_Cols+2), "#ffffff")
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
    
    def save_image(self):
        self.m_MazeImage.save(self.m_Name + ".png")
        self.m_MazeEnhancedImage.save(self.m_EName + ".png")
    

    def setting_increase(self, pixels, y, x, color):

        pixels[y, x] = color
        pixels[y, x+1] = color
        pixels[y+1, x] = color
        pixels[y+1, x+1] = color

    def increase_image_size(self):

        im = Image.new("RGB", ((self.m_Rows*2)+2, (self.m_Cols*2)+2), "#ffffff")
        pixels = im.load()

        for y in range(0, self.m_Rows):
            for x in range(0, self.m_Cols):
                offset_y = (y+1)+y
                offset_x = (x+1)+x

                t_ele = self.m_Maze[y][x].getElement()

                if t_ele is "#":
                    self.setting_increase(pixels, offset_y, offset_x, (0, 0, 0))
                elif t_ele is " ":
                    self.setting_increase(pixels, offset_y, offset_x, (255, 255, 255))
        
        rotated = im.transpose(Image.ROTATE_270)
        flip = ImageOps.mirror(rotated)
        self.m_MazeEnhancedImage = flip


    def save_text(self, path):
        saving = self.m_Maze
        
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
            





