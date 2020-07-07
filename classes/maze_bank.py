#!/usr/bin/python3



class Maze_Bank():
    ###############
    # CONSTRUCTOR #
    ###############
    def __init__(self):
        self.m_Bank = [None]*10
    
    ##############
    # DESTRUCTOR #
    ##############
    def __del__(self):
        del self.m_Bank

    ###########
    # GETTERS #
    ###########
    def getStack(self):
        return self.m_Bank
    def __getitem__(self, key):
        return self.m_Bank[key]


    ###########
    # SETTERS #
    ###########
    def __setitem__(self, key, element):
        self.m_Bank[key] = element
    
    def push(self, key):
        #num_of_mazes = len([x for x in self.m_Bank if x is not None])
        del self.m_Bank[0]
        self.m_Bank.append(key)


    def print(self):
        for i in range(len(self.m_Bank)-1, -1, -1):
            if self.m_Bank[i] is None:
                continue
            else:
                print(str(10-i) + " " + self.m_Bank[i].getName())
